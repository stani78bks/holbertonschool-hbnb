#!/usr/bin/python3
"""Module user business logic class
"""
import uuid
from datetime import datetime
from .base_model import BaseModel
import re
from app import db  # Assuming you have set up SQLAlchemy in your Flask app
from app.models import User, Place, Review, Amenity  # Import your models


regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'


class User(BaseModel):
    def __init__(self, id, created_at, updated_at, first_name, last_name, email, hash_password):
        from app.services.facade import facade
        super().__init__(id, created_at, updated_at)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = False
        self.places = facade.get_places_by_user_id(id)  # list to store related places
        self.hash_password = hash_password

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        super().save()

    def update(self, data):
        """
        Update the attributes of the object based on the provided dictionary
        """
        super().update(data)

    @staticmethod
    def validate_request_data(data: dict):
        for key in data.keys():
            value = data[key]
            if key == 'first_name' or key == 'last_name':
                if isinstance(value, str) and (len(value) > 50 or len(value) < 1):
                    raise ValueError(f"String must be less than 50 chars or not empty")
            elif key == 'email':
                if (re.match(regex, data["email"])):
                    return data
                else:
                    raise ValueError(f"Email must follow standard email format")
            elif key == 'id':
                try:
                    uuid_user = uuid.UUID(data[key], version=4)
                except ValueError:
                    return ValueError
                return data
    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)


class SQLAlchemyRepository(Repository):
    def __init__(self, model):
        self.model = model

    def add(self, obj):
        db.session.add(obj)
        db.session.commit()

    def get(self, obj_id):
        return self.model.query.get(obj_id)

    def get_all(self):
        return self.model.query.all()

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            db.session.commit()

    def delete(self, obj_id):
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()

    def get_by_attribute(self, attr_name, attr_value):
        return self.model.query.filter(getattr(self.model, attr_name) == attr_value).first()
