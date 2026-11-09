"""
StudyMate AI - Main Application
AI-Powered Study Assistant using Streamlit and Groq API
"""

import streamlit as st
from config import *
from ai import get_ai_client
from ui import *
from utils import *
import json

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom styling
apply_custom_css()

# Initialize session state
initialize_session_state()

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================
def render_sidebar():
    """
    Render professional sidebar with navigation.
    
    Streamlit Concepts:
    - st.sidebar for sidebar elements
    - Radio buttons for navigation
    - Session state for page tracking
    
    Why sidebar?
    - Standard UX pattern from ChatGPT, Claude, Notion
    - Easy navigation between features
    - Professional appearance
    """
    with st.sidebar:
        # Header
        st.markdown(f"# {APP_ICON} {APP_TITLE}")
        st.markdown("AI-Powered Study Assistant")
        st.divider()
        
        # Navigation
        st.markdown("### Navigation")
        
        pages_list = list(PAGES.keys())
        current_index = pages_list.index(st.session_state.get('current_page', 'Home'))
        
        selected_page = st.radio(
            "Choose a feature:",
            pages_list,
            index=current_index,
            label_visibility="collapsed"
        )
        
        if selected_page != st.session_state.get('current_page'):
            st.session_state.current_page = selected_page
            st.rerun()
        
        st.divider()
        
        # Settings Section
        st.markdown("### Settings")
        
        api_key_input = st.text_input(
            "🔑 Groq API Key",
            type="password",
            value=st.session_state.get('api_key', ''),
            help="Get your free API key from console.groq.com"
        )
        
        if api_key_input != st.session_state.get('api_key'):
            st.session_state.api_key = api_key_input
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.session_state.temperature = st.slider(
                "Temperature",
                min_value=0.0,
                max_value=1.0,
                value=st.session_state.get('temperature', 0.7),
                step=0.1,
                help="Higher = more creative, Lower = more factual"
            )
        
        with col2:
            st.session_state.max_tokens = st.slider(
                "Max Tokens",
                min_value=100,
                max_value=2000,
                value=st.session_state.get('max_tokens', 1024),
                step=100,
                help="Maximum response length"
            )
        
        # Dark Mode Toggle
        st.session_state.dark_mode = st.toggle(
            "🌙 Dark Mode",
            value=st.session_state.get('dark_mode', True)
        )
        
        st.divider()
        
        # About Section
        st.markdown("### About")
        st.markdown("""
        **StudyMate AI** is your personal study companion powered by AI.
        
        🚀 **Features:**
        - Fast responses with Groq API
        - Multiple study tools
        - Beautiful interface
        
        📚 **Great for:**
        - Students
        - Learners
        - Knowledge seekers
        """)
        
        st.divider()
        
        # Statistics
        stats = get_statistics()
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Session Requests", stats['session_requests'])
        with col2:
            st.metric("Total Requests", stats['total_requests'])


# ============================================================================
# PAGE: HOME
# ============================================================================
def page_home():
    """
    Render home page with feature cards and welcome message.
    
    Design Pattern:
    - Hero section at top
    - Feature cards for quick access
    - Statistics and benefits
    - Professional appearance
    """
    # Hero Section
    render_header("Welcome to StudyMate AI", 
                 "Your Personal AI-Powered Study Assistant", "🧠")
    
    st.markdown("""
    StudyMate AI helps you learn faster, smarter, and better. Whether you need 
    explanations, summaries, or quiz generation, we've got you covered.
    """)
    
    st.divider()
    
    # Feature Cards Grid
    st.markdown("### 🚀 Explore Our Features")
    
    col1, col2 = st.columns(2)
    
    features_list = [
        ('chat', FEATURES['chat']),
        ('summarize', FEATURES['summarize']),
        ('code', FEATURES['code']),
        ('explain', FEATURES['explain']),
        ('quiz', FEATURES['quiz']),
        ('rewrite', FEATURES['rewrite']),
    ]
    
    for idx, (key, feature) in enumerate(features_list):
        col = col1 if idx % 2 == 0 else col2
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <div style="font-size: 2.5rem; margin-bottom: 12px;">{feature['icon']}</div>
                <h3 style="margin: 0 0 8px 0; font-size: 1.3rem;">{feature['title']}</h3>
                <p style="margin: 0; color: #b0b0b0; line-height: 1.5;">
                    {feature['description']}
                </p>
                <button onclick="window.location.href='?page={key}'" 
                        style="margin-top: 12px; padding: 8px 16px; background: #0084FF; 
                                color: white; border: none; border-radius: 8px; cursor: pointer;">
                    Try Now →
                </button>
            </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    # Statistics
    st.markdown("### 📊 Why Choose StudyMate AI?")
    
    metrics = [
        {"label": "AI Powered", "value": "Groq API", "icon": "⚡"},
        {"label": "Ultra Fast", "value": "Instant", "icon": "🚀"},
        {"label": "6 Tools", "value": "Included", "icon": "🎯"},
        {"label": "Free", "value": "Always", "icon": "💎"},
    ]
    
    render_metric_cards(metrics)
    
    st.divider()
    
    # Call to Action
    st.markdown("### 🎯 Getting Started")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **1. Add Your API Key**
        - Get free key from [Groq Console](https://console.groq.com)
        - Enter it in the Settings sidebar
        
        **2. Choose a Tool**
        - Pick from 6 different study tools
        - Each tool has specific functions
        
        **3. Start Learning**
        - Ask questions, generate summaries
        - Create quizzes and explanations
        """)
    
    with col2:
        st.markdown("""
        **💡 Tips for Best Results:**
        
        ✓ Be specific with your questions
        
        ✓ Provide context when needed
        
        ✓ Use different tools for different tasks
        
        ✓ Copy and paste longer content
        
        ✓ Experiment with temperature setting
        """)


# ============================================================================
# PAGE: AI CHAT
# ============================================================================
def page_chat():
    """
    Render AI Chat page.
    
    Features:
    - Chat history display
    - User input area
    - Send button
    - Clear history
    
    Streamlit Concepts:
    - st.session_state for message history
    - Containers for layout
    - Callbacks for button actions
    """
    render_header("AI Chat", "Ask anything and get intelligent responses", "💬")
    
    st.markdown("Chat with your AI study assistant. Ask questions, get explanations, or discuss topics.")
    
    st.divider()
    
    # Chat Display Area
    chat_container = st.container(height=400, border=True)
    
    with chat_container:
        messages = get_chat_history()
        
        if not messages:
            st.markdown("""
            <div style="text-align: center; padding: 40px;">
                <div style="font-size: 2rem; margin-bottom: 12px;">💬</div>
                <p style="color: #b0b0b0;">Start a conversation with your AI assistant</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            for msg in messages:
                render_chat_message(msg['content'], is_user=(msg['role'] == 'user'))
    
    st.divider()
    
    # Input Area
    col1, col2 = st.columns([5, 1])
    
    with col1:
        user_input = st.text_input(
            "Type your question here...",
            key="chat_input",
            placeholder="Ask anything about your studies..."
        )
    
    with col2:
        send_button = st.button("Send", use_container_width=True, key="send_btn")
    
    st.divider()
    
    # Control Buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            clear_chat_history()
            st.rerun()
    
    with col2:
        if st.button("📋 Copy Last", use_container_width=True):
            if get_chat_history():
                last_msg = get_chat_history()[-1]
                st.write(f"```\n{last_msg['content']}\n```")
    
    with col3:
        st.markdown("ℹ️ Messages stay in your session")
    
    # Send Message Logic
    if send_button and user_input:
        # Get API key
        api_key = get_api_key_from_session()
        
        if not api_key:
            render_error_message(ERRORS['no_api_key'])
            return
        
        # Add user message
        add_to_chat_history("user", user_input)
        update_statistics()
        
        # Show loading
        with st.spinner("⏳ Getting response from AI..."):
            # Create AI client
            ai_client = get_ai_client(
                api_key=api_key,
                temperature=st.session_state.temperature,
                max_tokens=st.session_state.max_tokens
            )
            
            # Get response
            response = ai_client.chat(
                user_message=user_input,
                conversation_history=get_chat_history()[:-1]  # Exclude current message
            )
            
            if response:
                add_to_chat_history("assistant", response)
                st.rerun()
            else:
                render_error_message(ERRORS['api_error'])


# ============================================================================
# PAGE: SUMMARIZE NOTES
# ============================================================================
def page_summarize():
    """
    Render Notes Summarizer page.
    
    Features:
    - Large text input
    - Summary button
    - Structured output (summary, key points, concepts)
    """
    render_header("Summarize Notes", "Convert long notes into concise summaries", "📄")
    
    st.markdown("Paste your notes or any text, and get a clear summary with key points and concepts.")
    
    st.divider()
    
    # Input Area
    notes_input = render_text_input(
        label="Paste your notes here",
        key="summarize_input",
        placeholder="Paste long notes, articles, or any text you want to summarize...",
        height=250,
        help_text="The longer the input, the more concise the summary"
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        summarize_button = st.button("✨ Generate Summary", use_container_width=True)
    
    with col2:
        clear_button = st.button("🗑️ Clear", use_container_width=True)
    
    with col3:
        st.markdown("Word count: " + str(len(notes_input.split())))
    
    if clear_button:
        st.rerun()
    
    st.divider()
    
    # Results Area
    if summarize_button:
        if not notes_input.strip():
            render_error_message(ERRORS['empty_input'])
            return
        
        api_key = get_api_key_from_session()
        if not api_key:
            render_error_message(ERRORS['no_api_key'])
            return
        
        with st.spinner("✨ Summarizing your notes..."):
            ai_client = get_ai_client(
                api_key=api_key,
                temperature=st.session_state.temperature,
                max_tokens=st.session_state.max_tokens
            )
            
            summary = ai_client.generate_summary(notes_input)
            update_statistics()
            
            if summary:
                st.markdown("### 📋 Summary Results")
                
                # Display in formatted sections
                tabs = st.tabs(["Summary", "Full Response"])
                
                with tabs[0]:
                    parsed = format_summary_response(summary)
                    
                    if parsed['summary']:
                        st.markdown("#### Summary")
                        st.write(parsed['summary'])
                    
                    if parsed['key_points']:
                        st.markdown("#### Key Points")
                        for point in parsed['key_points']:
                            st.write(f"• {point}")
                    
                    if parsed['concepts']:
                        st.markdown("#### Important Concepts")
                        for concept in parsed['concepts']:
                            st.write(f"• {concept}")
                
                with tabs[1]:
                    st.markdown(summary)
                
                # Copy Button
                st.divider()
                if st.button("📋 Copy Summary", use_container_width=True):
                    st.write("```\n" + summary + "\n```")
                    render_success_message(SUCCESS_MESSAGES['copied'])
            else:
                render_error_message(ERRORS['api_error'])


# ============================================================================
# PAGE: EXPLAIN CODE
# ============================================================================
def page_explain_code():
    """
    Render Code Explainer page.
    
    Features:
    - Language selector
    - Code editor
    - Explain button
    - Step-by-step explanation
    """
    render_header("Explain Code", "Understand any code step-by-step", "💻")
    
    st.markdown("Paste your code and choose the language. Get detailed step-by-step explanations.")
    
    st.divider()
    
    # Language Selection
    col1, col2 = st.columns([1, 4])
    
    with col1:
        language = st.selectbox(
            "Select Language",
            list(SUPPORTED_LANGUAGES.keys()),
            key="code_language"
        )
    
    with col2:
        st.markdown(f"**Language:** {language}")
    
    # Code Input
    code_input = render_code_editor(language=language, key="code_input")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        explain_button = st.button("🔍 Explain Code", use_container_width=True)
    
    with col2:
        clear_button = st.button("🗑️ Clear", use_container_width=True)
    
    with col3:
        st.markdown(f"Lines: {len(code_input.split(chr(10)))}")
    
    if clear_button:
        st.rerun()
    
    st.divider()
    
    # Explanation Area
    if explain_button:
        if not code_input.strip():
            render_error_message(ERRORS['empty_input'])
            return
        
        api_key = get_api_key_from_session()
        if not api_key:
            render_error_message(ERRORS['no_api_key'])
            return
        
        with st.spinner(f"🔍 Analyzing your {language} code..."):
            ai_client = get_ai_client(
                api_key=api_key,
                temperature=st.session_state.temperature,
                max_tokens=st.session_state.max_tokens
            )
            
            explanation = ai_client.explain_code(code_input, language)
            update_statistics()
            
            if explanation:
                st.markdown("### 📚 Code Explanation")
                st.markdown(explanation)
                
                st.divider()
                
                if st.button("📋 Copy Explanation", use_container_width=True):
                    st.write("```\n" + explanation + "\n```")
                    render_success_message(SUCCESS_MESSAGES['copied'])
            else:
                render_error_message(ERRORS['api_error'])


# ============================================================================
# PAGE: QUIZ GENERATOR
# ============================================================================
def page_quiz():
    """
    Render Quiz Generator page.
    
    Features:
    - Notes input
    - Generate MCQs
    - Display questions with options
    - Answer checking
    """
    render_header("Quiz Generator", "Create practice questions from your notes", "📝")
    
    st.markdown("Paste your study notes and generate multiple-choice questions to test your knowledge.")
    
    st.divider()
    
    # Input Area
    notes_input = render_text_input(
        label="Paste your study notes",
        key="quiz_input",
        placeholder="Paste notes, textbook excerpts, or any study material...",
        height=250
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        generate_button = st.button("📝 Generate Quiz", use_container_width=True)
    
    with col2:
        clear_button = st.button("🗑️ Clear", use_container_width=True)
    
    with col3:
        st.markdown(f"Words: {len(notes_input.split())}")
    
    if clear_button:
        st.rerun()
    
    st.divider()
    
    # Quiz Generation
    if generate_button:
        if not notes_input.strip():
            render_error_message(ERRORS['empty_input'])
            return
        
        api_key = get_api_key_from_session()
        if not api_key:
            render_error_message(ERRORS['no_api_key'])
            return
        
        with st.spinner("📝 Generating quiz questions..."):
            ai_client = get_ai_client(
                api_key=api_key,
                temperature=st.session_state.temperature,
                max_tokens=st.session_state.max_tokens
            )
            
            quiz_response = ai_client.generate_quiz(notes_input)
            update_statistics()
            
            if quiz_response:
                # Parse quiz JSON
                quiz_data = format_quiz_response(quiz_response)
                
                if quiz_data:
                    st.markdown("### 🎯 Quiz Questions")
                    
                    for idx, question in enumerate(quiz_data, 1):
                        with st.container(border=True):
                            st.markdown(f"**Question {idx}:** {question.get('question', 'N/A')}")
                            
                            # Display options
                            options = question.get('options', [])
                            for opt_idx, option in enumerate(options):
                                st.markdown(f"- **{chr(65+opt_idx)}:** {option}")
                            
                            # Show answer (collapsible)
                            with st.expander("📋 Show Answer"):
                                correct_idx = question.get('correct', 0)
                                correct_answer = options[correct_idx] if correct_idx < len(options) else "Unknown"
                                st.success(f"**Correct Answer:** {chr(65+correct_idx)} - {correct_answer}")
                                st.info(f"**Explanation:** {question.get('explanation', 'N/A')}")
                            
                            st.divider()
                else:
                    st.warning("⚠️ Could not parse quiz format. Here's the raw response:")
                    st.write(quiz_response)
            else:
                render_error_message(ERRORS['api_error'])


# ============================================================================
# PAGE: REWRITE TEXT
# ============================================================================
def page_rewrite():
    """
    Render Text Rewriter page.
    
    Features:
    - Text input
    - Style selector
    - Rewrite button
    - Display rewritten text
    """
    render_header("Rewrite Text", "Rewrite text in different styles", "✍️")
    
    st.markdown("Enter text and choose a style to rewrite it. Perfect for academic writing or content creation.")
    
    st.divider()
    
    # Style Selection
    col1, col2 = st.columns([1, 4])
    
    with col1:
        style = st.selectbox(
            "Select Style",
            list(REWRITE_STYLES.keys()),
            key="rewrite_style"
        )
    
    with col2:
        st.markdown(f"**Style:** {style}")
        st.caption(REWRITE_STYLES[style])
    
    # Text Input
    text_input = render_text_input(
        label="Text to rewrite",
        key="rewrite_input",
        placeholder="Paste text you want to rewrite...",
        height=250
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        rewrite_button = st.button("✨ Rewrite", use_container_width=True)
    
    with col2:
        clear_button = st.button("🗑️ Clear", use_container_width=True)
    
    with col3:
        st.markdown(f"Characters: {len(text_input)}")
    
    if clear_button:
        st.rerun()
    
    st.divider()
    
    # Rewrite Results
    if rewrite_button:
        if not text_input.strip():
            render_error_message(ERRORS['empty_input'])
            return
        
        api_key = get_api_key_from_session()
        if not api_key:
            render_error_message(ERRORS['no_api_key'])
            return
        
        with st.spinner(f"✨ Rewriting in {style} style..."):
            ai_client = get_ai_client(
                api_key=api_key,
                temperature=st.session_state.temperature,
                max_tokens=st.session_state.max_tokens
            )
            
            rewritten = ai_client.rewrite_text(text_input, style)
            update_statistics()
            
            if rewritten:
                # Show comparison
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("#### Original")
                    st.text_area("", value=text_input, disabled=True, height=200)
                
                with col2:
                    st.markdown(f"#### Rewritten ({style})")
                    st.text_area("", value=rewritten, disabled=True, height=200, key="rewritten_output")
                
                st.divider()
                
                if st.button("📋 Copy Rewritten Text", use_container_width=True):
                    st.write("```\n" + rewritten + "\n```")
                    render_success_message(SUCCESS_MESSAGES['copied'])
            else:
                render_error_message(ERRORS['api_error'])


# ============================================================================
# MAIN APP
# ============================================================================
def main():
    """
    Main application orchestrator.
    
    Flow:
    1. Render sidebar
    2. Get current page from session state
    3. Render corresponding page
    
    Streamlit Patterns:
    - Function-based approach for each page
    - Session state for navigation
    - DRY principle (reusable components)
    """
    
    # Render sidebar
    render_sidebar()
    
    # Get current page
    current_page = st.session_state.get('current_page', 'Home')
    
    # Route to correct page
    pages = {
        'Home': page_home,
        'AI Chat': page_chat,
        'Summarize Notes': page_summarize,
        'Explain Code': page_explain_code,
        'Quiz Generator': page_quiz,
        'Rewrite Text': page_rewrite,
    }
    
    # Render page
    if current_page in pages:
        pages[current_page]()
    else:
        st.session_state.current_page = 'Home'
        st.rerun()


# ============================================================================
# ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    main()
