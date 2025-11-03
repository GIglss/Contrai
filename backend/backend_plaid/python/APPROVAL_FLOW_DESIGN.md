# Diseño del Flujo de Aprobación - Contrai Financial Agent

## Problema Resuelto
El agente necesitaba un sistema para pausar conversaciones cuando requiere aprobación del usuario y luego reanudarlas exactamente donde se quedó.

## Arquitectura de la Solución

### 1. Flujo Principal (`/api/financial-chat-agent`)

**Input:**
```json
{
  "message": "Please analyze my spending patterns",
  "session_id": "session_123",
  "include_context": true
}
```

**Proceso:**
1. Carga o crea un thread de conversación
2. Ejecuta el agente con el mensaje del usuario
3. **Si requiere aprobación:**
   - Guarda el estado del thread ANTES de responder
   - Guarda los detalles de aprobación en `{session_id}_pending.json`
   - Retorna `requires_approval: true`
4. **Si no requiere aprobación:**
   - Guarda el thread actualizado
   - Retorna la respuesta normalmente

**Output cuando requiere aprobación:**
```json
{
  "response": "I need your approval to perform detailed financial analysis...",
  "session_id": "session_123",
  "requires_approval": true,
  "pending_approvals": [
    {
      "function_name": "analyze_spending_patterns",
      "arguments": {"user_financial_data": "..."},
      "approval_id": "uuid-123"
    }
  ],
  "timestamp": "2025-11-02T..."
}
```

### 2. Flujo de Aprobación (`/api/financial-chat-agent/approval`)

**Input:**
```json
{
  "session_id": "session_123",
  "approved": true,
  "user_id": "user_456"
}
```

**Proceso:**
1. Carga los datos de aprobación pendiente desde `{session_id}_pending.json`
2. Carga el thread de conversación desde `{session_id}.json`
3. Reconstruye el contexto siguiendo el patrón del Agent Framework:
   ```python
   new_inputs = [original_query]
   
   # Para cada solicitud de aprobación pendiente:
   new_inputs.append(ChatMessage(role=Role.ASSISTANT, contents=[user_input_needed]))
   new_inputs.append(ChatMessage(role=Role.USER, contents=[user_input_needed.create_response(approved)]))
   ```
4. Ejecuta el agente con el contexto completo
5. Guarda el thread actualizado
6. Limpia los archivos de aprobación pendiente

**Output:**
```json
{
  "response": "Based on your approval, here's your spending analysis...",
  "session_id": "session_123",
  "approved": true,
  "timestamp": "2025-11-02T..."
}
```

## Archivos Involucrados

### Estructura de Archivos de Sesión:
```
contrai_chat_sessions/
├── {session_id}.json          # Thread de conversación completo
└── {session_id}_pending.json  # Datos de aprobación pendiente (temporal)
```

### `{session_id}.json` - Thread Serializado
Contiene el estado completo de la conversación que puede ser deserializado para continuar exactamente donde se quedó.

### `{session_id}_pending.json` - Datos de Aprobación
```json
{
  "user_input_requests": [
    {
      "function_name": "analyze_spending_patterns",
      "arguments": {"user_financial_data": "..."},
      "approval_id": "uuid-123"
    }
  ],
  "original_query": "Please analyze my spending patterns",
  "timestamp": "2025-11-02T..."
}
```

## Ventajas del Diseño

1. **Estado Consistente**: El thread se guarda en el momento exacto de la solicitud de aprobación
2. **Reanudación Perfecta**: Usa el patrón oficial del Agent Framework para continuar conversaciones
3. **Escalabilidad**: Soporta múltiples aprobaciones pendientes simultáneas
4. **Limpieza Automática**: Los archivos de aprobación pendiente se eliminan después del procesamiento
5. **Manejo de Errores**: Validación completa en cada paso

## Flujo de Frontend

1. **Envío inicial**: `POST /api/financial-chat-agent`
2. **Si `requires_approval === true`**: Mostrar UI de aprobación
3. **Respuesta del usuario**: `POST /api/financial-chat-agent/approval`
4. **Mostrar resultado final**

## Testing

Usa `test_approval_workflow.py` para probar el flujo completo:
```bash
python test_approval_workflow.py
```

## Consideraciones de Producción

1. **Timeouts**: Implementar expiración de aprobaciones pendientes
2. **Almacenamiento**: Migrar de archivos locales a base de datos
3. **Concurrencia**: Manejar múltiples usuarios simultáneos
4. **Seguridad**: Validar que el usuario tiene permisos para la sesión