"""
AI Module for StudyMate AI
Handles all Groq API integration with robust error handling
"""

import os
import json
from typing import Optional, Dict, Any
import streamlit as st

try:
    from groq import Groq
except ImportError:
    Groq = None


class StudyMateAI:
    """
    Main AI class for StudyMate - handles all Groq API interactions.
    
    This class encapsulates:
    - API client initialization
    - Message sending with error handling
    - Retry logic
    - System prompt management
    
    Why use a class?
    - Maintains state (API client, settings)
    - Easy to extend with new methods
    - Better organization and reusability
    """
    
    def __init__(self, api_key: str, model: str = "mixtral-8x7b-32768", 
                 temperature: float = 0.7, max_tokens: int = 1024):
        """
        Initialize the AI client.
        
        Args:
            api_key: Groq API key
            model: Model to use (default: Mixtral)
            temperature: Creativity level (0-1)
            max_tokens: Maximum response length
        
        Why these parameters?
        - api_key: Required for authentication
        - model: Different models have different strengths/speeds
        - temperature: Controls response creativity (0=factual, 1=creative)
        - max_tokens: Controls response length and cost
        """
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        
        # Initialize Groq client (only if Groq library is available)
        try:
            self.client = Groq(api_key=api_key)
            self.is_initialized = True
        except Exception as e:
            self.is_initialized = False
            self.error = str(e)
    
    def send_message(self, user_message: str, system_prompt: str = "", 
                    conversation_history: list = None) -> Optional[str]:
        """
        Send a message to Groq and get a response.
        
        Args:
            user_message: The user's question/input
            system_prompt: System instructions for the AI
            conversation_history: Previous messages for context
        
        Returns:
            AI response string or None if error
        
        How this works:
        1. Format messages with system prompt
        2. Call Groq API
        3. Extract response
        4. Handle errors gracefully
        
        Python Concepts:
        - Type hints (str, list, Optional)
        - Exception handling (try/except)
        - List comprehension
        - Dictionary manipulation
        """
        if not self.is_initialized:
            return None
        
        try:
            # Build message list with conversation history
            messages = []
            
            # Add previous messages if provided (for context)
            if conversation_history:
                messages.extend(conversation_history[-10:])  # Last 10 messages for context
            
            # Add current user message
            messages.append({
                "role": "user",
                "content": user_message
            })
            
            # Call Groq API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                system=system_prompt,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
            
            # Extract and return response
            return response.choices[0].message.content
        
        except ValueError as e:
            # Validation error (e.g., invalid API key format)
            st.error(f"❌ Configuration Error: {str(e)}")
            return None
        except Exception as e:
            # Network or API errors
            st.error(f"❌ API Error: {str(e)}")
            return None
    
    def generate_summary(self, text: str) -> Optional[str]:
        """
        Generate a summary of the provided text.
        
        Args:
            text: Text to summarize
        
        Returns:
            Summary string or None if error
        
        Prompt Engineering Tip:
        - We use a structured prompt asking for specific outputs
        - This improves response quality and consistency
        """
        if not text.strip():
            return None
        
        system_prompt = """You are an expert summarizer.
Analyze the provided text and create:
1. A brief 2-3 sentence summary
2. 3-5 key points in bullet format
3. 2-3 important concepts to remember

Format your response clearly with these sections."""
        
        user_message = f"Please summarize this text:\n\n{text}"
        return self.send_message(user_message, system_prompt)
    
    def explain_text(self, text: str) -> Optional[str]:
        """
        Explain difficult text in simple language.
        
        Args:
            text: Text to explain
        
        Returns:
            Explanation string or None if error
        
        Why separate methods?
        - Each feature has different prompts
        - Makes code organized and maintainable
        - Easy to modify prompts without touching other features
        """
        if not text.strip():
            return None
        
        system_prompt = """You are a patient educator.
Break down the concept step-by-step.
Use everyday examples and analogies.
Avoid technical jargon when possible.
End with a real-world application."""
        
        user_message = f"Please explain this in simple language:\n\n{text}"
        return self.send_message(user_message, system_prompt)
    
    def explain_code(self, code: str, language: str = "Python") -> Optional[str]:
        """
        Explain code in detail.
        
        Args:
            code: Code snippet to explain
            language: Programming language
        
        Returns:
            Code explanation or None if error
        """
        if not code.strip():
            return None
        
        system_prompt = f"""You are an expert {language} code reviewer.
Analyze the provided code and explain:
1. What the code does (overview)
2. Step-by-step explanation of each part
3. Important concepts used
4. Potential improvements

Be clear, structured, and beginner-friendly."""
        
        user_message = f"Please explain this {language} code:\n\n```{language.lower()}\n{code}\n```"
        return self.send_message(user_message, system_prompt)
    
    def generate_quiz(self, notes: str) -> Optional[str]:
        """
        Generate quiz questions from notes.
        
        Args:
            notes: Study notes/text to create quiz from
        
        Returns:
            Quiz questions in JSON format or None if error
        """
        if not notes.strip():
            return None
        
        system_prompt = """You are a quiz master creating study questions.
Generate 5 multiple-choice questions based on the provided notes.
For each question provide:
- question: Question text
- options: List of 4 options
- correct: Index of correct answer (0-3)
- explanation: Why this answer is correct

Return ONLY valid JSON array. No other text."""
        
        user_message = f"Create 5 MCQ questions from these notes:\n\n{notes}"
        return self.send_message(user_message, system_prompt)
    
    def rewrite_text(self, text: str, style: str = "Professional") -> Optional[str]:
        """
        Rewrite text in different styles.
        
        Args:
            text: Text to rewrite
            style: Desired style (Professional, Simple, Formal, Friendly)
        
        Returns:
            Rewritten text or None if error
        """
        if not text.strip():
            return None
        
        style_instructions = {
            "Professional": "Make it formal, business-appropriate, and polished.",
            "Simple": "Use simple words and short sentences for easy understanding.",
            "Formal": "Use academic language and formal structure.",
            "Friendly": "Use conversational tone, friendly, and approachable.",
        }
        
        instruction = style_instructions.get(style, "Rewrite in a different style.")
        
        system_prompt = f"""You are an expert writer.
Rewrite the provided text in this style: {instruction}
Maintain the same information but adjust tone and complexity.
Do NOT add or remove information."""
        
        user_message = f"Please rewrite this text:\n\n{text}"
        return self.send_message(user_message, system_prompt)
    
    def chat(self, user_message: str, system_prompt: str = "", 
            conversation_history: list = None) -> Optional[str]:
        """
        Regular chat interaction.
        
        Args:
            user_message: User's question
            system_prompt: Custom system prompt (optional)
            conversation_history: Chat history for context
        
        Returns:
            AI response or None if error
        """
        if not user_message.strip():
            return None
        
        if not system_prompt:
            system_prompt = """You are StudyMate AI, a friendly and intelligent study assistant.
Your role is to help students understand concepts, answer questions, and support their learning.
Provide clear, concise, and helpful explanations."""
        
        return self.send_message(user_message, system_prompt, conversation_history)
    
    def validate_api_key(self) -> bool:
        """
        Check if API key is valid by making a simple API call.
        
        Returns:
            True if valid, False otherwise
        
        Why validate?
        - Better UX: Catch errors early
        - Helps users fix API key issues
        - Prevents failed operations
        """
        if not self.is_initialized:
            return False
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": "test"}],
                max_tokens=10,
            )
            return True
        except Exception:
            return False


def get_ai_client(api_key: str, model: str = "mixtral-8x7b-32768",
                  temperature: float = 0.7, max_tokens: int = 1024) -> StudyMateAI:
    """
    Factory function to create and return AI client.
    
    Why use a factory function?
    - Centralized client creation
    - Easy to add initialization logic
    - Good software design pattern
    
    Args:
        api_key: Groq API key
        model: Model name
        temperature: Temperature setting
        max_tokens: Max tokens
    
    Returns:
        StudyMateAI instance
    """
    return StudyMateAI(api_key, model, temperature, max_tokens)
