import { useState } from 'react'
import './App.css'

// Define the shape of a message
interface Message {
  role: 'user' | 'assistant'
  content: string
}

function App() {
  // State to store all messages in the chat
  const [messages, setMessages] = useState<Message[]>([])
  // State to store the current input text
  const [input, setInput] = useState('')
  // State to track if we're waiting for a response
  const [isLoading, setIsLoading] = useState(false)

  const sendMessage = async () => {
    if (!input.trim()) return // Don't send empty messages

    // Add user message to chat
    const userMessage: Message = { role: 'user', content: input }
    setMessages(prev => [...prev, userMessage])
    setInput('') // Clear input field
    setIsLoading(true)

    try {
      // Call our Python backend
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: input }),
      })

      if (!response.ok) {
        throw new Error('Failed to get response')
      }

      const data = await response.json()
      
      // Add AI response to chat
      const assistantMessage: Message = { 
        role: 'assistant', 
        content: data.response 
      }
      setMessages(prev => [...prev, assistantMessage])
    } catch (error) {
      console.error('Error:', error)
      // Show error message in chat
      const errorMessage: Message = {
        role: 'assistant',
        content: 'Sorry, I couldn\'t connect to the server. Make sure the backend is running on port 8000.'
      }
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }

  // Handle Enter key press
  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      sendMessage()
    }
  }

  return (
    <div className="app">
      <div className="chat-container">
        <header className="chat-header">
          <h1>🏠 California Tenant Rights Assistant</h1>
          <p>Ask me about your tenant rights in California</p>
        </header>

        <div className="messages">
          {messages.length === 0 ? (
            <div className="welcome-message">
              <h2>Welcome! 👋</h2>
              <p>I can help you understand your rights as a California tenant.</p>
              <div className="example-questions">
                <strong>Try asking:</strong>
                <ul>
                  <li>"What are my rights if my unit is unsafe?"</li>
                  <li>"How much notice does a landlord need to give before eviction?"</li>
                  <li>"Can my landlord enter my apartment without permission?"</li>
                  <li>"What can I do about a security deposit dispute?"</li>
                </ul>
              </div>
            </div>
          ) : (
            messages.map((msg, index) => (
              <div key={index} className={`message ${msg.role}`}>
                <div className="message-content">
                  <strong>{msg.role === 'user' ? 'You' : 'Assistant'}:</strong>
                  <p>{msg.content}</p>
                </div>
              </div>
            ))
          )}
          {isLoading && (
            <div className="message assistant loading">
              <div className="message-content">
                <strong>Assistant:</strong>
                <p>Thinking...</p>
              </div>
            </div>
          )}
        </div>

        <div className="input-container">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Ask about your tenant rights..."
            disabled={isLoading}
          />
          <button 
            onClick={sendMessage} 
            disabled={isLoading || !input.trim()}
          >
            Send
          </button>
        </div>
      </div>
    </div>
  )
}

export default App
