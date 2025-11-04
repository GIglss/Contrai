import React, { useEffect, useRef, useState } from 'react';
import styles from './Chat.module.scss';

interface Message {
  id: string;
  content: string;
  role: 'user' | 'assistant' | 'approval' | 'system';
  timestamp: string;
  approvalData?: PendingApproval;
  isApprovalRequest?: boolean;
  approvalStatus?: 'pending' | 'approved' | 'denied' | 'processed';
}

interface PendingApproval {
  function_name: string;
  arguments: any;
  approval_id?: string;
  description?: string;
  risk_level?: 'low' | 'medium' | 'high';
}

interface ChatResponse {
  response: string;
  session_id: string;
  requires_approval?: boolean;
  pending_approvals?: PendingApproval[];
  timestamp: string;
  context_included: boolean;
  user_id: string;
}

interface ApprovalResponse {
  response: string;
  session_id: string;
  timestamp: string;
}

const EnhancedChat: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputMessage, setInputMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [sessionId, setSessionId] = useState<string>('012346');
  const [userId] = useState<string>('user_123'); // Replace with actual user ID from auth
  const [error, setError] = useState<string | null>(null);
  const [pendingApprovals, setPendingApprovals] = useState<PendingApproval[]>([]);
  const [contextEnabled, setContextEnabled] = useState(true);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  // Persist session and messages in sessionStorage
  const STORAGE_KEYS = {
    sessionId: 'contrai_chat_session_id_1',
    // sessionId: '12346',
    messages: 'contrai_chat_messages',
    contextEnabled: 'contrai_chat_context_enabled'
  };

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Load persisted data on component mount
  useEffect(() => {
    const initializeChat = async () => {
      try {
        // Load context setting
        const savedContextEnabled = sessionStorage.getItem(STORAGE_KEYS.contextEnabled);
        if (savedContextEnabled !== null) {
          setContextEnabled(JSON.parse(savedContextEnabled));
        }

        // Load session ID
        const savedSessionId = sessionStorage.getItem(STORAGE_KEYS.sessionId);
        let currentSessionId = savedSessionId || '012346'; // Default session ID
        console.log('🔍 Debug sessionId:', { savedSessionId, currentSessionId });
        setSessionId(currentSessionId);

        // Load messages from sessionStorage
        const savedMessages = sessionStorage.getItem(STORAGE_KEYS.messages);
        if (savedMessages) {
          const parsedMessages = JSON.parse(savedMessages);
          console.log('💾 Restored conversation from sessionStorage', currentSessionId);
          setMessages(parsedMessages);
          return; // Successfully restored from sessionStorage
        }

        // Show welcome message if no conversation found
        console.log('🎉 Starting new conversation');
        const welcomeMessage: Message = {
          id: 'welcome',
          content: `Bienvenido al Asistente Financiero Inteligente de Contrai.

🏦 **Capacidades Avanzadas:**
• Análisis integral de sus cuentas y transacciones
• Gestión inteligente de reglas de transferencia
• Recomendaciones financieras personalizadas  
• Proceso de aprobación para operaciones sensibles
• Memoria conversacional para seguimiento continuo

💼 **Servicios Disponibles:**
• "Analice mi situación financiera actual"
• "Revise mis patrones de gastos e ingresos"
• "Establezca una regla de ahorro automático"
• "Proporcione un resumen detallado de mis cuentas"

¿En qué puedo asistirle hoy?`,
          role: 'assistant',
          timestamp: new Date().toISOString()
        };
        setMessages([welcomeMessage]);

      } catch (error) {
        console.error('❌ Error initializing chat:', error);
        // Clear corrupted data and show welcome message
        sessionStorage.removeItem(STORAGE_KEYS.messages);
        const welcomeMessage: Message = {
          id: 'welcome-error',
          content: "Bienvenido al Asistente Financiero de Contrai. Se ha producido un error al recuperar la sesión anterior, pero el sistema está operativo y listo para asistirle. ¿En qué puedo ayudarle hoy?",
          role: 'assistant',
          timestamp: new Date().toISOString()
        };
        setMessages([welcomeMessage]);
      }
    };

    initializeChat();
  }, []); // Empty dependency array - run only on mount

  // Save messages to sessionStorage whenever they change
  useEffect(() => {
    if (messages.length > 0) {
      try {
        sessionStorage.setItem(STORAGE_KEYS.messages, JSON.stringify(messages));
      } catch (error) {
        console.error('Error saving messages to sessionStorage:', error);
      }
    }
  }, [messages]);

  // Save sessionId to sessionStorage whenever it changes
  useEffect(() => {
    if (sessionId) {
      try {
        sessionStorage.setItem(STORAGE_KEYS.sessionId, sessionId);
      } catch (error) {
        console.error('Error saving session ID to sessionStorage:', error);
      }
    }
  }, [sessionId]);

  // Save context setting to sessionStorage whenever it changes
  useEffect(() => {
    try {
      sessionStorage.setItem(STORAGE_KEYS.contextEnabled, JSON.stringify(contextEnabled));
    } catch (error) {
      console.error('Error saving context setting to sessionStorage:', error);
    }
  }, [contextEnabled]);

  const sendMessage = async () => {
    if (!inputMessage.trim() || isLoading) return;

    const userMessage: Message = {
      id: `user-${Date.now()}`,
      content: inputMessage,
      role: 'user',
      timestamp: new Date().toISOString()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputMessage('');
    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch('/api/financial-chat-agent', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: inputMessage,
          user_id: userId,
          session_id: sessionId,
          include_context: contextEnabled
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data: ChatResponse = await response.json();

      if (data.response) {
        const assistantMessage: Message = {
          id: `assistant-${Date.now()}`,
          content: data.response,
          role: 'assistant',
          timestamp: data.timestamp
        };

        setMessages(prev => [...prev, assistantMessage]);

        // Only update session ID if we don't have one yet (for new conversations)
        if (!sessionId || sessionId === '') {
          console.log('🆔 Setting new session ID:', data.session_id);
          setSessionId(data.session_id);
        } else {
          console.log('🔒 Keeping existing session ID:', sessionId, '(server wanted:', data.session_id, ')');
        }

        // Handle pending approvals - Create approval messages instead of separate UI
        if (data.requires_approval && data.pending_approvals) {
          setPendingApprovals(data.pending_approvals);

          // Create approval messages for each pending approval
          data.pending_approvals.forEach((approval, index) => {
            const approvalMessage: Message = {
              id: `approval-${Date.now()}-${index}`,
              content: getApprovalMessageContent(approval),
              role: 'approval',
              timestamp: new Date().toISOString(),
              approvalData: approval,
              isApprovalRequest: true,
              approvalStatus: 'pending'
            };
            setMessages(prev => [...prev, approvalMessage]);
          });
        }
      } else {
        throw new Error('No response received');
      }
    } catch (err) {
      console.error('Error sending message:', err);
      setError('Error en la comunicación con el asistente. Por favor, intente nuevamente.');

      const errorMessage: Message = {
        id: `error-${Date.now()}`,
        content: 'Se ha producido un error al procesar su solicitud. Por favor, inténtelo nuevamente o contacte al soporte técnico si el problema persiste.',
        role: 'assistant',
        timestamp: new Date().toISOString()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
      inputRef.current?.focus();
    }
  };

  const handleApproval = async (approval: PendingApproval, approved: boolean, messageId: string) => {
    setIsLoading(true);

    // Update the approval message status immediately for better UX
    setMessages(prev => prev.map(msg =>
      msg.id === messageId
        ? { ...msg, approvalStatus: approved ? 'approved' : 'denied' }
        : msg
    ));

    // Add system message about the decision
    const decisionMessage: Message = {
      id: `decision-${Date.now()}`,
      content: `${approved ? '✅' : '❌'} **${approved ? 'Aprobado' : 'Denegado'}**: ${getFunctionDisplayName(approval.function_name)}`,
      role: 'system',
      timestamp: new Date().toISOString()
    };
    setMessages(prev => [...prev, decisionMessage]);

    try {
      const response = await fetch('/api/financial-chat-agent/approval', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          session_id: sessionId,
          approval_id: approval.approval_id,
          approved: approved,
          user_id: userId,
          function_name: approval.function_name
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data: ApprovalResponse = await response.json();

      if (data.response) {
        const approvalResultMessage: Message = {
          id: `approval-result-${Date.now()}`,
          content: data.response,
          role: 'assistant',
          timestamp: data.timestamp
        };

        setMessages(prev => [...prev, approvalResultMessage]);

        // Remove this approval from pending list
        setPendingApprovals(prev => prev.filter(a => a.approval_id !== approval.approval_id));

        // Update the original approval message to processed
        setMessages(prev => prev.map(msg =>
          msg.id === messageId
            ? { ...msg, approvalStatus: 'processed' }
            : msg
        ));
      }
    } catch (err) {
      console.error('Error handling approval:', err);
      setError('Error al procesar la solicitud de aprobación.');

      // Revert the approval message status on error
      setMessages(prev => prev.map(msg =>
        msg.id === messageId
          ? { ...msg, approvalStatus: 'pending' }
          : msg
      ));
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const clearChat = () => {
    setMessages([]);
    setSessionId('');
    setPendingApprovals([]);
    setError(null);

    // Clear from sessionStorage
    try {
      sessionStorage.removeItem(STORAGE_KEYS.sessionId);
      sessionStorage.removeItem(STORAGE_KEYS.messages);
    } catch (error) {
      console.error('Error clearing sessionStorage:', error);
    }

    // Re-add welcome message
    const welcomeMessage: Message = {
      id: 'welcome-new',
      content: "� **Nueva Sesión Iniciada** \n\nSesión reiniciada exitosamente. El asistente está listo para proporcionarle servicios financieros. ¿Cómo puedo asistirle?",
      role: 'assistant',
      timestamp: new Date().toISOString()
    };
    setMessages([welcomeMessage]);
  };

  const formatMessage = (content: string) => {
    return content.split('\n').map((line, index) => (
      <React.Fragment key={index}>
        {line}
        {index < content.split('\n').length - 1 && <br />}
      </React.Fragment>
    ));
  };

  const formatFunctionArguments = (args: any) => {
    try {
      return JSON.stringify(args, null, 2);
    } catch {
      return String(args);
    }
  };

  const getApprovalMessageContent = (approval: PendingApproval) => {
    const riskEmoji = approval.risk_level === 'high' ? '🔴' :
      approval.risk_level === 'medium' ? '🟡' : '🟢';

    return `${riskEmoji} **Aprobación Requerida**

**Acción:** ${approval.function_name}
${approval.description ? `**Descripción:** ${approval.description}` : ''}

**Parámetros:**
\`\`\`
${formatFunctionArguments(approval.arguments)}
\`\`\`

Esta acción requiere tu aprobación antes de continuar. ¿Deseas proceder?`;
  };

  const getFunctionDisplayName = (functionName: string) => {
    const functionNames: { [key: string]: string } = {
      'create_transfer_rule': 'Crear Regla de Transferencia',
      'update_transfer_rule': 'Actualizar Regla de Transferencia',
      'delete_transfer_rule': 'Eliminar Regla de Transferencia',
      'execute_transfer': 'Ejecutar Transferencia',
      'get_account_balance': 'Consultar Saldo de Cuenta',
      'analyze_spending_patterns': 'Analizar Patrones de Gasto'
    };
    return functionNames[functionName] || functionName;
  };

  return (
    <div className={styles.chat}>
      <div className={styles.header}>
        <div>
          <h1 className={styles.title}>Asistente Financiero IA</h1>
          <p className={styles.subtitle}>
            Contrai Agent • Sesión: {sessionId ? `${sessionId.slice(-8)}` : 'Nueva'}
          </p>
        </div>
        <div className={styles.headerActions}>
          <label className={styles.contextToggle}>
            <input
              type="checkbox"
              checked={contextEnabled}
              onChange={(e) => setContextEnabled(e.target.checked)}
            />
          </label>
          <button
            className={styles.clearBtn}
            onClick={clearChat}
            title="Nueva sesión"
          >
            🔄 Nueva sesión
          </button>
        </div>
      </div>

      {error && (
        <div className={styles.error}>
          {error}
        </div>
      )}

      {/* Pending Approvals UI - Remove this section as approvals are now inline */}

      <div className={styles.messagesContainer}>
        <div className={styles.messages}>
          {messages.map((message) => (
            <div
              key={message.id}
              className={`${styles.message} ${styles[message.role]}`}
            >
              <div className={styles.messageContent}>
                {message.isApprovalRequest ? (
                  <div className={styles.approvalMessage}>
                    <div className={styles.approvalContent}>
                      {formatMessage(message.content)}
                    </div>
                    {message.approvalStatus === 'pending' && (
                      <div className={styles.approvalActions}>
                        <button
                          className={`${styles.approvalBtn} ${styles.approve}`}
                          onClick={() => handleApproval(message.approvalData!, true, message.id)}
                          disabled={isLoading}
                        >
                          ✅ Aprobar
                        </button>
                        <button
                          className={`${styles.approvalBtn} ${styles.deny}`}
                          onClick={() => handleApproval(message.approvalData!, false, message.id)}
                          disabled={isLoading}
                        >
                          ❌ Denegar
                        </button>
                      </div>
                    )}
                    {message.approvalStatus === 'approved' && (
                      <div className={styles.approvalStatus}>
                        <span className={styles.statusApproved}>✅ Aprobado - Procesando...</span>
                      </div>
                    )}
                    {message.approvalStatus === 'denied' && (
                      <div className={styles.approvalStatus}>
                        <span className={styles.statusDenied}>❌ Denegado</span>
                      </div>
                    )}
                    {message.approvalStatus === 'processed' && (
                      <div className={styles.approvalStatus}>
                        <span className={styles.statusProcessed}>✅ Completado</span>
                      </div>
                    )}
                  </div>
                ) : (
                  formatMessage(message.content)
                )}
              </div>
              <div className={styles.messageTime}>
                {new Date(message.timestamp).toLocaleTimeString('es-ES', {
                  hour: '2-digit',
                  minute: '2-digit'
                })}
              </div>
            </div>
          ))}

          {isLoading && (
            <div className={`${styles.message} ${styles.assistant}`}>
              <div className={styles.messageContent}>
                <div className={styles.typing}>
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
                {pendingApprovals.length > 0 ? 'Procesando aprobación...' : 'Analizando finanzas...'}
              </div>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>
      </div>

      <div className={styles.inputContainer}>
        <div className={styles.inputWrapper}>
          <input
            ref={inputRef}
            type="text"
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder={pendingApprovals.length > 0 ?
              "Por favor, responda a las solicitudes de aprobación pendientes..." :
              "Ingrese su consulta financiera... ej: 'analice mis cuentas'"
            }
            className={styles.messageInput}
            disabled={isLoading || (pendingApprovals.length > 0)}
            maxLength={500}
          />
          <button
            onClick={sendMessage}
            disabled={isLoading || !inputMessage.trim() || (pendingApprovals.length > 0)}
            className={styles.sendBtn}
          >
            {isLoading ? '⏳' : '🚀'}
          </button>
        </div>
        <div className={styles.inputHint}>
          Presione Enter para enviar • {contextEnabled ? '✅ Con' : '❌ Sin'} contexto financiero
          {pendingApprovals.length > 0 && ' • Responda las aprobaciones pendientes'}
        </div>
      </div>
    </div>
  );
};

EnhancedChat.displayName = "EnhancedChat";

export default EnhancedChat;