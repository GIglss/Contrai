"""
Simple conversation history endpoint for Contrai chat.
"""

import json
import os
from typing import Dict, Any, List, Optional
from datetime import datetime

def get_conversation_from_session_file(session_id: str) -> Optional[List[Dict[str, Any]]]:
    """
    Load conversation history from session file and convert to frontend format.
    
    Args:
        session_id: The session identifier
        
    Returns:
        List of messages in frontend format, or None if session not found
    """
    try:
        # Path to session files (relative to this script)
        sessions_path = os.path.join(os.path.dirname(__file__), 'contrai_chat_sessions')
        session_file = os.path.join(sessions_path, f'{session_id}.json')
        
        if not os.path.exists(session_file):
            print(f"Session file not found: {session_file}")
            return None
            
        # Load the session data
        with open(session_file, 'r', encoding='utf-8') as f:
            session_data = json.load(f)
            
        # Navigate the nested structure to get messages
        chat_store = session_data.get('chat_message_store_state', {})
        backend_messages = chat_store.get('messages', [])
        
        # Convert backend format to frontend format
        frontend_messages = []
        for i, msg in enumerate(backend_messages):
            # Extract role
            role_obj = msg.get('role', {})
            role = role_obj.get('value', 'assistant')
            
            # Extract content
            contents = msg.get('contents', [])
            content = ""
            if contents and len(contents) > 0:
                content = contents[0].get('text', '')
            
            # Create frontend message
            frontend_message = {
                'id': f"{role}-{i}",
                'role': role,
                'content': content,
                'timestamp': datetime.now().isoformat()  # Using current time as fallback
            }
            
            frontend_messages.append(frontend_message)
            
        print(f"Successfully loaded {len(frontend_messages)} messages for session {session_id}")
        return frontend_messages
        
    except Exception as e:
        print(f"Error loading conversation for session {session_id}: {e}")
        return None

# def add_conversation_endpoint(app):
#     """Add conversation history endpoint to Flask app."""
    
#     @app.route('/api/get-conversation-history/<session_id>', methods=['GET'])
#     def get_conversation_history(session_id):
#         """Get conversation history for a session."""
#         from flask import jsonify
        
#         try:
#             messages = get_conversation_from_session_file(session_id)
            
#             if messages is None:
#                 return jsonify({
#                     'success': False,
#                     'error': 'Session not found',
#                     'session_id': session_id,
#                     'messages': []
#                 }), 404
            
#             return jsonify({
#                 'success': True,
#                 'session_id': session_id,
#                 'messages': messages,
#                 'message_count': len(messages)
#             })
            
#         except Exception as e:
#             print(f"Error in get_conversation_history endpoint: {e}")
#             return jsonify({
#                 'success': False,
#                 'error': str(e),
#                 'session_id': session_id,
#                 'messages': []
#             }), 500