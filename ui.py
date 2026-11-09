"""
UI Module for StudyMate AI
Reusable UI components and custom styling
Following DRY (Don't Repeat Yourself) principle
"""

import streamlit as st
from typing import Callable, Optional
import json


def apply_custom_css():
    """
    Apply custom CSS to make StudyMate look premium.
    
    Why custom CSS?
    - Default Streamlit is plain
    - Custom CSS creates professional appearance
    - Matches modern SaaS applications
    - Improves UX significantly
    
    CSS Concepts:
    - CSS variables for consistent theming
    - Gradients for modern look
    - Shadows and rounded corners for depth
    - Smooth transitions for interactivity
    """
    st.markdown("""
    <style>
    /* ===== ROOT VARIABLES ===== */
    :root {
        --primary-color: #0084FF;
        --secondary-color: #34C759;
        --danger-color: #FF3B30;
        --warning-color: #FF9500;
        --success-color: #34C759;
        --dark-bg: #0f0f0f;
        --card-bg: #1a1a1a;
        --border-color: #333;
        --text-primary: #ffffff;
        --text-secondary: #b0b0b0;
        --shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
        --radius: 12px;
    }
    
    /* ===== MAIN CONTAINER ===== */
    .main {
        background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 100%);
        color: var(--text-primary);
    }
    
    /* ===== SIDEBAR ===== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f0f0f 0%, #1a1a1a 100%);
        border-right: 1px solid var(--border-color);
    }
    
    /* ===== CARDS ===== */
    .feature-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #252525 100%);
        border: 1px solid var(--border-color);
        border-radius: var(--radius);
        padding: 24px;
        margin: 12px 0;
        box-shadow: var(--shadow);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 32px rgba(0, 132, 255, 0.2);
        border-color: var(--primary-color);
    }
    
    /* ===== METRIC CARDS ===== */
    .metric-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #252525 100%);
        border: 1px solid var(--border-color);
        border-radius: var(--radius);
        padding: 16px;
        text-align: center;
        box-shadow: var(--shadow);
    }
    
    /* ===== CHAT MESSAGES ===== */
    .chat-message {
        border-radius: var(--radius);
        padding: 12px 16px;
        margin: 8px 0;
        max-width: 70%;
        word-wrap: break-word;
    }
    
    .chat-message-user {
        background: var(--primary-color);
        margin-left: auto;
        color: white;
    }
    
    .chat-message-ai {
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        margin-right: auto;
        color: var(--text-primary);
    }
    
    /* ===== BUTTONS ===== */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-color) 0%, #0066cc 100%);
        color: white;
        border: none;
        border-radius: var(--radius);
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0, 132, 255, 0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 132, 255, 0.3);
    }
    
    /* ===== TEXT INPUT ===== */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: var(--card-bg) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: var(--radius) !important;
        color: var(--text-primary) !important;
        padding: 12px 16px !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--primary-color) !important;
        box-shadow: 0 0 0 2px rgba(0, 132, 255, 0.1) !important;
    }
    
    /* ===== SELECT BOX ===== */
    .stSelectbox > div > div > select {
        background: var(--card-bg) !important;
        border: 1px solid var(--border-color) !important;
        color: var(--text-primary) !important;
    }
    
    /* ===== EXPANDER ===== */
    .streamlit-expanderHeader {
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: var(--radius);
    }
    
    /* ===== HEADERS ===== */
    h1, h2, h3 {
        color: var(--text-primary);
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    
    h1 {
        font-size: 2.5rem;
        margin-bottom: 8px;
    }
    
    h2 {
        font-size: 1.8rem;
        margin-top: 24px;
    }
    
    h3 {
        font-size: 1.3rem;
    }
    
    /* ===== TEXT ===== */
    p, span {
        color: var(--text-secondary);
        line-height: 1.6;
    }
    
    /* ===== CODE BLOCKS ===== */
    .stCodeBlock {
        background: var(--card-bg) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: var(--radius) !important;
    }
    
    /* ===== DIVIDER ===== */
    hr {
        border-color: var(--border-color);
        margin: 24px 0;
    }
    
    /* ===== ANIMATIONS ===== */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in {
        animation: fadeIn 0.3s ease-out;
    }
    
    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {
        .chat-message {
            max-width: 90%;
        }
        
        h1 {
            font-size: 1.8rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def render_header(title: str, subtitle: str = "", emoji: str = ""):
    """
    Render a beautiful header with title and subtitle.
    
    Args:
        title: Main heading
        subtitle: Secondary text
        emoji: Icon/emoji to display
    
    Why separate function?
    - Consistent styling across all pages
    - Easy to modify header appearance globally
    - DRY principle
    """
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"<h1 style='font-size: 2rem; margin: 0;'>{emoji}</h1>", 
                   unsafe_allow_html=True)
    with col2:
        st.markdown(f"<h1 style='margin: 0;'>{title}</h1>", unsafe_allow_html=True)
        if subtitle:
            st.markdown(f"<p style='margin: 4px 0 0 0; font-size: 0.95rem;'>{subtitle}</p>", 
                       unsafe_allow_html=True)


def render_feature_card(title: str, description: str, icon: str, 
                       callback: Callable = None, key: str = ""):
    """
    Render a feature card (clickable or not).
    
    Args:
        title: Card title
        description: Card description
        icon: Emoji/icon
        callback: Function to call on click (optional)
        key: Unique key for button
    
    Streamlit Concepts:
    - st.columns() for layout
    - st.button() for interactivity
    - Callbacks for handling clicks
    - Session state for navigation
    """
    col1, col2 = st.columns([1, 5])
    
    with col1:
        st.markdown(f"<h2 style='font-size: 2.5rem; margin: 0;'>{icon}</h2>", 
                   unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"<h3 style='margin: 0;'>{title}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='margin: 4px 0 0 0; color: #b0b0b0;'>{description}</p>", 
                   unsafe_allow_html=True)
    
    if callback:
        if st.button("Open", key=key, use_container_width=True):
            callback()


def render_feature_cards_grid(features: dict):
    """
    Render multiple feature cards in a responsive grid.
    
    Args:
        features: Dictionary of features with metadata
    
    Streamlit Layout:
    - st.columns() creates a flexible grid
    - Each feature gets equal width
    - Responsive on different screen sizes
    """
    cols = st.columns(2)
    
    for idx, (key, feature) in enumerate(features.items()):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="feature-card">
                <div style="font-size: 2rem; margin-bottom: 8px;">{feature['icon']}</div>
                <h3 style="margin: 0 0 8px 0;">{feature['title']}</h3>
                <p style="margin: 0; color: #b0b0b0;">{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)


def render_metric_cards(metrics: list):
    """
    Render metric cards for statistics.
    
    Args:
        metrics: List of metric dicts with 'label', 'value', 'icon' keys
    
    Layout Strategy:
    - Responsive columns
    - Equal width for each metric
    - Professional appearance
    """
    cols = st.columns(len(metrics))
    
    for col, metric in zip(cols, metrics):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 2rem; margin-bottom: 8px;">{metric['icon']}</div>
                <p style="margin: 0; color: #b0b0b0; font-size: 0.9rem;">{metric['label']}</p>
                <p style="margin: 8px 0 0 0; font-size: 1.5rem; font-weight: 700; color: #0084FF;">
                    {metric['value']}
                </p>
            </div>
            """, unsafe_allow_html=True)


def render_text_input(label: str, key: str, placeholder: str = "", 
                     height: int = 100, help_text: str = "") -> str:
    """
    Render a styled text input field.
    
    Args:
        label: Input label
        key: Unique key for Streamlit
        placeholder: Placeholder text
        height: Height in pixels
        help_text: Help text to display
    
    Returns:
        User input text
    
    Streamlit Concepts:
    - st.text_area() for large text input
    - key parameter for state management
    - help parameter for UX
    """
    return st.text_area(
        label=label,
        key=key,
        placeholder=placeholder,
        height=height,
        help=help_text
    )


def render_code_editor(language: str = "Python", key: str = "code_input") -> str:
    """
    Render a code editor area.
    
    Args:
        language: Programming language
        key: Unique key
    
    Returns:
        Code input from user
    """
    return st.text_area(
        label="📝 Enter your code",
        key=key,
        placeholder=f"Paste your {language} code here...",
        height=250,
        language="python"
    )


def render_chat_message(content: str, is_user: bool = False):
    """
    Render a single chat message.
    
    Args:
        content: Message text
        is_user: True for user message, False for AI
    
    UI Pattern:
    - User messages on right, AI on left
    - Different colors for distinction
    - Supports markdown
    """
    if is_user:
        col1, col2 = st.columns([5, 1])
        with col2:
            st.markdown("👤")
        with col1:
            st.markdown(f"""
            <div class="chat-message chat-message-user">
                {content}
            </div>
            """, unsafe_allow_html=True)
    else:
        col1, col2 = st.columns([1, 5])
        with col1:
            st.markdown("🤖")
        with col2:
            st.markdown(f"""
            <div class="chat-message chat-message-ai">
                {content}
            </div>
            """, unsafe_allow_html=True)


def render_loading_spinner(message: str = "Processing..."):
    """
    Render a loading spinner with message.
    
    Args:
        message: Loading message
    """
    with st.spinner(f"⏳ {message}"):
        return True


def render_error_message(message: str):
    """
    Render a styled error message.
    
    Args:
        message: Error text
    """
    st.error(message)


def render_success_message(message: str):
    """
    Render a styled success message.
    
    Args:
        message: Success text
    """
    st.success(message)


def render_info_message(message: str):
    """
    Render a styled info message.
    
    Args:
        message: Info text
    """
    st.info(message)


def render_copy_button(text: str, label: str = "📋 Copy") -> bool:
    """
    Render a button to copy text to clipboard.
    
    Args:
        text: Text to copy
        label: Button label
    
    Returns:
        True if clicked
    
    Why use column?
    - Better button placement
    - More professional appearance
    """
    col1, col2, col3 = st.columns([2, 1, 1])
    with col2:
        if st.button(label, use_container_width=True):
            st.write(f"```\n{text}\n```")
            st.success("✅ Copied to clipboard!")
            return True
    return False


def render_divider():
    """Render a horizontal divider."""
    st.divider()


def render_section(title: str, emoji: str = ""):
    """
    Render a section header.
    
    Args:
        title: Section title
        emoji: Optional emoji
    """
    st.markdown(f"### {emoji} {title}")
