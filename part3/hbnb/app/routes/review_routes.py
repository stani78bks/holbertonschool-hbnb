from flask import Blueprint, request, jsonify
from app.models.review import Review
from app.persistence.repositories.review_repository import ReviewRepository

review_bp = Blueprint('reviews', __name__)
review_repo = ReviewRepository()

@review_bp.route("/", methods=["GET"])
def get_all_reviews():
    reviews = review_repo.get_all()
    return jsonify([review.to_dict() for review in reviews])

@review_bp.route("/<string:review_id>", methods=["GET"])
def get_review(review_id):
    review = review_repo.get_by_id(review_id)
    if not review:
        return jsonify({"error": "Review not found"}), 404
    return jsonify(review.to_dict())

@review_bp.route("/", methods=["POST"])
def create_review():
    data = request.get_json()
    try:
        review = Review(**data)
        review_repo.create(review)
        return jsonify(review.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@review_bp.route("/<string:review_id>", methods=["PUT"])
def update_review(review_id):
    review = review_repo.get_by_id(review_id)
    if not review:
        return jsonify({"error": "Review not found"}), 404
    data = request.get_json()
    for key, value in data.items():
        setattr(review, key, value)
    review_repo.update(review)
    return jsonify(review.to_dict())

@review_bp.route("/<string:review_id>", methods=["DELETE"])
def delete_review(review_id):
    review = review_repo.get_by_id(review_id)
    if not review:
        return jsonify({"error": "Review not found"}), 404
    review_repo.delete(review)
    return jsonify({"message": "Review deleted successfully"})

