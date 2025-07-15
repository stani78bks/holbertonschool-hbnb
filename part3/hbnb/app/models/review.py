#!/usr/bin/python3
"""Module review business logic class
"""
from .base_model import BaseModel
from app.models.db_app import db

class Review(BaseModel):
    __tablename__ = 'reviews'  # Specify the table name for the Review model
    
    # Define the fields for the Review model
    text = db.Column(db.String(1024), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        super().save()

    def delete(self):
        """Delete the review from the database"""
        super().delete()

    @staticmethod
    def validate_request_data(data: dict):
        for key in data.keys():
            value = data[key]
            if key == 'text':
                if  not isinstance(value, str) or len(value) < 1:
                    raise ValueError(f'Text must not be empty')
            elif key == 'rating':
                if isinstance(value, int) and (value > 5 or value < 1):
                    raise ValueError(f'Rating must be between 1 and 5')
            elif key == 'place_id':
                if isinstance(value, str) and len(value) < 1:
                    raise ValueError(f'Place ID must be a non-empty string')
            elif key == 'user_id':
                if isinstance(value, str) and len(value) < 1:
                    raise ValueError(f'User ID must be a non-empty string')
        return data
