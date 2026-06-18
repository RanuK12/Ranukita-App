import { useEffect, useRef, useState } from 'react';

interface WebSocketMessage {
  type: string;
  payload: unknown;
}

export function useWebSocket(url: string) {
  const [isConnected, setIsConnected] = useState(false);
  const [lastMessage, setLastMessage] = useState<WebSocketMessage | null>(null);
  const wsRef = useRef<WebSocket | null>(null);
  const reconnectTimeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const maxReconnectAttempts = 5;
  const reconnectDelay = 3000;
  const reconnectAttemptsRef = useRef(0);

  const connect = () => {
    if (wsRef.current?.readyState === WebSocket.OPEN) return;

    wsRef.current = new WebSocket(url);

    wsRef.current.onopen = () => {
      setIsConnected(true);
      reconnectAttemptsRef.current = 0;
      console.log('WebSocket conectado');
    };

    wsRef.current.onclose = () => {
      setIsConnected(false);
      console.log('WebSocket desconectado');
      attemptReconnect();
    };

    wsRef.current.onerror = (error) => {
      console.error('WebSocket error:', error);
    };

    wsRef.current.onmessage = (event) => {
      try {
        const message: WebSocketMessage = JSON.parse(event.data);
        setLastMessage(message);
      } catch (err) {
        console.error('Error parsing WebSocket message:', err);
      }
    };
  };

  const attemptReconnect = () => {
    if (reconnectAttemptsRef.current >= maxReconnectAttempts) {
      console.log('Máximos intentos de reconexión alcanzados');
      return;
    }

    reconnectAttemptsRef.current += 1;
    console.log(`Intento de reconexión ${reconnectAttemptsRef.current}/${maxReconnectAttempts}`);

    reconnectTimeoutRef.current = setTimeout(() => {
      connect();
    }, reconnectDelay);
  };

  const sendMessage = (message: WebSocketMessage) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify(message));
    } else {
      console.warn('WebSocket no está conectado. No se puede enviar el mensaje.');
    }
  };

  const disconnect = () => {
    if (reconnectTimeoutRef.current) {
      clearTimeout(reconnectTimeoutRef.current);
      reconnectTimeoutRef.current = null;
    }
    reconnectAttemptsRef.current = maxReconnectAttempts; // Evitar reconexión automática
    wsRef.current?.close();
    wsRef.current = null;
  };

  useEffect(() => {
    connect();

    return () => {
      disconnect();
    };
  }, [url]);

  return {
    isConnected,
    lastMessage,
    sendMessage,
    disconnect,
    connect,
  };
}