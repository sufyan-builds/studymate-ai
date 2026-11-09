# 🚀 StudyMate AI - Quick Start Guide

## ⚡ Get Running in 5 Minutes

### Step 1: Install Dependencies (1 min)
```bash
pip install -r requirements.txt
```

**What you're installing:**
- `streamlit` - Web app framework
- `groq` - AI API client
- `python-dotenv` - Environment variable loader

### Step 2: Get Your API Key (2 min)
1. Go to https://console.groq.com
2. Sign up with email (free!)
3. Copy your API key
4. Create a file named `.env` in the project folder
5. Add: `GROQ_API_KEY=your_key_here`

**Why?** Groq provides free API access with fast inference.

### Step 3: Run the App (1 min)
```bash
streamlit run app.py
```

Opens at: http://localhost:8501

### Step 4: Start Using (1 min)
- Visit Settings in sidebar
- Paste your API key (if not using .env)
- Choose any feature and start!

---

## 📂 What's Inside

### Core Files Explained

#### `app.py` (590 lines)
**The Main Engine**
- Orchestrates all pages and navigation
- Handles user interactions
- Integrates all modules
- Renders Streamlit UI

**Key Functions:**
- `page_home()` - Welcome screen
- `page_chat()` - AI chat interface
- `page_summarize()` - Notes summarizer
- `page_explain_code()` - Code explainer
- `page_quiz()` - Quiz generator
- `page_rewrite()` - Text rewriter

#### `ai.py` (280 lines)
**The Brain**
- `StudyMateAI` class - API client wrapper
- All communication with Groq
- Error handling and retry logic
- Specialized methods for each feature

**Key Methods:**
- `send_message()` - Core API call
- `generate_summary()` - Summarize text
- `explain_code()` - Explain code
- `generate_quiz()` - Create questions
- `rewrite_text()` - Rewrite in styles

#### `ui.py` (380 lines)
**The Designer**
- Custom CSS for premium look
- Reusable UI components
- Consistent styling across app
- Professional layouts

**Key Functions:**
- `apply_custom_css()` - Beautiful styling
- `render_header()` - Titles
- `render_chat_message()` - Chat bubbles
- `render_metric_cards()` - Statistics

#### `utils.py` (240 lines)
**The Helper**
- Parsing and formatting
- Session state management
- JSON processing
- Token estimation

**Key Functions:**
- `safe_json_parse()` - Safe JSON parsing
- `initialize_session_state()` - Setup
- `add_to_chat_history()` - Chat management
- `update_statistics()` - Track usage

#### `config.py` (180 lines)
**The Configuration**
- All constants in one place
- System prompts for each feature
- UI metadata
- Error messages
- Settings definitions

**Why?** Easy to modify without touching other code

---

## 🎓 What You're Learning

### Python Concepts ✅

1. **Object-Oriented Programming**
   - Classes: `StudyMateAI`
   - Methods and attributes
   - Encapsulation

2. **Functions & Modularization**
   - Reusable components
   - Type hints: `def func(x: str) -> str:`
   - Docstrings

3. **Error Handling**
   - Try/except blocks
   - Custom error messages
   - Graceful degradation

4. **Data Structures**
   - Lists: Chat history
   - Dictionaries: Configuration
   - JSON: API responses

5. **String Processing**
   - f-strings: `f"{variable}"`
   - Regular expressions
   - Markdown formatting

### Streamlit Concepts ✅

1. **Session State**
   - Persistent data across reruns
   - `st.session_state`

2. **Layouts**
   - Columns: `st.columns()`
   - Containers: `st.container()`
   - Sidebar: `st.sidebar`

3. **Interactive Elements**
   - Buttons with callbacks
   - Text inputs
   - Radio buttons
   - Sliders

4. **Styling**
   - Custom CSS
   - Markdown support
   - HTML rendering

5. **Component Composition**
   - Building reusable functions
   - Page-based routing
   - State management

### AI/API Concepts ✅

1. **API Integration**
   - REST API calls
   - Error handling
   - Request/response cycles

2. **Prompt Engineering**
   - System prompts guide behavior
   - Different prompts for different tasks
   - Temperature control (creativity)

3. **Token Management**
   - Tokens ≈ 4 characters
   - Max tokens = response length limit
   - Cost estimation

4. **JSON Processing**
   - Parsing API responses
   - Handling malformed JSON
   - Data validation

---

## 🎯 Key Features Breakdown

### Feature 1: AI Chat 💬
**What it does:**
- Simple Q&A with AI
- Maintains conversation history
- Natural language understanding

**Python Concepts:**
- Session state for messages
- List management
- String concatenation

**API Concepts:**
- Conversation context
- Message roles (user/assistant)
- System prompts

### Feature 2: Summarize Notes 📄
**What it does:**
- Condenses long text
- Extracts key points
- Identifies concepts

**Python Concepts:**
- Text parsing
- String splitting
- Data structuring

**Prompt Engineering:**
- Structured output request
- Section identification
- Format specification

### Feature 3: Code Explainer 💻
**What it does:**
- Explains code step-by-step
- Supports multiple languages
- Identifies patterns

**Python Concepts:**
- Language selection logic
- Code formatting
- Technical explanation generation

**Educational Value:**
- Understanding algorithms
- Learning best practices
- Code review skills

### Feature 4: Quiz Generator 📝
**What it does:**
- Creates MCQ from notes
- Generates explanations
- JSON output

**Python Concepts:**
- JSON parsing
- Data validation
- Error recovery

**Assessment Value:**
- Self-testing
- Learning verification
- Exam preparation

### Feature 5: Text Rewriter ✍️
**What it does:**
- Changes writing style
- Maintains meaning
- Improves clarity

**Python Concepts:**
- Dictionary lookup
- Conditional styling
- Side-by-side comparison

**Writing Skills:**
- Audience adaptation
- Tone adjustment
- Clarity improvement

---

## 🔧 How to Extend This Project

### Add a New Feature

**Step 1: Create function in `ai.py`**
```python
def new_feature(self, text: str) -> Optional[str]:
    system_prompt = "Your instructions here"
    return self.send_message(text, system_prompt)
```

**Step 2: Create page function in `app.py`**
```python
def page_new_feature():
    render_header("Feature Name", "Description", "🎯")
    # Your UI here
```

**Step 3: Add to navigation in `config.py`**
```python
PAGES = {
    ...
    "New Feature": "🎯",
}
```

**Step 4: Add to routing in `app.py`**
```python
pages = {
    ...
    'New Feature': page_new_feature,
}
```

### Modify System Prompts

Edit `config.py` > `SYSTEM_PROMPTS`:
```python
SYSTEM_PROMPTS = {
    "chat": "Your new system prompt here",
    ...
}
```

### Change UI Theme

Edit CSS in `ui.py`:
```python
:root {
    --primary-color: #your-color;
    --secondary-color: #your-color;
}
```

---

## 🚀 Deployment Tips

### Local Development ✅
```bash
streamlit run app.py
```

### Testing
```bash
# Test with fake API responses
# Modify ai.py to print requests before sending
```

### Production Deployment
1. **Streamlit Cloud** (easiest)
   - Push to GitHub
   - Connect to Streamlit Cloud
   - Auto-deploys on push

2. **Docker**
   ```bash
   docker build -t studymate .
   docker run -p 8501:8501 studymate
   ```

3. **Environment Variables**
   - Use Streamlit Secrets management
   - Set `GROQ_API_KEY` in secrets
   - Never commit `.env` to git

---

## 🎓 Interview Preparation

### Questions You Might Get

**"Tell me about your project structure"**
- Answer: Modular design with separate concerns
- Explain each file's responsibility
- Mention DRY principle

**"How does the API integration work?"**
- Answer: StudyMateAI class manages all API calls
- Show error handling
- Explain retry logic

**"How would you add feature X?"**
- Answer: Show how you extended it before
- Walk through the 4 steps above
- Demonstrate code modification

**"What Python concepts are used?"**
- Answer: Classes, type hints, error handling, sessions state
- Provide specific examples from code

**"How do you handle errors?"**
- Answer: Try/except blocks, user-friendly messages
- Show specific error handling examples

---

## 📊 Performance Insights

### Response Speed
- **Groq Mixtral**: ~1-3 seconds typically
- **Network**: Varies by location
- **Model**: Mixtral 8x7B is optimized for speed

### Token Usage
- **Chat**: 100-500 tokens per message
- **Summarize**: 200-1000 tokens
- **Code Explain**: 300-800 tokens
- **Quiz**: 400-1200 tokens (includes JSON)

### Cost (Free Tier)
- Groq offers free API access
- Great for learning and portfolios
- No credit card required

---

## 🐛 Troubleshooting

### App Won't Start
```bash
# Check Python version
python --version  # Should be 3.8+

# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Clear Streamlit cache
rm -rf ~/.streamlit
```

### API Errors
- Check API key in console.groq.com
- Verify internet connection
- Check rate limits
- Try in Settings: increase temperature

### Styling Issues
- Clear browser cache (Ctrl+Shift+Del)
- Hard refresh (Ctrl+Shift+R)
- Check CSS syntax in `ui.py`

---

## 📚 Next Steps

1. **Run the app** - Test all features
2. **Read the code** - Understand each component
3. **Modify settings** - Play with temperature/tokens
4. **Add a feature** - Extend the project
5. **Deploy** - Share with others
6. **Interview** - Confidently explain everything

---

**You built this! You understand it! You can explain it! 🎉**

Good luck with your internship applications! 🚀
