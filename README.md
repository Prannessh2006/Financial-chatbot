# 💰 AI Financial Advisor Chatbot

> An intelligent conversational AI financial advisor powered by Google's Gemini 1.5 Flash, built with Flask and Python

## 📖 Overview

This project is an AI-powered financial chatbot that provides personalized financial advice and guidance. Built using Google's Gemini 1.5 Flash language model, the chatbot offers concise, actionable financial advice in a user-friendly conversational interface. Whether you're looking for budgeting tips, investment advice, or savings strategies, this AI assistant is here to help.

## ✨ Features

### 🤖 AI-Powered Conversations
- Leverages **Google Gemini 1.5 Flash** for intelligent, context-aware responses
- Maintains conversation history for coherent, multi-turn dialogues
- Provides personalized financial advice based on your questions

### 💬 Smart Financial Guidance
- **Concise Responses**: Short, focused advice (max 2-3 sentences per point)
- **Structured Format**: Uses bullet points for clarity
- **Actionable Steps**: Always provides practical next steps
- **Easy to Understand**: Uses emojis and simple language for better comprehension
- **Topic Coverage**: Money (💵), investments (📊), savings (💰), credit (💳), and more

### 🎨 User-Friendly Interface
- Clean, modern web interface
- Real-time chat experience
- Responsive design that works on all devices
- Message history maintained throughout the session

### 🔒 Built-in Guardrails
- Professional and friendly tone
- No overly technical jargon
- Brief greetings and acknowledgments
- Focused on actionable advice

## 🗂️ Project Structure

```
Financial-chatbot/
│
├── app.py                   # Main Flask application with AI logic
├── index.html               # Frontend chat interface
├── Img.jpg                  # Project screenshot/image 1
├── Img2.jpg                 # Project screenshot/image 2
└── README.md                # Project documentation (this file)
```

### File Descriptions

- **`app.py`**: Core Flask application that handles:
  - Google Gemini AI integration
  - Chat session management
  - API endpoints for message processing
  - Environment variable configuration
  
- **`index.html`**: Frontend interface with:
  - Chat UI components
  - Real-time message display
  - User input handling
  - Responsive design

- **`Img.jpg` & `Img2.jpg`**: Application screenshots showcasing the chatbot interface

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- pip (Python package manager)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Prannessh2006/Financial-chatbot.git
   cd Financial-chatbot
   ```

2. **Install required packages**:
   ```bash
   pip install flask
   pip install python-dotenv
   pip install google-generativeai
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

4. **Get your Google Gemini API Key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in with your Google account
   - Create a new API key
   - Copy and paste it into your `.env` file

### Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Access the application**:
   - Open your web browser
   - Navigate to `http://localhost:5000`
   - Start chatting with your AI financial advisor!

## 💻 Usage Guide

### Asking Questions

1. Type your financial question in the chat input box
2. Press Enter or click Send
3. Wait for the AI to process and respond
4. Continue the conversation naturally

### Example Questions

- "How can I start saving money?"
- "What's the best way to invest as a beginner?"
- "How do I create a budget?"
- "Should I pay off debt or save first?"
- "How much should I have in an emergency fund?"
- "What are some passive income ideas?"

### Best Practices

- Be specific with your questions for better advice
- Provide context when relevant (e.g., age, income level, goals)
- Ask follow-up questions to dive deeper
- Remember: This is for educational purposes, not professional financial advice

## 🛠️ Technical Details

### Technologies Used

- **Backend Framework**: Flask (Python)
- **AI Model**: Google Gemini 1.5 Flash
- **Frontend**: HTML, CSS, JavaScript
- **Environment Management**: python-dotenv
- **API Integration**: google-generativeai

### Key Components

#### Flask Routes
- **`/`** (GET): Serves the main chat interface
- **`/chat`** (POST): Handles message processing and AI responses

#### AI Configuration
- **Model**: gemini-1.5-flash
- **Temperature**: Controlled for consistent, reliable responses
- **History Management**: Maintains conversation context
- **System Prompts**: Guides AI behavior and response style

#### Response Formatting
- Markdown cleanup for clean text
- JSON responses for easy frontend integration
- Error handling for API failures

## 📸 Screenshots

*See `Img.jpg` and `Img2.jpg` for application interface examples*

## 🔮 Future Enhancements

Potential features for future versions:

- 📈 **Financial Calculators**: Integrate mortgage, loan, and investment calculators
- 📊 **Data Visualization**: Charts for budget planning and investment tracking
- 💾 **Save Chat History**: Allow users to download or save conversations
- 👤 **User Profiles**: Personalized advice based on user preferences
- 🌍 **Multi-language Support**: Expand to serve users in different languages
- 📱 **Mobile App**: Native iOS and Android applications
- 🔔 **Financial Alerts**: Notifications for market updates and reminders
- 🤝 **Integration**: Connect with banking APIs for real-time data

## ⚠️ Disclaimer

**Important**: This chatbot provides general financial information and educational content only. It is NOT a substitute for professional financial advice. Always consult with a qualified financial advisor, accountant, or other professional before making significant financial decisions.

The AI's responses are generated based on general financial principles and may not be suitable for your specific situation.

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

### Areas for Contribution
- UI/UX improvements
- Additional financial advice categories
- Performance optimizations
- Testing and bug fixes
- Documentation enhancements

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Prannessh2006**
- GitHub: [@Prannessh2006](https://github.com/Prannessh2006)
- Project Link: [Financial-chatbot](https://github.com/Prannessh2006/Financial-chatbot)

## 🙏 Acknowledgments

- **Google Gemini**: For providing the powerful AI language model
- **Flask Community**: For the excellent web framework
- **Open Source Community**: For inspiration and resources

## 📞 Support & Contact

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Star the repository if you find it helpful!

## 🔗 Useful Resources

- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python dotenv Documentation](https://pypi.org/project/python-dotenv/)

---

**Made with ❤️ by Prannessh2006 | Powered by Google Gemini AI**

*Last Updated: November 2025*
