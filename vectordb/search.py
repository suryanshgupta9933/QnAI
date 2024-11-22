# Importing Dependencies
import os
import logging

from .connection import connect_pinecone
from utils.embedding import generate_embedding
from db.question import get_question

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Connect to Pinecone
index = connect_pinecone()

# Search Pinecone
def search_index(search_query: str):
    try:
        # Generate embeddings for the search query
        search_embedding = generate_embedding(search_query)
        logger.info(f"Search query embedded successfully.")

        # Query the index
        results = index.query(
            vector=search_embedding,
            namespace="questions",
            top_k=5,
            include_metadata=True,
            include_values=False,
            show_progress=False
        )
        logger.info(f"Search query executed successfully.")

        # Extract the relevant information
        related_questions = []
        for match in results["matches"]:
            metadata = match["metadata"]
            org_id = metadata["org_id"]
            question_id = metadata["question_id"]
            question = get_question(org_id, question_id)
            related_questions.append(question)
        
        return related_questions
    except Exception as e:
        logger.error(f"Failed to execute search query: {e}")
        return None