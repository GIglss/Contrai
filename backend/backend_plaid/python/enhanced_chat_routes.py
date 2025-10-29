"""
Enhanced financial chat endpoints for Contrai server.py
Add these routes to your existing server.py file.
"""

# Add these imports to the top of your server.py file:
from financial_agent import create_contrai_financial_agent, ContraiFinancialAgent
import asyncio
from datetime import datetime
import uuid

# Global agent instance (initialize once)
financial_agent = None

def get_financial_agent():
    """Get or create the financial agent instance."""
    global financial_agent
    if financial_agent is None:
        financial_agent = create_contrai_financial_agent(
            azure_endpoint=AZURE_ENDPOINT,
            deployment_name=DEPLOYMENT_NAME,
            api_version=API_VERSION,
            api_key=API_KEY
        )
    return financial_agent

def get_enhanced_financial_context():
    """Get enhanced financial context with more detailed analysis."""
    try:
        context = {}
        
        # Get accounts data with enhanced details
        tokens_file_path = os.path.join(os.path.dirname(__file__), 'tokens.json')
        if os.path.exists(tokens_file_path):
            with open(tokens_file_path, 'r') as f:
                tokens_data = json.load(f)
            
            accounts = []
            total_checking = 0
            total_savings = 0
            
            for item_id, token_info in tokens_data.items():
                access_token_for_item = token_info.get('access_token')
                bank_name = token_info.get('bank_name', 'Unknown Bank')
                custom_name = token_info.get('custom_name')
                
                if access_token_for_item:
                    try:
                        request_obj = AccountsGetRequest(access_token=access_token_for_item)
                        response = client.accounts_get(request_obj)
                        
                        for account in response['accounts']:
                            balances = account.get('balances', {})
                            balance = balances.get('available') or balances.get('current') or 0
                            account_type = str(account.get('type', '')).lower()
                            
                            # Categorize balances
                            if 'checking' in account_type:
                                total_checking += balance
                            elif 'savings' in account_type:
                                total_savings += balance
                            
                            accounts.append({
                                'account_id': account.get('account_id'),
                                'name': custom_name or account.get('name'),
                                'bank': bank_name,
                                'type': account_type,
                                'subtype': str(account.get('subtype', '')),
                                'balance': balance,
                                'currency': balances.get('iso_currency_code', 'USD'),
                                'mask': account.get('mask', '****')
                            })
                    except Exception as e:
                        print(f"Error getting account data for context: {e}")
                        continue
            
            context['accounts'] = accounts
            context['total_checking'] = total_checking
            context['total_savings'] = total_savings
            context['total_balance'] = total_checking + total_savings
        
        # Get rules data with enhanced analysis
        rules_file_path = os.path.join(os.path.dirname(__file__), 'rules.json')
        if os.path.exists(rules_file_path):
            with open(rules_file_path, 'r') as f:
                rules_data = json.load(f)
            
            rules = []
            active_count = 0
            total_monthly_transfers = 0
            
            for rule in rules_data.get('rules', []):
                is_active = rule.get('isActive', False)
                if is_active:
                    active_count += 1
                    # Estimate monthly transfer amount
                    if rule.get('transferType') == 'percentage' and rule.get('percentage'):
                        estimated_amount = (total_checking * rule.get('percentage', 0)) / 100
                    else:
                        estimated_amount = rule.get('amount', 0) or 0
                    total_monthly_transfers += estimated_amount
                
                rules.append({
                    'id': rule.get('id'),
                    'name': rule.get('name'),
                    'description': rule.get('description'),
                    'from_account': rule.get('fromAccount'),
                    'to_account': rule.get('toAccount'),
                    'transfer_type': rule.get('transferType'),
                    'amount': rule.get('amount'),
                    'percentage': rule.get('percentage'),
                    'frequency': rule.get('frequency'),
                    'is_active': is_active,
                    'created_at': rule.get('createdAt'),
                    'last_executed': rule.get('lastExecuted')
                })
            
            context['rules'] = rules
            context['active_rules_count'] = active_count
            context['estimated_monthly_transfers'] = total_monthly_transfers
        
        return context
    except Exception as e:
        print(f"Error getting enhanced financial context: {e}")
        return {}

@app.route('/api/financial-chat-agent', methods=['POST'])
def financial_chat_agent():
    """
    Enhanced financial chat using agent framework.
    Expected payload:
    {
        "message": "User's question about their finances",
        "user_id": "unique-user-identifier",
        "session_id": "optional-session-id",
        "include_context": true
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({'error': 'Message is required'}), 400
        
        # Validate Azure OpenAI configuration
        if not all([API_KEY, API_VERSION, AZURE_ENDPOINT, DEPLOYMENT_NAME]):
            return jsonify({'error': 'Azure OpenAI configuration incomplete'}), 500
        
        user_message = data['message']
        user_id = data.get('user_id', 'default_user')
        session_id = data.get('session_id')
        include_context = data.get('include_context', True)
        
        # Get financial context if requested
        financial_context = get_enhanced_financial_context() if include_context else {}
        
        # Get the financial agent
        agent = get_financial_agent()
        
        # Run the async chat function
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            if not session_id:
                # Create new session
                session_id = loop.run_until_complete(
                    agent.start_conversation(user_id)
                )
            
            # Chat with financial context
            result = loop.run_until_complete(
                agent.chat_with_financial_context(
                    message=user_message,
                    session_id=session_id,
                    user_id=user_id,
                    financial_context=financial_context
                )
            )
        finally:
            loop.close()
        
        if result['success']:
            return jsonify({
                'response': result['response'],
                'session_id': result['session_id'],
                'requires_approval': result.get('requires_approval', False),
                'pending_approvals': result.get('pending_approvals', []),
                'timestamp': datetime.now().isoformat(),
                'context_included': include_context,
                'user_id': user_id
            })
        else:
            return jsonify({
                'error': result['error'],
                'session_id': session_id
            }), 500
            
    except Exception as e:
        print(f"Error in financial_chat_agent: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/financial-chat-agent/approval', methods=['POST'])
def handle_approval():
    """
    Handle approval responses for financial agent.
    Expected payload:
    {
        "session_id": "session-id",
        "approval_id": "approval-id",
        "approved": true/false,
        "user_id": "user-id"
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Request data is required'}), 400
        
        session_id = data.get('session_id')
        approval_id = data.get('approval_id')
        approved = data.get('approved', False)
        user_id = data.get('user_id', 'default_user')
        
        if not all([session_id, approval_id]):
            return jsonify({'error': 'session_id and approval_id are required'}), 400
        
        # Get the financial agent
        agent = get_financial_agent()
        
        # Run the async approval handler
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            result = loop.run_until_complete(
                agent.handle_approval_response(
                    session_id=session_id,
                    approval_id=approval_id,
                    approved=approved,
                    user_id=user_id
                )
            )
        finally:
            loop.close()
        
        if result['success']:
            return jsonify({
                'response': result['response'],
                'session_id': result['session_id'],
                'timestamp': datetime.now().isoformat()
            })
        else:
            return jsonify({
                'error': result['error'],
                'session_id': session_id
            }), 500
            
    except Exception as e:
        print(f"Error in handle_approval: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/financial-chat-agent/sessions/<user_id>', methods=['GET'])
def get_user_sessions(user_id):
    """Get all chat sessions for a user."""
    try:
        agent = get_financial_agent()
        sessions = agent.get_user_sessions(user_id)
        
        return jsonify({
            'user_id': user_id,
            'sessions': sessions,
            'session_count': len(sessions)
        })
        
    except Exception as e:
        print(f"Error getting user sessions: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/financial-chat-agent/insights/<user_id>', methods=['GET'])
def get_user_insights(user_id):
    """Get financial insights history for a user."""
    try:
        agent = get_financial_agent()
        insights = agent.get_user_insights_history(user_id)
        
        return jsonify({
            'user_id': user_id,
            'insights_history': insights,
            'insights_count': len(insights)
        })
        
    except Exception as e:
        print(f"Error getting user insights: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/financial-chat-agent/context', methods=['GET'])
def get_financial_context_endpoint():
    """Get current financial context for debugging."""
    try:
        context = get_enhanced_financial_context()
        return jsonify(context)
    except Exception as e:
        print(f"Error getting financial context: {e}")
        return jsonify({'error': str(e)}), 500