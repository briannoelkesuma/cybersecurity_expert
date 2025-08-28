# backend/app/services/feedback_service.py
from app import schemas
def log_feedback(feedback: schemas.FeedbackRequest):
    # TODO: Log this data to a CSV file or a separate database for analysis
    print(f"Feedback logged: Query='{feedback.query}', Helpful={feedback.is_helpful}")