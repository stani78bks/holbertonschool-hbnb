#!/usr/bin/python3
"""Module users API endpoint
"""
from flask_restx import Namespace, Resource, fields
from app.services.facade import facade
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')


    api.response(201, 'User successfully registered')
    @api.response(400, 'Invalid input data or email already registered')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        required_fields = ['first_name', 'last_name', 'email', 'password']
        if not all(field in user_data for field in required_fields):
            return {'error': 'Missing required fields'}, 400

        # Vérification de l'unicité de l'email
        existing_user = facade.get_user_by_email(user_d8ata['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        try:
            # Hachage du mot de passe
            password = user_data.pop('password')  # on le retire temporairement du dict
            new_user = facade.create_user(user_data)
            new_user.hash_password(password)  # hachage via méthode du modèle

            # Sauvegarde de l'utilisateur avec le mot de passe haché
            facade.save_user(new_user)

            return {
                'id': new_user.id,
                'first_name': new_user.first_name,
                'last_name': new_user.last_name,
                'email': new_user.email
            }, 201

        except ValueError as error:
            return {'error': 'Invalid input data'}, 400


        @api.response(200, 'OK')
    def get(self):
        """Retrieve list of Users"""
        list_of_users = facade.get_all_users()
        return [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email} for user in list_of_users], 200

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user_id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200

    @api.expect(user_model)
    @api.response(200, 'User updated successfully')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    def put(self, user_id):
        """Update an user's information"""
        # Placeholder for the logic to update a user by ID

	current_user = get_jwt_identity()

	if user_id != current_user['id']:
	    return {'error': 'Unauthorized action'}, 403
        user_data = api.payload

         # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        try:
            updated_user = facade.update_user(user_id, user_data)
        except ValueError as error:
            return {'error': 'Invalid input data'}, 400

        if not updated_user:
            return {'error': 'User not found'}, 404
        return {'id': user_id}, 200

    @api.response(200, 'User deleted successfully')
    @api.response(404, 'User not found')
    def delete(self, user_id):
        """Delete a user"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        facade.delete_user(user_id)
        return {"message": "User deleted successfully"}, 200


