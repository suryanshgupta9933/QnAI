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
        question_data = """Title: {title}\nBody: {body}\nTags: {tags}""".format(title=title, body=body, tags=tags)
        question_embedding = generate_embedding(question_data)
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

        # Update the index
        index.upsert(
            vectors=[data],
            namespace=namespace
        )
        logger.info(f"Question {question_id} indexed successfully.")
    except Exception as e:
        logger.error(f"Failed to index question {question_id}: {e}")
        return None

# Index Answers
def index_answer(org_id: str, user_id: str, question_id: str, answer_id: str, body: str):
    try:
        # Generate embeddings for the answer
        answer_data = body
        answer_embedding = generate_embedding(answer_data)
        logger.info(f"Answer {answer_id} embedded successfully.")

        # Connect to Pinecone
        index = connect_pinecone()
        namespace = "answers"
        
        # Prepare the data
        data = {
            "id": answer_id,
            "values": answer_embedding,
            "metadata": {
                "org_id": org_id,
                "user_id": user_id,
                "question_id": question_id,
                "answer_id": answer_id
            }
        }
        
        # Update the index
        index.upsert(
            vectors=[data],
            namespace=namespace
        )
        logger.info(f"Answer {answer_id} indexed successfully.")
    except Exception as e:
        logger.error(f"Failed to index answer {answer_id}: {e}")
        return None