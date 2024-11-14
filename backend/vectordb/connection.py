# Importing Dependencies
import os
import logging
from pinecone.grpc import PineconeGRPC as Pinecone

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize Pinecone
def connect_pinecone(PINECONE_API_KEY, INDEX_NAME):
    try:
        pinecone = Pinecone(api_key=PINECONE_API_KEY)
        index = pinecone.Index(INDEX_NAME)
        if index is not None:
            logging.info(f"Connected to Pinecone Index: {INDEX_NAME}")
            return index
        else:
            logging.error(f"Failed to connect to Pinecone Index: {INDEX_NAME}")
            return None
    except Exception as e:
        logging.error(f"Failed to connect to Pinecone: {e}")
        return None