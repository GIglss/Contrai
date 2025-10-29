"""
Enhanced Financial Agent for Contrai Application
Integrates agent framework with Plaid financial data
"""

import json
import os
import asyncio
import uuid
from datetime import datetime
from typing import Annotated, Dict, Any, List, Optional
from random import randint

from pydantic import Field
from agent_framework import ChatAgent, ChatMessage, Role, ai_function
from agent_framework.azure import AzureOpenAIChatClient


class ContraiMemoryManager:
    """Memory manager for Contrai financial conversations."""
    
    def __init__(self, storage_path: str = "./contrai_memory"):
        self.storage_path = storage_path
        os.makedirs(storage_path, exist_ok=True)
    
    def save_conversation_data(self, user_id: str, data: Dict[str, Any]) -> None:
        """Save user conversation data and preferences."""
        file_path = os.path.join(self.storage_path, f"user_{user_id}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    
    def load_conversation_data(self, user_id: str) -> Dict[str, Any]:
        """Load user conversation data and preferences."""
        file_path = os.path.join(self.storage_path, f"user_{user_id}.json")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}
    
    def save_financial_insights(self, user_id: str, insights: str) -> None:
        """Save AI-generated financial insights for user."""
        data = self.load_conversation_data(user_id)
        if "insights_history" not in data:
            data["insights_history"] = []
        
        data["insights_history"].append({
            "timestamp": datetime.now().isoformat(),
            "insight": insights
        })
        
        # Keep only last 10 insights
        if len(data["insights_history"]) > 10:
            data["insights_history"] = data["insights_history"][-10:]
        
        self.save_conversation_data(user_id, data)


class ContraiSessionManager:
    """Session manager for Contrai financial conversations."""
    
    def __init__(self, storage_path: str = "./contrai_sessions"):
        self.storage_path = storage_path
        os.makedirs(storage_path, exist_ok=True)
    
    def save_session(self, session_id: str, serialized_thread: Dict[str, Any]) -> None:
        """Save conversation thread state."""
        file_path = os.path.join(self.storage_path, f"session_{session_id}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_thread, f, indent=2)
    
    def load_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Load conversation thread state."""
        file_path = os.path.join(self.storage_path, f"session_{session_id}.json")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return None
    
    def list_user_sessions(self, user_id: str) -> List[str]:
        """List all sessions for a specific user."""
        sessions = []
        for file in os.listdir(self.storage_path):
            if file.startswith("session_") and file.endswith(".json"):
                session_id = file[8:-5]  # Remove "session_" prefix and ".json" suffix
                if session_id.startswith(user_id):
                    sessions.append(session_id)
        return sessions


# Financial AI Functions with approval controls
@ai_function
def get_account_summary(user_financial_data: Annotated[str, Field(description="JSON string of user's financial data")]) -> str:
    """Get a summary of user's accounts and balances."""
    try:
        data = json.loads(user_financial_data)
        accounts = data.get('accounts', [])
        
        if not accounts:
            return "No accounts found. Please connect your bank accounts first."
        
        total_balance = sum(acc.get('balance', 0) or 0 for acc in accounts)
        account_count = len(accounts)
        
        summary = f"Account Summary:\n"
        summary += f"• Total Balance: ${total_balance:,.2f}\n"
        summary += f"• Connected Accounts: {account_count}\n\n"
        
        for acc in accounts[:5]:  # Show first 5 accounts
            balance = acc.get('balance', 0) or 0
            name = acc.get('name', 'Unknown Account')
            bank = acc.get('bank', 'Unknown Bank')
            summary += f"• {name} ({bank}): ${balance:,.2f}\n"
        
        return summary
    except Exception as e:
        return f"Error analyzing account data: {str(e)}"


@ai_function(approval_mode="always_require")
def create_savings_rule_suggestion(
    user_financial_data: Annotated[str, Field(description="JSON string of user's financial data")],
    savings_percentage: Annotated[float, Field(description="Suggested savings percentage (1-50)")],
    target_account: Annotated[str, Field(description="Name of target savings account")]
) -> str:
    """Suggest creating a new automated savings rule (requires approval)."""
    try:
        data = json.loads(user_financial_data)
        accounts = data.get('accounts', [])
        
        if savings_percentage < 1 or savings_percentage > 50:
            return "Savings percentage must be between 1% and 50%"
        
        checking_accounts = [acc for acc in accounts if 'checking' in acc.get('type', '').lower()]
        if not checking_accounts:
            return "No checking accounts found to create savings rule from."
        
        primary_account = checking_accounts[0]
        current_balance = primary_account.get('balance', 0) or 0
        monthly_transfer = current_balance * (savings_percentage / 100)
        
        suggestion = f"💡 Savings Rule Suggestion:\n\n"
        suggestion += f"From: {primary_account.get('name')} (${current_balance:,.2f})\n"
        suggestion += f"To: {target_account}\n"
        suggestion += f"Amount: {savings_percentage}% monthly (≈${monthly_transfer:,.2f})\n\n"
        suggestion += f"This rule would automatically transfer ${monthly_transfer:,.2f} monthly to build your savings!"
        
        return suggestion
    except Exception as e:
        return f"Error creating savings rule suggestion: {str(e)}"


@ai_function(approval_mode="always_require")
def analyze_spending_patterns(
    user_financial_data: Annotated[str, Field(description="JSON string of user's financial data")]
) -> str:
    """Analyze user's spending patterns and provide insights (requires approval)."""
    try:
        data = json.loads(user_financial_data)
        accounts = data.get('accounts', [])
        rules = data.get('rules', [])
        
        if not accounts:
            return "No account data available for spending analysis."
        
        total_balance = sum(acc.get('balance', 0) or 0 for acc in accounts)
        active_rules = [r for r in rules if r.get('is_active')]
        
        analysis = f"📊 Financial Analysis:\n\n"
        analysis += f"Total Portfolio: ${total_balance:,.2f}\n"
        analysis += f"Active Rules: {len(active_rules)}\n\n"
        
        # Account type distribution
        checking_balance = sum(acc.get('balance', 0) or 0 for acc in accounts if 'checking' in acc.get('type', '').lower())
        savings_balance = sum(acc.get('balance', 0) or 0 for acc in accounts if 'savings' in acc.get('type', '').lower())
        
        if checking_balance > 0:
            analysis += f"💰 Checking: ${checking_balance:,.2f} ({checking_balance/total_balance*100:.1f}%)\n"
        if savings_balance > 0:
            analysis += f"🏦 Savings: ${savings_balance:,.2f} ({savings_balance/total_balance*100:.1f}%)\n"
        
        # Recommendations
        analysis += f"\n💡 Recommendations:\n"
        if checking_balance > savings_balance * 3:
            analysis += f"• Consider moving some checking funds to savings\n"
        if len(active_rules) == 0:
            analysis += f"• Set up automated transfer rules for better money management\n"
        
        return analysis
    except Exception as e:
        return f"Error analyzing spending patterns: {str(e)}"


@ai_function
def get_rules_summary(user_financial_data: Annotated[str, Field(description="JSON string of user's financial data")]) -> str:
    """Get a summary of user's active transfer rules."""
    try:
        data = json.loads(user_financial_data)
        rules = data.get('rules', [])
        
        if not rules:
            return "No transfer rules configured. Consider setting up automated transfers to optimize your money management!"
        
        active_rules = [r for r in rules if r.get('is_active')]
        inactive_rules = [r for r in rules if not r.get('is_active')]
        
        summary = f"Transfer Rules Summary:\n\n"
        summary += f"• Active Rules: {len(active_rules)}\n"
        summary += f"• Inactive Rules: {len(inactive_rules)}\n\n"
        
        if active_rules:
            summary += "Active Rules:\n"
            for rule in active_rules[:3]:  # Show first 3 rules
                amount_info = f"{rule.get('percentage')}%" if rule.get('transfer_type') == 'percentage' else f"${rule.get('amount')}"
                summary += f"• {rule.get('name')}: {amount_info} {rule.get('frequency', 'monthly')}\n"
        
        return summary
    except Exception as e:
        return f"Error getting rules summary: {str(e)}"


class ContraiFinancialAgent:
    """Main financial agent for Contrai application."""
    
    def __init__(
        self,
        azure_endpoint: str,
        deployment_name: str,
        api_version: str,
        api_key: str,
        memory_path: str = "./contrai_memory",
        sessions_path: str = "./contrai_sessions"
    ):
        self.memory_manager = ContraiMemoryManager(memory_path)
        self.session_manager = ContraiSessionManager(sessions_path)
        
        # Initialize the financial agent
        self.agent = ChatAgent(
            chat_client=AzureOpenAIChatClient(
                endpoint=azure_endpoint,
                deployment_name=deployment_name,
                api_version=api_version,
                api_key=api_key,
            ),
            name="Contrai Financial Assistant",
            instructions="""You are Contrai's AI Financial Assistant, specialized in personal finance management.

Your capabilities:
- Analyze connected bank accounts and balances
- Review and suggest automated transfer rules
- Provide personalized financial insights and recommendations
- Help users optimize their money management through automation

Key features of Contrai:
- Users connect bank accounts via Plaid
- Create automated transfer rules (percentage or fixed amount)
- Monitor money flows between accounts
- Set custom names for accounts

When responding:
- Be helpful, concise, and actionable
- Reference specific accounts and rules when available
- Suggest practical improvements to financial automation
- Use emojis sparingly but effectively (💰 💡 📊)
- Always ask for approval before making specific rule suggestions
- Keep responses focused on the user's actual financial data

You have access to specialized functions for:
- Getting account summaries
- Analyzing spending patterns (requires approval)
- Creating savings rule suggestions (requires approval)
- Reviewing transfer rules"""
        )
        
        # Available financial tools
        self.tools = [
            get_account_summary,
            get_rules_summary,
            create_savings_rule_suggestion,
            analyze_spending_patterns
        ]
    
    async def start_conversation(self, user_id: str, session_id: Optional[str] = None) -> str:
        """Start a new financial conversation."""
        if session_id is None:
            session_id = f"{user_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        thread = self.agent.get_new_thread()
        
        # Load user conversation context
        user_data = self.memory_manager.load_conversation_data(user_id)
        if user_data.get("insights_history"):
            last_insight = user_data["insights_history"][-1]["insight"]
            context_message = f"Previous financial insight: {last_insight[:200]}..."
            await self.agent.run(context_message, thread=thread)
        
        # Save initial session state
        serialized_thread = await thread.serialize()
        self.session_manager.save_session(session_id, serialized_thread)
        
        return session_id
    
    async def chat_with_financial_context(
        self, 
        message: str, 
        session_id: str, 
        user_id: str,
        financial_context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Chat with financial context integration."""
        try:
            # Load session
            session_data = self.session_manager.load_session(session_id)
            if not session_data:
                # Create new session if not found
                session_id = await self.start_conversation(user_id, session_id)
                session_data = self.session_manager.load_session(session_id)
            
            thread = await self.agent.deserialize_thread(session_data)
            
            # Build context-aware message
            if financial_context:
                context_str = json.dumps(financial_context)
                enhanced_message = f"""User question: {message}

Available financial data: {context_str}

Please use the appropriate functions to analyze this financial data and provide helpful insights."""
            else:
                enhanced_message = message
            
            # Process with agent
            result = await self.agent.run(enhanced_message, thread=thread)
            
            # Save updated session
            serialized_thread = await thread.serialize()
            self.session_manager.save_session(session_id, serialized_thread)
            
            # Save insights to memory
            if len(result.text) > 50:  # Only save substantial responses
                self.memory_manager.save_financial_insights(user_id, result.text[:500])
            
            return {
                'success': True,
                'response': result.text,
                'session_id': session_id,
                'requires_approval': bool(result.user_input_requests),
                'pending_approvals': [
                    {
                        'function_name': req.function_call.name,
                        'arguments': req.function_call.arguments,
                        'approval_id': str(uuid.uuid4())
                    }
                    for req in result.user_input_requests
                ] if result.user_input_requests else []
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f"Financial agent error: {str(e)}",
                'session_id': session_id
            }
    
    async def handle_approval_response(
        self,
        session_id: str,
        approval_id: str,
        approved: bool,
        user_id: str
    ) -> Dict[str, Any]:
        """Handle user approval response for pending function calls."""
        try:
            # This would be implemented to handle specific approval workflows
            # For now, return a placeholder response
            
            response_message = f"Approval {'granted' if approved else 'denied'} for function call."
            
            if approved:
                response_message += " The requested financial analysis will be performed."
            else:
                response_message += " No action will be taken. Feel free to ask other questions!"
            
            return {
                'success': True,
                'response': response_message,
                'session_id': session_id
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f"Approval handling error: {str(e)}",
                'session_id': session_id
            }
    
    def get_user_sessions(self, user_id: str) -> List[str]:
        """Get all sessions for a user."""
        return self.session_manager.list_user_sessions(user_id)
    
    def get_user_insights_history(self, user_id: str) -> List[Dict[str, Any]]:
        """Get user's financial insights history."""
        data = self.memory_manager.load_conversation_data(user_id)
        return data.get('insights_history', [])


# Factory function for easy integration
def create_contrai_financial_agent(
    azure_endpoint: str,
    deployment_name: str,
    api_version: str,
    api_key: str
) -> ContraiFinancialAgent:
    """Factory function to create Contrai financial agent."""
    return ContraiFinancialAgent(
        azure_endpoint=azure_endpoint,
        deployment_name=deployment_name,
        api_version=api_version,
        api_key=api_key
    )