# Importing Dependencies
import math
from datetime import datetime

def sigmoid(x):
    # Sigmoid function to scale values between 0 and 1
    return 1 / (1 + math.exp(-x))

def rank_responses(responses):
    """
    Rank responses based on upvotes, downvotes
    """
    ranked_responses = []
    # Weights for different parameters
    official_answer_weight = 0.5
    author_approved_weight = 0.2
    upvote_weight = 0.25
    downvote_weight = -0.15

    # Calculate score for each response    
    for response in responses:
        # Fetch response details
        created_at = response.get("created_at")
        upvotes = response.get("upvotes")
        downvotes = response.get("downvotes")
        author_upvote = response.get("author_upvote")
        is_official_answer = response.get("is_official_answer")
        
        # Calculate time difference
        # age_in_days = (datetime.now() - created_at).days + 1
        # age_factor = max(1, 1 / (age_in_days) / 30)

        # Calculate rank score
        score = 0
        if is_official_answer:
            score += official_answer_weight
        if author_upvote:
            score += author_approved_weight
        score += upvote_weight * upvotes
        score += downvote_weight * downvotes
        # score *= age_factor

        # Apply sigmoid function to total votes
        score = sigmoid(score/5)
        response["score"] = score

    # Sort responses based on score
    ranked_responses = sorted(responses, key=lambda x: x["score"], reverse=True)
    return ranked_responses