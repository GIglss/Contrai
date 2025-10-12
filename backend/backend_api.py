"""
API Backend Flask para conectar interfaz web con sistema de automatización
"""

import base64
from flask import Flask, request, jsonify, session
from flask_cors import CORS
import os
from datetime import datetime, timedelta
import secrets
import sys
import traceback

from dotenv import load_dotenv

load_dotenv()

# add yapily_sdk to path
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'yapily_sdk/yapily_api_client/api/'))

import yapily_sdk.yapily_api_client as yapily
# import yapily_sdk.yapily_api_client.api as yapily_api
from yapily_sdk.yapily_api_client.api.institutions import get_institutions



class YapilyClientManager:
    _instance = None
    _client = None
    
    def __new__(cls):
        if cls._instance is None:  # Check if instance already exists
            cls._instance = super(YapilyClientManager, cls).__new__(cls)  # Create new instance
        return cls._instance  # Always return the same instance
    
    def get_client(self):
        if self._client is None:
            app_uuid = os.getenv('YAPILY_APP_UUID')
            app_secret = os.getenv('YAPILY_APP_SECRET')
            
            if not app_uuid or not app_secret:
                raise ValueError('Missing Yapily credentials')

            credentials = f"{app_uuid}:{app_secret}"
            encoded_credentials = base64.b64encode(credentials.encode()).decode()
            
            self._client = yapily.Client(
                base_url="https://api.yapily.com",
                headers={
                    'Accept': 'application/json;charset=UTF-8',
                    'Authorization': f'Basic {encoded_credentials}',
                    'Content-Type': 'application/json'
                },
                verify_ssl= False  # For development only; remove in production
            )
        
        return self._client

# Global instance
yapily_manager = YapilyClientManager()


# Importar nuestro sistema de automatización
# from bank_automation import (
#     PlaidAutomation,
#     # YapilyAutomation, 
#     MotorAutomacion, GestorTokens,
#     ejemplo_regla_balance_bajo, ejemplo_regla_ahorro_automatico
# )

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', secrets.token_hex(32))
CORS(app)

# Almacenamiento temporal (usar BD en producción)
user_sessions = {}
automation_engines = {}


# ==================== ENDPOINTS DE REGLAS ====================


# @app.route('/api/get/institutions', methods=['GET'])
# def yapily_get_institutions():
#     """Obtiene la lista de instituciones soportadas por Yapily"""
#     try:
#         cliente = YapilyAutomation(
#             app_key=os.getenv('YAPILY_APP_UUID'),
#             app_secret=os.getenv('YAPILY_APP_SECRET'),
#             environment='sandbox'
#         )
        
#         instituciones = cliente.obtener_instituciones()
        
#         return jsonify({
#             'institutions': instituciones
#         })
    
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


@app.route('/api/get/institutions', methods=['GET'])
def yapily_get_institutions():
    """Obtiene la lista de instituciones"""
    try:
        client = yapily_manager.get_client()
        response = get_institutions.sync(client=client)
        
        institutions_list = []
        if hasattr(response, 'data') and response.data:
            institutions_list = [inst.to_dict() if hasattr(inst, 'to_dict') else inst for inst in response.data]
        elif isinstance(response, list):
            institutions_list = response
        
        return jsonify({
            'institutions': institutions_list,
            'count': len(institutions_list)
        })
    
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
        return jsonify({'error': str(e)}), 500



# ==================== HEALTH CHECK ====================

@app.route('/', methods=['GET'])
def home():
    """Endpoint de prueba"""
    return jsonify({
        'message': 'API de Automatización Financiera',
        'status': 'running',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=3000
    )