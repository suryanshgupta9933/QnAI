# Importing Dependencies
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

