# Importing Dependencies
import os
import logging
from dotenv import load_dotenv
from pinecone.grpc import PineconeGRPC as Pinecone

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

# Initialize Pinecone
def connect_pinecone():
    try:
        pinecone = Pinecone(api_key=PINECONE_API_KEY)
        index = pinecone.Index(
            name=PINECONE_INDEX_NAME,
            pool_threads=50,
        )
        logging.info(f"Connected to Pinecone Index: {PINECONE_INDEX_NAME}")
        return index        
    except Exception as e:
        logging.error(f"Failed to connect to Pinecone: {e}")
        return None