# Importing Dependencies
import logging
from datetime import datetime
from firebase_admin import firestore

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

