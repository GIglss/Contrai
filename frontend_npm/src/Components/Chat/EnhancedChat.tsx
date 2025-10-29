import React, { useState, useRef, useEffect } from 'react';
import styles from './Chat.module.scss';

interface Message {
  id: string;
  content: string;
  role: 'user' | 'assistant';
  timestamp: string;
}

interface PendingApproval {
  function_name: string;
  arguments: any;
  approval_id: string;
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
  const [sessionId, setSessionId] = useState<string>('');
  const [userId] = useState<string>('user_123'); // Replace with actual user ID from auth
  const [error, setError] = useState<string | null>(null);
  const [pendingApprovals, setPendingApprovals] = useState<PendingApproval[]>([]);
  const [contextEnabled, setContextEnabled] = useState(true);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    // Add enhanced welcome message
    const welcomeMessage: Message = {
      id: 'welcome',
      content: `¡Hola! Soy tu asistente financiero inteligente de Contrai. 

🤖 **Nuevas capacidades mejoradas:**
• Recuerdo nuestras conversaciones anteriores
• Analizo tus cuentas y reglas de transferencia en tiempo real  
• Puedo sugerir mejoras financieras personalizadas
• Solicito aprobación para acciones sensibles

💬 **Puedes preguntarme:**
• "¿Cómo están mis finanzas?"
• "Analiza mis patrones de gasto"
• "Sugiere una regla de ahorro del 20%"
• "Muestra un resumen de mis cuentas"

¿En qué puedo ayudarte hoy?`,
      role: 'assistant',
      timestamp: new Date().toISOString()
    };
    setMessages([welcomeMessage]);
  }, []);

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
        setSessionId(data.session_id);

        // Handle pending approvals
        if (data.requires_approval && data.pending_approvals) {
          setPendingApprovals(data.pending_approvals);
        }
      } else {
        throw new Error('No response received');
      }
    } catch (err) {
      console.error('Error sending message:', err);
      setError('Error al comunicarse con el asistente. Intenta nuevamente.');
      
      const errorMessage: Message = {
        id: `error-${Date.now()}`,
        content: 'Lo siento, hubo un error al procesar tu mensaje. Por favor intenta nuevamente.',
        role: 'assistant',
        timestamp: new Date().toISOString()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
      inputRef.current?.focus();
    }
  };

  const handleApproval = async (approval: PendingApproval, approved: boolean) => {
    setIsLoading(true);
    
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
          user_id: userId
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data: ApprovalResponse = await response.json();

      if (data.response) {
        const approvalMessage: Message = {
          id: `approval-${Date.now()}`,
          content: data.response,
          role: 'assistant',
          timestamp: data.timestamp
        };

        setMessages(prev => [...prev, approvalMessage]);
        setPendingApprovals([]); // Clear pending approvals
      }
    } catch (err) {
      console.error('Error handling approval:', err);
      setError('Error al procesar la aprobación.');
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
    
    // Re-add welcome message
    const welcomeMessage: Message = {
      id: 'welcome-new',
      content: "Chat reiniciado. Nueva sesión iniciada. ¿En qué puedo ayudarte?",
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
            <span>Contexto financiero</span>
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

      {/* Pending Approvals UI */}
      {pendingApprovals.length > 0 && (
        <div className={styles.approvalsContainer}>
          <div className={styles.approvalsHeader}>
            <span>⚠️ Aprobación requerida</span>
          </div>
          {pendingApprovals.map((approval, index) => (
            <div key={index} className={styles.approvalCard}>
              <div className={styles.approvalInfo}>
                <h4>🔧 {approval.function_name}</h4>
                <details className={styles.approvalDetails}>
                  <summary>Ver parámetros</summary>
                  <pre className={styles.approvalArgs}>
                    {formatFunctionArguments(approval.arguments)}
                  </pre>
                </details>
              </div>
              <div className={styles.approvalActions}>
                <button
                  className={`${styles.approvalBtn} ${styles.approve}`}
                  onClick={() => handleApproval(approval, true)}
                  disabled={isLoading}
                >
                  ✅ Aprobar
                </button>
                <button
                  className={`${styles.approvalBtn} ${styles.deny}`}
                  onClick={() => handleApproval(approval, false)}
                  disabled={isLoading}
                >
                  ❌ Denegar
                </button>
              </div>
            </div>
          ))}
        </div>
      )}

      <div className={styles.messagesContainer}>
        <div className={styles.messages}>
          {messages.map((message) => (
            <div
              key={message.id}
              className={`${styles.message} ${styles[message.role]}`}
            >
              <div className={styles.messageContent}>
                {formatMessage(message.content)}
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
            placeholder="Pregunta sobre tus finanzas... ej: 'analiza mis cuentas'"
            className={styles.messageInput}
            disabled={isLoading || pendingApprovals.length > 0}
            maxLength={500}
          />
          <button
            onClick={sendMessage}
            disabled={isLoading || !inputMessage.trim() || pendingApprovals.length > 0}
            className={styles.sendBtn}
          >
            {isLoading ? '⏳' : '🚀'}
          </button>
        </div>
        <div className={styles.inputHint}>
          Enter para enviar • {contextEnabled ? '✅ Con' : '❌ Sin'} contexto financiero
          {pendingApprovals.length > 0 && ' • Responde las aprobaciones primero'}
        </div>
      </div>
    </div>
  );
};

EnhancedChat.displayName = "EnhancedChat";

export default EnhancedChat;