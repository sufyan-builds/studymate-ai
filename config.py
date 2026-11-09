"""
Configuration file for StudyMate AI
Centralizes all settings, constants, and system prompts
"""

# ============================================================================
# API CONFIGURATION
# ============================================================================
DEFAULT_GROQ_MODEL = "mixtral-8x7b-32768"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 1024
REQUEST_TIMEOUT = 30

# ============================================================================
# UI CONFIGURATION
# ============================================================================
APP_TITLE = "StudyMate AI"
APP_ICON = "🧠"
APP_DESCRIPTION = "Your personal AI-powered study assistant"

# Page configuration
PAGES = {
    "Home": "🏠",
    "AI Chat": "💬",
    "Summarize Notes": "📄",
    "Explain Code": "💻",
    "Quiz Generator": "📝",
    "Rewrite Text": "✍️",
    "Settings": "⚙️",
    "About": "ℹ️",
}

# ============================================================================
# SYSTEM PROMPTS FOR DIFFERENT FEATURES
# ============================================================================
SYSTEM_PROMPTS = {
    "chat": """You are StudyMate AI, a friendly and intelligent study assistant.
Your role is to help students understand concepts, answer questions, and support their learning journey.
Provide clear, concise, and helpful explanations.
Use examples and analogies when helpful.""",
    
    "summarize": """You are an expert summarizer.
Analyze the provided text and create:
1. A brief 2-3 sentence summary
2. 3-5 key points in bullet format
3. 2-3 important concepts to remember

Format your response with clear headers.""",
    
    "explain": """You are a patient educator who explains complex concepts in simple language.
Break down the concept step-by-step.
Use everyday examples and analogies.
Avoid technical jargon when possible.
End with a real-world application.""",
    
    "code_explain": """You are an expert code reviewer and educator.
Analyze the provided code and explain:
1. What the code does (overview)
2. Step-by-step explanation of each part
3. Important concepts used
4. Potential improvements or suggestions

Be clear, structured, and beginner-friendly.""",
    
    "quiz": """You are a quiz master creating study questions.
Generate 5 multiple-choice questions (MCQs) based on the provided notes.
For each question provide:
- Question text
- 4 options (A, B, C, D)
- Correct answer
- Brief explanation

Format as JSON.""",
    
    "rewrite": """You are an expert writer.
Rewrite the provided text in the requested style without changing the core meaning.
Maintain the same information but adjust tone and complexity as requested.""",
}

# ============================================================================
# REWRITE STYLES
# ============================================================================
REWRITE_STYLES = {
    "Professional": "Make it formal, business-appropriate, and polished.",
    "Simple": "Use simple words and short sentences for easy understanding.",
    "Formal": "Use academic language and formal structure.",
    "Friendly": "Use conversational tone, friendly, and approachable.",
}

# ============================================================================
# SUPPORTED PROGRAMMING LANGUAGES
# ============================================================================
SUPPORTED_LANGUAGES = {
    "Python": "python",
    "JavaScript": "javascript",
    "Java": "java",
    "C++": "cpp",
    "SQL": "sql",
    "HTML/CSS": "html",
}

# ============================================================================
# UI/UX CONSTANTS
# ============================================================================
MAX_CHAT_MESSAGES = 50
MESSAGE_AVATAR_AI = "🤖"
MESSAGE_AVATAR_USER = "👤"
EMPTY_CHAT_PLACEHOLDER = "Start a conversation with your AI study assistant..."

# ============================================================================
# ERROR MESSAGES
# ============================================================================
ERRORS = {
    "no_api_key": "🔑 Groq API Key not found. Please add it in Settings.",
    "empty_input": "⚠️ Please enter some text before proceeding.",
    "api_error": "❌ API Error: Unable to connect to Groq. Check your API key and try again.",
    "timeout": "⏱️ Request timeout. The API took too long to respond.",
    "invalid_request": "❌ Invalid request. Please check your input and try again.",
}

# ============================================================================
# SUCCESS MESSAGES
# ============================================================================
SUCCESS_MESSAGES = {
    "copied": "✅ Copied to clipboard!",
    "generated": "✅ Generated successfully!",
    "settings_saved": "✅ Settings saved!",
}

# ============================================================================
# FEATURES METADATA
# ============================================================================
FEATURES = {
    "chat": {
        "title": "AI Chat",
        "icon": "💬",
        "description": "Ask any question and get instant AI responses",
        "color": "#0084FF",
    },
    "summarize": {
        "title": "Summarize Notes",
        "icon": "📄",
        "description": "Convert long notes into concise summaries",
        "color": "#34C759",
    },
    "explain": {
        "title": "Explain Text",
        "icon": "📚",
        "description": "Get simple explanations of difficult concepts",
        "color": "#FF9500",
    },
    "code": {
        "title": "Explain Code",
        "icon": "💻",
        "description": "Understand code step-by-step in any language",
        "color": "#5856D6",
    },
    "quiz": {
        "title": "Quiz Generator",
        "icon": "📝",
        "description": "Create practice MCQ questions from your notes",
        "color": "#FF3B30",
    },
    "rewrite": {
        "title": "Rewrite Text",
        "icon": "✍️",
        "description": "Rewrite text in different styles and tones",
        "color": "#1FB0F1",
    },
}

# ============================================================================
# HOME PAGE STATS
# ============================================================================
HOME_STATS = [
    {"label": "AI Powered", "value": "Groq API", "icon": "⚡"},
    {"label": "Response Time", "value": "Ultra-Fast", "icon": "⚙️"},
    {"label": "Features", "value": "6 Tools", "icon": "🎯"},
    {"label": "Theme", "value": "Dark & Light", "icon": "🎨"},
]
