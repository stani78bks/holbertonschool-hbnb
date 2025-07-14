from flask import Blueprint, request, jsonify
from app.services.place_service import PlaceService

place_bp = Blueprint('places', __name__)
service = PlaceService()

@place_bp.route('/places', methods=['POST'])
def create_place():
    data = request.get_json()
    place = service.create_place(data)
    return jsonify({'id': place.id}), 201

@place_bp.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    place = service.get_place(place_id)
    if not place:
        return jsonify({'error': 'Place not found'}), 404
    return jsonify({
        'id': place.id,
        'title': place.title,
        'description': place.description,
        'price': place.price,
        'latitude': place.latitude,
        'longitude': place.longitude,
        'owner_id': place.owner_id
    })

@place_bp.route('/places', methods=['GET'])
def get_places():
    places = service.get_all_places()
    output = []
    for place in places:
        output.append({
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner_id': place.owner_id
        })
    return jsonify(output)

@place_bp.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.get_json()
    place = service.update_place(place_id, data)
    if not place:
        return jsonify({'error': 'Place not found'}), 404
    return jsonify({'message': 'Place updated'})

@place_bp.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    success = service.delete_place(place_id)
    if not success:
        return jsonify({'error': 'Place not found'}), 404
    return jsonify({'message': 'Place deleted'})

