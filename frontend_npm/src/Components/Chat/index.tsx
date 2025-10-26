import React, { useState, useRef, useEffect } from 'react';
import styles from './Chat.module.scss';

interface Message {
  id: string;
  content: string;
  role: 'user' | 'assistant';
  timestamp: string;
}

interface ChatResponse {
  response: string;
  conversation_id: string;
  usage: {
    prompt_tokens: number;
    completion_tokens: number;
    total_tokens: number;
  };
  timestamp: string;
  context_included: boolean;
}

const Chat: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputMessage, setInputMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [conversationId, setConversationId] = useState<string>('');
  const [error, setError] = useState<string | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    // Add welcome message
    const welcomeMessage: Message = {
      id: 'welcome',
      content: "¡Hola! Soy tu asistente financiero personal. Puedo ayudarte a:\n\n• Analizar tus cuentas y balances\n• Revisar tus reglas de transferencia\n• Sugerir mejoras en tu planificación financiera\n• Responder preguntas sobre tus finanzas\n\n¿En qué puedo ayudarte hoy?",
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
      const response = await fetch('/api/financial-chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: inputMessage,
          conversation_id: conversationId,
          include_context: true
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
        setConversationId(data.conversation_id);
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

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const clearChat = () => {
    setMessages([]);
    setConversationId('');
    setError(null);
    // Re-add welcome message
    const welcomeMessage: Message = {
      id: 'welcome-new',
      content: "Chat reiniciado. ¿En qué puedo ayudarte?",
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

  return (
    <div className={styles.chat}>
      <div className={styles.header}>
        <div>
          <h1 className={styles.title}>Asistente Financiero</h1>
          <p className={styles.subtitle}>Pregúntame sobre tus finanzas</p>
        </div>
        <button 
          className={styles.clearBtn}
          onClick={clearChat}
          title="Nuevo chat"
        >
          🗑️ Limpiar
        </button>
      </div>

      {error && (
        <div className={styles.error}>
          {error}
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
                Pensando...
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
            placeholder="Pregúntame sobre tus finanzas..."
            className={styles.messageInput}
            disabled={isLoading}
            maxLength={500}
          />
          <button
            onClick={sendMessage}
            disabled={isLoading || !inputMessage.trim()}
            className={styles.sendBtn}
          >
            {isLoading ? '⏳' : '📤'}
          </button>
        </div>
        <div className={styles.inputHint}>
          Presiona Enter para enviar • Shift+Enter para nueva línea
        </div>
      </div>
    </div>
  );
};

Chat.displayName = "Chat";

export default Chat;