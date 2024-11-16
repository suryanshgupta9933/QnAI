# Importing Dependencies
import os
import logging
from langchain_openai import ChatOpenAI

def llm_model():
    """
    Load LLM model.
    """
    try:
        # Load OpenAI language model
        llm = ChatOpenAI(model="gpt-4o")
        return llm
    except Exception as e:
        logger.error(f"Failed to load LLM model: {e}")
        return None