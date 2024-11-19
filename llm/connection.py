# Importing Dependencies
import os
import logging
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def llm_model():
    """
    Load LLM model.
    """
    try:
        # Load OpenAI language model
        llm = ChatOpenAI(model="gpt-4o-mini")
        return llm
    except Exception as e:
        logger.error(f"Failed to load LLM model: {e}")
        return None