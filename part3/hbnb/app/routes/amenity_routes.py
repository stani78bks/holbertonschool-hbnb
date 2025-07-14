from flask import Blueprint, request, jsonify
from app.models.amenity import Amenity
from app.persistence.repositories.amenity_repository import AmenityRepository

amenity_bp = Blueprint('amenities', __name__)
amenity_repo = AmenityRepository()

@amenity_bp.route("/", methods=["GET"])
def get_all_amenities():
    amenities = amenity_repo.get_all()
    return jsonify([amenity.to_dict() for amenity in amenities])

@amenity_bp.route("/<string:amenity_id>", methods=["GET"])
def get_amenity(amenity_id):
    amenity = amenity_repo.get_by_id(amenity_id)
    if not amenity:
        return jsonify({"error": "Amenity not found"}), 404
    return jsonify(amenity.to_dict())

@amenity_bp.route("/", methods=["POST"])
def create_amenity():
    data = request.get_json()
    try:
        amenity = Amenity(**data)
        amenity_repo.create(amenity)
        return jsonify(amenity.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@amenity_bp.route("/<string:amenity_id>", methods=["PUT"])
def update_amenity(amenity_id):
    amenity = amenity_repo.get_by_id(amenity_id)
    if not amenity:
        return jsonify({"error": "Amenity not found"}), 404
    data = request.get_json()
    for key, value in data.items():
        setattr(amenity, key, value)
    amenity_repo.update(amenity)
    return jsonify(amenity.to_dict())

@amenity_bp.route("/<string:amenity_id>", methods=["DELETE"])
def delete_amenity(amenity_id):
    amenity = amenity_repo.get_by_id(amenity_id)
    if not amenity:
        return jsonify({"error": "Amenity not found"}), 404
    amenity_repo.delete(amenity)
    return jsonify({"message": "Amenity deleted successfully"})

