#!/usr/bin/python3
"""Module user business logic class
"""
import uuid
from datetime import datetime
from .base_model import BaseModel
import re
from app.models.db_app import db

regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'


class User(BaseModel):
    __tablename__ = 'users'  # Specify the table name for the User model

    # Define the fields for the User model
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        super().save()

    def delete(self):
        """Delete the user from the database"""
        super().delete()

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
