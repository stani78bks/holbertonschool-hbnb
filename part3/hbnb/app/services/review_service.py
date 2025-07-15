from app.persistence.repositories.review_repository import ReviewRepository
from app.models.review import Review

class ReviewService:
    def __init__(self):
        self.repo = ReviewRepository()

    def create_review(self, data: dict):
        review = Review(**data)
        return self.repo.add(review)

    def get_review(self, review_id: str):
        return self.repo.get(review_id)

    def get_all_reviews(self):
        return self.repo.get_all()

    def update_review(self, review_id: str, data: dict):
        review = self.repo.get(review_id)
        if review:
            return self.repo.update(review, data)
        return None

    def delete_review(self, review_id: str):
        review = self.repo.get(review_id)
        if review:
            self.repo.delete(review)
            return True
        return False

