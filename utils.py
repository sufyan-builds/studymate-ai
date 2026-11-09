"""
Utilities Module for StudyMate AI
Helper functions for common operations
"""

import json
import re
from typing import Any, Dict, List, Optional
import streamlit as st


def safe_json_parse(json_string: str, default: Any = None) -> Any:
    """
    Safely parse JSON with fallback to default.
    
    Args:
        json_string: JSON string to parse
        default: Default value if parsing fails
    
    Returns:
        Parsed JSON or default value
    
    Why safe parsing?
    - API responses might be malformed
    - Prevents app crashes
    - Better error handling
    
    Python Concepts:
    - Exception handling
    - Try/except blocks
    - Type hints
    """
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        st.warning(f"⚠️ Could not parse response: {str(e)[:50]}...")
        return default


def extract_json_from_text(text: str) -> Optional[Dict]:
    """
    Extract JSON from text (useful when API returns mixed content).
    
    Args:
        text: Text that might contain JSON
    
    Returns:
        Parsed JSON dict or None
    
    Regex Concepts:
    - Pattern matching for JSON objects
    - findall() to extract matching patterns
    - Character escaping in regex
    """
    # Look for JSON objects in text
    json_pattern = r'\{[^{}]*\}'
    matches = re.findall(json_pattern, text, re.DOTALL)
    
    if matches:
        for match in matches:
            result = safe_json_parse(match)
            if result:
                return result
    
    return None


def format_quiz_response(quiz_json: str) -> Optional[List[Dict]]:
    """
    Parse and format quiz response from AI.
    
    Args:
        quiz_json: JSON string from AI
    
    Returns:
        Formatted quiz questions list
    
    Data Structure:
    - Quiz is a list of question dictionaries
    - Each question has: question, options, correct, explanation
    - This standardizes the data format
    """
    try:
        # First try to parse as-is
        data = json.loads(quiz_json)
        
        # Validate structure
        if isinstance(data, list):
            for item in data:
                if all(key in item for key in ['question', 'options', 'correct']):
                    return data
        
        # If direct parsing fails, try to extract JSON
        extracted = extract_json_from_text(quiz_json)
        if extracted and isinstance(extracted, list):
            return extracted
        
        return None
    except Exception as e:
        st.warning(f"Could not parse quiz: {str(e)}")
        return None


def format_summary_response(text: str) -> Dict[str, str]:
    """
    Parse summary response from AI into structured format.
    
    Args:
        text: Summary response from AI
    
    Returns:
        Dictionary with summary, key_points, concepts
    
    String Processing:
    - Split by common delimiters
    - Strip whitespace
    - Clean up formatting
    """
    lines = text.split('\n')
    
    summary = ""
    key_points = []
    concepts = []
    current_section = None
    
    for line in lines:
        line = line.strip()
        
        if not line:
            continue
        
        # Identify sections
        if "summary" in line.lower() and ":" in line:
            current_section = "summary"
            line = line.split(":", 1)[1].strip()
        elif "key point" in line.lower() and ":" in line:
            current_section = "key_points"
            line = line.split(":", 1)[1].strip()
        elif "concept" in line.lower() and ":" in line:
            current_section = "concepts"
            line = line.split(":", 1)[1].strip()
        
        # Add to appropriate section
        if line:
            if current_section == "summary":
                summary += line + " "
            elif current_section == "key_points":
                key_points.append(line)
            elif current_section == "concepts":
                concepts.append(line)
    
    return {
        "summary": summary.strip(),
        "key_points": key_points,
        "concepts": concepts
    }


def validate_api_key(api_key: str) -> bool:
    """
    Validate API key format (basic check).
    
    Args:
        api_key: API key to validate
    
    Returns:
        True if valid format
    
    Validation:
    - Check if key exists and has reasonable length
    - Not a complete validation (needs actual API call)
    - Basic sanity check
    """
    if not api_key:
        return False
    
    # Groq API keys are usually 30+ characters
    if len(api_key.strip()) < 20:
        return False
    
    return True


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """
    Truncate text to max length with ellipsis.
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add
    
    Returns:
        Truncated text
    
    Use Cases:
    - Display previews
    - Prevent text overflow
    - Better UX for long responses
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def count_tokens_estimate(text: str) -> int:
    """
    Estimate token count for text (rough approximation).
    
    Args:
        text: Text to estimate tokens for
    
    Returns:
        Approximate token count
    
    Token Estimation:
    - Average: 1 token ≈ 4 characters
    - Used for setting max_tokens dynamically
    - Helps avoid truncation
    """
    # Rough approximation: 1 token ≈ 4 characters
    return max(1, len(text) // 4)


def format_code_block(code: str, language: str = "python") -> str:
    """
    Format code as markdown code block.
    
    Args:
        code: Code to format
        language: Programming language
    
    Returns:
        Formatted code block
    
    Markdown:
    - Triple backticks for code blocks
    - Language specification for syntax highlighting
    """
    return f"```{language}\n{code}\n```"


def initialize_session_state():
    """
    Initialize Streamlit session state variables.
    
    Streamlit Concepts:
    - st.session_state for persistent data within a session
    - Initialize on app load
    - Maintains state across reruns
    
    Why session state?
    - Resets on browser refresh (expected behavior)
    - Persists during navigation
    - No database needed
    """
    
    # Chat state
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []
    
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Home"
    
    # Settings
    if 'api_key' not in st.session_state:
        st.session_state.api_key = ""
    
    if 'temperature' not in st.session_state:
        st.session_state.temperature = 0.7
    
    if 'max_tokens' not in st.session_state:
        st.session_state.max_tokens = 1024
    
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = True
    
    # Statistics
    if 'total_requests' not in st.session_state:
        st.session_state.total_requests = 0
    
    if 'session_requests' not in st.session_state:
        st.session_state.session_requests = 0


def update_statistics():
    """Update request statistics in session state."""
    if 'total_requests' not in st.session_state:
        st.session_state.total_requests = 0
    if 'session_requests' not in st.session_state:
        st.session_state.session_requests = 0
    
    st.session_state.total_requests += 1
    st.session_state.session_requests += 1


def get_statistics() -> Dict[str, Any]:
    """
    Get current statistics.
    
    Returns:
        Dictionary with statistics
    """
    return {
        "total_requests": st.session_state.get('total_requests', 0),
        "session_requests": st.session_state.get('session_requests', 0),
        "theme": "🌙 Dark" if st.session_state.get('dark_mode', True) else "☀️ Light",
    }


def add_to_chat_history(role: str, content: str):
    """
    Add message to chat history.
    
    Args:
        role: "user" or "assistant"
        content: Message content
    
    Data Structure:
    - Chat history is a list of dictionaries
    - Each message has role and content
    - Matches OpenAI/Groq message format
    """
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []
    
    st.session_state.chat_messages.append({
        "role": role,
        "content": content
    })


def get_chat_history() -> List[Dict[str, str]]:
    """Get chat history from session state."""
    return st.session_state.get('chat_messages', [])


def clear_chat_history():
    """Clear chat history."""
    st.session_state.chat_messages = []


def get_api_key_from_session() -> str:
    """
    Get API key from session or environment.
    
    Returns:
        API key string
    
    Priority:
    1. Session state (user entered in settings)
    2. Environment variable (for deployment)
    3. Empty string (user must enter)
    """
    import os
    
    # Check session state first
    if st.session_state.get('api_key'):
        return st.session_state.api_key
    
    # Check environment variable
    env_key = os.getenv('GROQ_API_KEY')
    if env_key:
        return env_key
    
    return ""


def format_error_message(error: Exception) -> str:
    """
    Format error message for display.
    
    Args:
        error: Exception object
    
    Returns:
        Formatted error message
    
    Error Handling:
    - Extract useful information from exception
    - Make it user-friendly
    - Log important details
    """
    error_str = str(error)
    
    if "API key" in error_str or "authentication" in error_str:
        return "🔑 Authentication Error: Check your Groq API key in Settings"
    elif "rate limit" in error_str.lower():
        return "⏱️ Rate Limit: Too many requests. Please wait a moment."
    elif "timeout" in error_str.lower():
        return "⏱️ Timeout: Request took too long. Try again."
    elif "connection" in error_str.lower():
        return "🌐 Connection Error: Check your internet connection."
    else:
        return f"❌ Error: {truncate_text(error_str, 100)}"
