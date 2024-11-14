# Importing Dependencies
import uuid
import logging
from fastapi import APIRouter, HTTPException, status

from db.post import create_post, get_post, update_post_votes

# Configure Logging
logger = logging.getLogger(__name__)

# Create API Router
router = APIRouter()

# Create Post
@router.post("/post/create", status_code=status.HTTP_201_CREATED)
def create_post_endpoint(org_id: str, dept_id: str, user_id: str, title: str, content: str, tags: list, is_official_answer: bool = False):
    try:
        post_id = str(uuid.uuid4())
        create_post(org_id, dept_id, user_id, post_id, title, content, tags, is_official_answer)
        return {
            "post_id": post_id,
            "title": title,
            "content": content,
            "tags": tags,
            "is_official_answer": is_official_answer
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to create post due to Internal Server Error.")

# Get Post
@router.get("/post", status_code=status.HTTP_200_OK)
def get_post_endpoint(org_id: str, dept_id: str, user_id: str, post_id: str):
    try:
        post = get_post(org_id, dept_id, user_id, post_id)
        if post:
            return post
        else:
            raise HTTPException(status_code=404, detail=f"Post not found.")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to get post due to Internal Server Error.")

# Get Posts
@router.get("/posts", status_code=status.HTTP_200_OK)
def get_posts_endpoint(org_id: str, dept_id: str, user_id: str):
    try:
        posts = get_posts(org_id, dept_id, user_id)
        if posts:
            return posts
        else:
            raise HTTPException(status_code=404, detail=f"No posts found.")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to get posts due to Internal Server Error.")

@router.put("/post/update_vote", status_code=status.HTTP_200_OK)
def update_post_votes_endpoint(org_id: str, dept_id: str, user_id: str, post_id: str, upvotes: int = 0, downvotes: int = 0):
    try:
        update_post_votes(org_id, dept_id, user_id, post_id, upvotes=upvotes, downvotes=downvotes)
        return {
            "post_id": post_id,
            "upvotes_increment": upvotes,
            "downvotes_increment": downvotes
        }
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to update post votes due to Internal Server Error.")
