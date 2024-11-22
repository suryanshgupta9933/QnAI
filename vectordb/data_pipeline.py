# Importing Dependencies
import os
import logging
from dotenv import load_dotenv

from .connection import connect_pinecone
from utils.embedding import generate_embedding

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Index Questions
def index_question(org_id: str, user_id: str, question_id: str, title: str, body: str, tags: list):
    try:
        # Generate embeddings for the question
        question_data = """Title: {title}\nBody: {body}""".format(title=title, body=body)
        print(question_data)
        question_embedding = generate_embedding(question_data)
        print(question_embedding)
        logger.info(f"Question {question_id} embedded successfully.")

        # Connect to Pinecone
        index = connect_pinecone()
        namespace = "questions"
        # Prepare the data
        data = {
            "id": question_id,
            "values": question_embedding,
            "metadata": {
                "org_id": org_id,
                "user_id": user_id,
                "question_id": question_id,
                "tags": tags
            }
        }
        print(data)
        # Update the index
        index.upsert(
            vectors=[data],
            namespace=namespace
        )
        logger.info(f"Question {question_id} indexed successfully.")
    except Exception as e:
        logger.error(f"Failed to index question {question_id}: {e}")
        return None