import React, { useState, useRef, useEffect } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  FlatList,
  StyleSheet,
  KeyboardAvoidingView,
  Platform,
  SafeAreaView,
  StatusBar,
} from 'react-native';

const ChatScreen = () => {
  const [messages, setMessages] = useState([
    { id: '1', text: '¡Hola! Soy Ranukita, ¿en qué puedo ayudarte?', sender: 'bot' },
  ]);
  const [inputText, setInputText] = useState('');
  const flatListRef = useRef(null);

  const handleSend = () => {
    if (inputText.trim() === '') return;

    const userMessage = {
      id: Date.now().toString(),
      text: inputText.trim(),
      sender: 'user',
    };

    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setInputText('');

    // Simular respuesta del bot después de un breve retardo
    setTimeout(() => {
      const botMessage = {
        id: (Date.now() + 1).toString(),
        text: 'Gracias por tu mensaje. Estoy procesando tu solicitud...',
        sender: 'bot',
      };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    }, 1000);
  };

  useEffect(() => {
    if (flatListRef.current && messages.length > 0) {
      flatListRef.current.scrollToEnd({ animated: true });
    }
  }, [messages]);

  const renderMessage = ({ item }) => {
    const isUser = item.sender === 'user';
    return (
      <View style={[styles.messageContainer, isUser ? styles.userContainer : styles.botContainer]}>
        <View style={[styles.bubble, isUser ? styles.userBubble : styles.botBubble]}>
          <Text style={[styles.messageText, isUser ? styles.userText : styles.botText]}>
            {item.text}
          </Text>
        </View>
      </View>
    );
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="light-content" backgroundColor="#4A90D9" />
      <KeyboardAvoidingView
        style={styles.container}
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
        keyboardVerticalOffset={Platform.OS === 'ios' ? 90 : 0}
      >
        <View style={styles.header}>
          <Text style={styles.headerTitle}>Ranukita Chat</Text>
        </View>
        <FlatList
          ref={flatListRef}
          data={messages}
          renderItem={renderMessage}
          keyExtractor={(item) => item.id}
          style={styles.messageList}
          contentContainerStyle={styles.messageListContent}
          showsVerticalScrollIndicator={false}
        />
        <View style={styles.inputContainer}>
          <TextInput
            style={styles.input}
            placeholder="Escribe un mensaje..."
            placeholderTextColor="#999"
            value={inputText}
            onChangeText={setInputText}
            multiline
            maxLength={500}
          />
          <TouchableOpacity style={styles.sendButton} onPress={handleSend}>
            <Text style={styles.sendButtonText}>Enviar</Text>
          </TouchableOpacity>
        </View>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#4A90D9',
  },
  container: {
    flex: 1,
    backgroundColor: '#F5F5F5',
  },
  header: {
    backgroundColor: '#4A90D9',
    paddingVertical: 15,
    paddingHorizontal: 20,
    elevation: 4,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
  },
  headerTitle: {
    color: '#FFFFFF',
    fontSize: 20,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  messageList: {
    flex: 1,
    paddingHorizontal: 15,
  },
  messageListContent: {
    paddingVertical: 15,
  },
  messageContainer: {
    marginVertical: 5,
    flexDirection: 'row',
  },
  userContainer: {
    justifyContent: 'flex-end',
  },
  botContainer: {
    justifyContent: 'flex-start',
  },
  bubble: {
    maxWidth: '75%',
    paddingHorizontal: 15,
    paddingVertical: 10,
    borderRadius: 20,
    marginHorizontal: 5,
  },
  userBubble: {
    backgroundColor: '#4A90D9',
    borderBottomRightRadius: 5,
  },
  botBubble: {
    backgroundColor: '#E0E0E0',
    borderBottomLeftRadius: 5,
  },
  messageText: {
    fontSize: 16,
    lineHeight: 22,
  },
  userText: {
    color: '#FFFFFF',
  },
  botText: {
    color: '#333333',
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 10,
    paddingVertical: 8,
    backgroundColor: '#FFFFFF',
    borderTopWidth: 1,
    borderTopColor: '#DDD',
  },
  input: {
    flex: 1,
    backgroundColor: '#F0F0F0',
    borderRadius: 25,
    paddingHorizontal: 20,
    paddingVertical: 10,
    fontSize: 16,
    maxHeight: 100,
    color: '#333',
  },
  sendButton: {
    backgroundColor: '#4A90D9',
    borderRadius: 25,
    paddingHorizontal: 20,
    paddingVertical: 10,
    marginLeft: 10,
  },
  sendButtonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: '600',
  },
});

export default ChatScreen;