# Importing Dependencies
import math
from datetime import datetime

def sigmoid(x):
    # Sigmoid function to scale values between 0 and 1
    return 1 / (1 + math.exp(-x))

def rank_answers(answers):
    """
    Rank answers based on upvotes, downvotes
    """
    ranked_answers = []
    # Weights for different parameters
    official_answer_weight = 0.5
    author_approved_weight = 0.2
    upvote_weight = 0.25
    downvote_weight = -0.15

    # Calculate score for each answer    
    for answer in answers:
        # Fetch answer details
        created_at = answer.get("created_at")
        upvotes = answer.get("upvotes")
        downvotes = answer.get("downvotes")
        author_upvote = answer.get("author_upvote")
        is_official_answer = answer.get("is_official_answer")
        
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
        answer["score"] = score

    # Sort answers based on score
    ranked_answers = sorted(answers, key=lambda x: x["score"], reverse=True)
    return ranked_answers