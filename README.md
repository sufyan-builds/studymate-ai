# 🧠 StudyMate AI - Your Personal AI Study Assistant

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Groq API](https://img.shields.io/badge/Groq-API-green.svg)](https://groq.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> An AI-powered study assistant application that helps students learn faster, smarter, and better with beautiful UI and powerful features.

## 📋 Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Screenshots](#screenshots)
- [Key Concepts](#key-concepts)
- [Future Improvements](#future-improvements)
- [Learning Resources](#learning-resources)

## ✨ Features

StudyMate AI comes with 6 powerful study tools:

### 🤖 **AI Chat**
- Ask any question about your studies
- Get intelligent, contextual responses
- Maintains conversation history for context
- Perfect for clarifying concepts

### 📄 **Summarize Notes**
- Paste long notes or articles
- Get concise summaries automatically
- Extract key points and concepts
- Save time on reading

### 💻 **Explain Code**
- Paste code in any supported language
- Get step-by-step explanations
- Learn about algorithms and patterns
- Supports: Python, JavaScript, Java, C++, SQL

### 📝 **Quiz Generator**
- Create practice MCQs from notes
- Test your knowledge
- Get detailed explanations
- Prepare for exams

### ✍️ **Rewrite Text**
- Change writing style instantly
- Options: Professional, Simple, Formal, Friendly
- Improve your academic writing
- Perfect for assignments

### ⚙️ **Smart Settings**
- Customize Groq API settings
- Adjust temperature for creativity
- Control response length
- Dark/Light theme toggle

## 🛠️ Technology Stack

### Core Technologies
- **Python 3.8+** - Programming language
- **Streamlit** - Web app framework
- **Groq API** - AI model inference

### Key Libraries
- `groq` - Groq Python SDK
- `streamlit` - Web UI framework
- `python-dotenv` - Environment variable management

### Architecture Principles
- **Modular Design** - Separate concerns into different files
- **DRY (Don't Repeat Yourself)** - Reusable components
- **Object-Oriented Programming** - Classes for AI client
- **Clean Code** - Type hints, docstrings, comments
- **Error Handling** - Graceful failure with user-friendly messages

## 📁 Project Structure

```
studymate-ai/
│
├── app.py              # Main Streamlit application
├── ai.py               # Groq API integration and AI logic
├── ui.py               # Reusable UI components and styling
├── utils.py            # Helper functions and utilities
├── config.py           # Configuration, constants, prompts
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (API keys)
├── .gitignore         # Git ignore file
└── README.md          # This file
```

### File Responsibilities

| File | Purpose |
|------|---------|
| `app.py` | Streamlit UI orchestration and page routing |
| `ai.py` | Groq API client and AI operations |
| `ui.py` | Reusable UI components and CSS styling |
| `utils.py` | Helper functions (parsing, formatting, validation) |
| `config.py` | Constants, prompts, settings, metadata |

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Groq API key (free from [console.groq.com](https://console.groq.com))

### Step 1: Clone or Download
```bash
git clone https://github.com/yourusername/studymate-ai.git
cd studymate-ai
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_api_key_here
```

Or add it through the app's Settings sidebar.

### Step 5: Run the Application
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📖 Usage

### First Time Setup
1. Get your free Groq API key from [console.groq.com](https://console.groq.com)
2. Open the app and click Settings in the sidebar
3. Enter your API key
4. Adjust temperature and max tokens as needed

### Using Each Feature

**AI Chat**
- Simply type your question
- Press Send or Enter
- Continue the conversation

**Summarize Notes**
- Copy and paste your notes
- Click "Generate Summary"
- Review summary, key points, and concepts

**Explain Code**
- Select the programming language
- Paste your code
- Click "Explain Code"
- Get step-by-step breakdown

**Quiz Generator**
- Paste study material
- Click "Generate Quiz"
- Review questions and answers

**Rewrite Text**
- Choose your desired style
- Paste text
- Click "Rewrite"
- Compare original and rewritten versions

## 🧠 How It Works

### Architecture Overview

```
┌─────────────────────────────────────────────────┐
│            Streamlit Web UI (app.py)            │
│  ┌─────────────────────────────────────────┐   │
│  │  Home │ Chat │ Summarize │ Code │ Quiz │   │
│  └─────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────┐
│           UI Components (ui.py)                 │
│  • Custom CSS styling                           │
│  • Reusable component functions                │
│  • Professional layout system                  │
└─────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────┐
│        AI Logic & API Client (ai.py)            │
│  • Groq API Integration                        │
│  • Message formatting                          │
│  • Error handling                              │
└─────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────┐
│        Groq API (Cloud)                         │
│  • Mixtral 8x7B Model                          │
│  • Fast inference                              │
│  • Streaming responses                         │
└─────────────────────────────────────────────────┘
```

### Data Flow Example: Chat

```
User Input
    ↓
Session State (chat_messages)
    ↓
AI Client (StudyMateAI class)
    ↓
Groq API (mixtral-8x7b-32768)
    ↓
Response Processing
    ↓
Add to Chat History
    ↓
Render Message
    ↓
Display to User
```

### Key Python Concepts

1. **Classes & OOP** - `StudyMateAI` class encapsulates API logic
2. **Type Hints** - Functions specify parameter and return types
3. **Exception Handling** - Try/except blocks for robust error handling
4. **Session State** - Streamlit's st.session_state for data persistence
5. **Decorators** - Python functions as callbacks
6. **String Formatting** - f-strings for clean code
7. **JSON Processing** - Parsing API responses
8. **Functions** - Modular, reusable code blocks

## 📸 Screenshots

### Home Page
- Welcome message
- Feature cards grid
- Quick statistics
- Getting started guide

### Chat Interface
- Message history display
- Real-time responses
- Clear chat button
- Copy functionality

### Note Summarizer
- Large text input area
- Structured output (Summary, Key Points, Concepts)
- Copy button for results
- Word count indicator

### Code Explainer
- Language selector dropdown
- Code input area
- Step-by-step explanations
- Important concepts highlighted

### Quiz Generator
- Notes input
- Generated MCQs with options
- Expandable answer sections
- Explanation for each answer

### Text Rewriter
- Style selector (4 options)
- Side-by-side comparison
- Original vs rewritten text
- Copy button for result

## 🎓 Key Concepts Explained

### Prompt Engineering
Different features use tailored system prompts to guide AI behavior:
- Chat: General assistant tone
- Summarize: Structured summary format
- Code Explain: Step-by-step breakdown
- Quiz: JSON output format

### Temperature Setting
- **Low (0.0-0.3)**: Factual, consistent responses
- **Medium (0.5-0.7)**: Balanced (default)
- **High (0.8-1.0)**: Creative, varied responses

### Token Management
- **Tokens**: Units of text (approximately 4 characters = 1 token)
- **Max Tokens**: Limits response length and costs
- **Estimate**: User input tokens affect available output tokens

### Session State vs Environment
- **Session State**: Data within current browser session (resets on refresh)
- **Environment Variables**: Persistent, for deployment
- **API Key**: Can be set either way for convenience and security

## 🔒 Security Considerations

1. **API Keys**: Never commit `.env` file to git
2. **Password Fields**: API key uses `type="password"` for obscuring input
3. **Input Validation**: All inputs are validated before API calls
4. **Error Handling**: API errors don't expose sensitive information
5. **HTTPS**: Use HTTPS when deploying to production

## 🚀 Future Improvements

### Phase 2 Features
- [ ] Chat conversation export (PDF/TXT)
- [ ] User accounts and saved history
- [ ] Multiple language support
- [ ] Dark mode theme variations
- [ ] Voice input support
- [ ] Study streak tracking
- [ ] Performance analytics

### Performance Optimizations
- [ ] Response caching
- [ ] Streaming responses
- [ ] Pagination for long outputs
- [ ] Lazy loading for images

### Code Quality
- [ ] Unit tests
- [ ] Integration tests
- [ ] Type checking with mypy
- [ ] Code coverage reports

### Deployment
- [ ] Docker containerization
- [ ] GitHub Actions CI/CD
- [ ] Streamlit Cloud deployment
- [ ] Production configuration

## 📚 Learning Resources

### For Understanding This Project

**Python Concepts**
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Exception Handling](https://docs.python.org/3/tutorial/errors.html)
- [Classes and OOP](https://docs.python.org/3/tutorial/classes.html)
- [List Comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

**Streamlit Documentation**
- [Streamlit Basics](https://docs.streamlit.io/library/get-started)
- [Session State](https://docs.streamlit.io/library/api-reference/session-state)
- [Layouts & Containers](https://docs.streamlit.io/library/api-reference/layout)
- [Custom CSS](https://docs.streamlit.io/library/api-reference/text/markdown)

**API Integration**
- [Groq API Documentation](https://console.groq.com/docs)
- [REST API Basics](https://restfulapi.net/)
- [JSON Processing in Python](https://docs.python.org/3/library/json.html)

**Prompt Engineering**
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Prompt Design Patterns](https://learnprompting.org/)
- [System Prompts Best Practices](https://help.openai.com/en/articles/7042661-how-can-i-use-the-system-parameter)

### Portfolio & Interview Tips

1. **Explain Architecture**: Be ready to explain file structure and design decisions
2. **Demonstrate Features**: Show all 6 tools and explain how each uses AI
3. **Code Quality**: Point out error handling, type hints, and modular design
4. **Performance**: Discuss API optimization and response handling
5. **UI/UX**: Explain custom CSS and design choices
6. **Scalability**: How would you add new features or languages?

## 🤝 Contributing

This is a personal portfolio project. If you fork it, consider:
- Adding your own features in separate branches
- Improving documentation
- Adding tests
- Optimizing performance

## 📄 License

This project is open source and available under the MIT License. See `LICENSE` file for details.

## 💬 Questions & Support

### Common Issues

**API Key Error**
- Verify key from [console.groq.com](https://console.groq.com)
- Check for trailing spaces
- Ensure key is valid and active

**Empty Response**
- Check temperature and max_tokens settings
- Try a clearer, more specific input
- Verify internet connection

**Slow Response**
- Groq API is usually fast
- Check internet connection
- Reduce max_tokens for faster response

### For Interview Preparation

- Practice explaining each component
- Be ready to modify features on the fly
- Discuss design decisions
- Show understanding of Python and Streamlit concepts

## 🎯 Project Goals Achieved

✅ **Python** - Clean, well-documented code with type hints
✅ **Streamlit** - Professional UI with custom CSS
✅ **API Integration** - Robust Groq API integration
✅ **Error Handling** - Graceful error management
✅ **UI/UX** - Modern, beautiful interface inspired by ChatGPT
✅ **Modular Design** - Separate concerns into dedicated files
✅ **Documentation** - Comprehensive README and code comments
✅ **Portfolio Ready** - Interview-friendly complexity level

---

**Made with ❤️ for students who want to learn smarter**

Happy studying! 🚀
