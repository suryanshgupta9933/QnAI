# Importing Dependencies
import logging
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, status

from vectordb.search import search_index

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create API Router
router = APIRouter()

# Create Search Model
class SearchQuery(BaseModel):
    search_query: str

# Search Index
@router.post("/search_index", status_code=status.HTTP_200_OK)
def search_index_endpoint(search: SearchQuery):
    try:
        results = search_index(search.search_query)
        return {
            "related_questions": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to execute search query. {e}")