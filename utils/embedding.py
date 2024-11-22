# Imnporting Dependencies
import os
import logging
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def generate_embedding(data):
    try:
        embedding_model = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=1024)
        embedding_data = embedding_model.embed_query(data)
        logger.info(f"Embedding generated successfully.")
        return embedding_data
    except Exception as e:
        logger.error(f"Failed to generate embedding: {e}")
        return None