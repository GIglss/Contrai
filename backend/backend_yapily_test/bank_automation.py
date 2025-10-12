import base64
"""
Sistema de Automatización de Transacciones Bancarias con Reglas IFTTT
Soporta Plaid y Yapily APIs
"""

import os
from datetime import datetime, timedelta
from typing import List, Dict, Callable
import json

# Instalar: pip install plaid-python requests schedule
try:
    import plaid
    from plaid.api import plaid_api
    from plaid.model.payment_initiation_payment_create_request import PaymentInitiationPaymentCreateRequest
except ImportError:
    print("Instalar: pip install plaid-python")

import requests
import schedule
import time


class ReglaIFTTT:
    """Define una regla IF-THIS-THEN-THAT para automatización"""
    
    def __init__(self, nombre: str, condicion: Callable, accion: Callable, activa: bool = True):
        self.nombre = nombre
        self.condicion = condicion  # Función que retorna True/False
        self.accion = accion  # Función a ejecutar si condición es True
        self.activa = activa
        self.ultima_ejecucion = None
    
    def evaluar(self, contexto: Dict) -> bool:
        """Evalúa si la regla debe ejecutarse"""
        if not self.activa:
            return False
        
        if self.condicion(contexto):
            print(f"✓ Regla '{self.nombre}' activada")
            self.accion(contexto)
            self.ultima_ejecucion = datetime.now()
            return True
        return False


class YapilyAutomation:
    """Cliente para automatización con Yapily"""
    
    def __init__(self, app_key: str, app_secret: str, environment: str = 'sandbox'):
        self.app_key = app_key
        self.app_secret = app_secret
        self.base_url = 'https://api.yapily.com'
        
        # Properly encode credentials for Basic Auth
        credentials = f"{app_key}:{app_secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        
        self.headers = {
            'Accept': 'application/json;charset=UTF-8',
            'Authorization': f'Basic {encoded_credentials}',
            'Content-Type': 'application/json'
        }

    # def obtener_instituciones(self) -> Dict:
    #     """Obtiene las instituciones registradas"""
    #     try:
    #         url = f"{self.base_url}/institutions"
    #         # Remove payload and data parameter - not needed for GET
    #         response = requests.get(url, headers=self.headers, verify=False)
    #         response.raise_for_status()
            
    #         data = response.json()
    #         instituciones = {}
    #         for institucion in data.get('data', []):
    #             institucion_id = institucion.get('id')
    #             instituciones[institucion_id] = {
    #                 'nombre': institucion.get('name'),
    #                 'nombre_completo': institucion.get('fullName'),
    #                 'paises': [pais.get('displayName') for pais in institucion.get('countries', [])],
    #                 'tipo_credenciales': institucion.get('credentialsType'),
    #                 'features': institucion.get('features', []),
    #                 'media': institucion.get('media', [])
    #             }
    #         return data
    #     except requests.exceptions.RequestException as e:
    #         print(f"Error de conexión obteniendo instituciones: {e}")
    #         return {}
    #     except Exception as e:
    #         print(f"Error obteniendo instituciones: {e}")
    #         return {}
    


class MotorAutomacion:
    """Motor principal para ejecutar reglas IFTTT"""
    
    def __init__(self, cliente_banco, user_id=None):
        self.cliente = cliente_banco
        self.user_id = user_id
        self.reglas: List[ReglaIFTTT] = []
        self.access_token = None  # Token de acceso a la cuenta bancaria
    
    def agregar_regla(self, regla: ReglaIFTTT):
        """Agrega una nueva regla al motor"""
        self.reglas.append(regla)
        print(f"Regla '{regla.nombre}' agregada")
    
    def ejecutar_reglas(self):
        """Ejecuta todas las reglas activas"""
        print(f"\n--- Ejecutando reglas: {datetime.now()} ---")
        
        # Obtener contexto actual
        contexto = {
            'balances': self.cliente.obtener_balance(self.access_token),
            'transacciones': self.cliente.obtener_transacciones(self.access_token, dias=7),
            'fecha': datetime.now(),
            'cliente': self.cliente,
            'access_token': self.access_token
        }
        
        # Evaluar cada regla
        for regla in self.reglas:
            try:
                regla.evaluar(contexto)
            except Exception as e:
                print(f"Error ejecutando regla '{regla.nombre}': {e}")
    
    def iniciar_programacion(self, intervalo_minutos: int = 60):
        """Inicia la ejecución programada de reglas"""
        schedule.every(intervalo_minutos).minutes.do(self.ejecutar_reglas)
        
        print(f"Motor iniciado. Ejecutando cada {intervalo_minutos} minutos...")
        print("Presiona Ctrl+C para detener\n")
        
        # Ejecutar una vez al inicio
        self.ejecutar_reglas()
        
        # Loop principal
        while True:
            schedule.run_pending()
            time.sleep(1)
            
    def configurar_acceso_inicial(self, token: str, expiracion=None):
        """Configura el token de acceso inicial"""
        self.access_token = token
        self.expiracion = expiracion
        print(f"Token configurado para usuario {self.user_id}")

class GestorTokens:
    """Gestor para validar y manejar tokens de acceso"""
    
    def __init__(self):
        self.tokens = {}  # In production, use a database
    
    def token_valido(self, user_id: str) -> bool:
        """Verifica si el token del usuario es válido"""
        # Simple validation - in production, check expiration dates
        return user_id in self.tokens
    
    def guardar_token(self, user_id: str, token: str, expiracion=None):
        """Guarda un token para el usuario"""
        self.tokens[user_id] = {
            'token': token,
            'expiracion': expiracion,
            'guardado_en': datetime.now()
        }
    
    def obtener_token(self, user_id: str):
        """Obtiene el token del usuario"""
        return self.tokens.get(user_id, {}).get('token')
    
# ==================== EJEMPLOS DE REGLAS IFTTT ====================

def ejemplo_regla_balance_bajo(monto_minimo: float = 100):
    """Regla: Si el balance es menor a X, enviar alerta"""
    
    def condicion(ctx: Dict) -> bool:
        balances = ctx['balances']
        for account_id, info in balances.items():
            if info['disponible'] < monto_minimo:
                ctx['cuenta_baja'] = info
                return True
        return False
    
    def accion(ctx: Dict):
        cuenta = ctx['cuenta_baja']
        print(f"⚠️  ALERTA: Balance bajo en {cuenta['nombre']}: {cuenta['disponible']} {cuenta['moneda']}")
        # Aquí podrías enviar email, SMS, etc.
    
    return ReglaIFTTT("Balance Bajo", condicion, accion)


def ejemplo_regla_ahorro_automatico(porcentaje: float = 0.1):
    """Regla: Si hay ingresos, transferir X% a cuenta de ahorros"""
    
    def condicion(ctx: Dict) -> bool:
        transacciones = ctx['transacciones']
        ingresos_recientes = [tx for tx in transacciones if tx['monto'] < 0]  # Plaid usa negativos para ingresos
        
        if ingresos_recientes:
            ctx['total_ingresos'] = sum(abs(tx['monto']) for tx in ingresos_recientes)
            return True
        return False
    
    def accion(ctx: Dict):
        monto_ahorrar = ctx['total_ingresos'] * porcentaje
        print(f"💰 Ahorro automático: Transferir {monto_ahorrar:.2f} a cuenta de ahorros")
        # Aquí ejecutarías la transferencia real
    
    return ReglaIFTTT("Ahorro Automático", condicion, accion)


def ejemplo_regla_gasto_excesivo(categoria: str, limite: float):
    """Regla: Si gastos en categoría superan límite, alertar"""
    
    def condicion(ctx: Dict) -> bool:
        transacciones = ctx['transacciones']
        gastos_categoria = [
            tx for tx in transacciones 
            if tx['monto'] > 0 and categoria.lower() in str(tx.get('categoria', '')).lower()
        ]
        
        if gastos_categoria:
            total = sum(tx['monto'] for tx in gastos_categoria)
            if total > limite:
                ctx['total_gastado'] = total
                ctx['categoria_excedida'] = categoria
                return True
        return False
    
    def accion(ctx: Dict):
        print(f"🚨 Has gastado {ctx['total_gastado']:.2f} en {ctx['categoria_excedida']} (límite: {limite})")
    
    return ReglaIFTTT(f"Límite {categoria}", condicion, accion)


def ejemplo_regla_pago_recurrente(dia_mes: int, beneficiario_id: str, monto: float):
    """Regla: Cada día X del mes, hacer un pago automático"""
    
    def condicion(ctx: Dict) -> bool:
        fecha_actual = ctx['fecha']
        if fecha_actual.day == dia_mes:
            # Verificar que no se haya ejecutado hoy
            return True
        return False
    
    def accion(ctx: Dict):
        print(f"📅 Ejecutando pago recurrente de {monto}")
        # cliente = ctx['cliente']
        # resultado = cliente.iniciar_pago(beneficiario_id, f"Pago mensual {dia_mes}", monto)
        # print(f"Resultado: {resultado}")
    
    return ReglaIFTTT("Pago Recurrente", condicion, accion)


# ==================== EJEMPLO DE USO ====================

if __name__ == "__main__":
    # Configuración (usar variables de entorno en producción)
    USAR_PLAID = True  # Cambiar a False para usar Yapily
    
    if USAR_PLAID:
        # Configurar Plaid
        cliente = PlaidAutomation(
            client_id=os.getenv('PLAID_CLIENT_ID', 'tu_client_id'),
            secret=os.getenv('PLAID_SECRET', 'tu_secret'),
            environment='sandbox'
        )
        ACCESS_TOKEN = os.getenv('PLAID_ACCESS_TOKEN', 'access-sandbox-xxxx')
    else:
        # Configurar Yapily
        cliente = YapilyAutomation(
            app_key=os.getenv('YAPILY_APP_KEY', 'tu_app_key'),
            app_secret=os.getenv('YAPILY_APP_SECRET', 'tu_app_secret'),
            environment='sandbox'
        )
        ACCESS_TOKEN = os.getenv('YAPILY_CONSENT_TOKEN', 'consent-token-xxxx')
    
    # Crear motor de automatización
    motor = MotorAutomacion(cliente)
    motor.access_token = ACCESS_TOKEN
    
    # Agregar reglas IFTTT
    motor.agregar_regla(ejemplo_regla_balance_bajo(monto_minimo=500))
    motor.agregar_regla(ejemplo_regla_ahorro_automatico(porcentaje=0.15))
    motor.agregar_regla(ejemplo_regla_gasto_excesivo("restaurantes", limite=300))
    motor.agregar_regla(ejemplo_regla_pago_recurrente(dia_mes=1, beneficiario_id="recip_xxx", monto=100))
    
    # Ejecutar una sola vez (para testing)
    motor.ejecutar_reglas()
    
    # O iniciar ejecución programada
    # motor.iniciar_programacion(intervalo_minutos=60)
