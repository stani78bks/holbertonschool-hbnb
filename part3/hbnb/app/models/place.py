#!/usr/bin/python3
"""Module place business logic class
"""
import uuid
from datetime import datetime
from .base_model import BaseModel
from .user import User
from .amenity import Amenity
from app.models.db_app import db


class Place(BaseModel):
    __tablename__ = 'places'  # Specify the table name for the Place model
    
    # Define the fields for the Place model
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        super().save()

    def update(self, data):
        """
        Update the attributes of the object based on the provided dictionary
        """
        super().update(data)

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    @staticmethod
    def validate_request_data(data: dict) -> None:
        for key in data.keys():
            value = data[key]
            if key == "title":
                if isinstance(value, str) is False or len(value) < 1 or len(value) > 100:
                    raise ValueError(f"title: is incorrect, should be a non-empty string.")
            elif key == "price":
                if isinstance(value, float) is False or value < 0:
                    raise ValueError(f"price: is incorrect, should be a non-negative float.")
            elif key == "latitude":
                if value < -90 or value > 90:
                    raise ValueError(f"latitude: is incorrect, between -90 -> 90.")
            elif key == "longitude":
                if value < -180 or value > 180:
                    raise ValueError(f"longitude: is incorrect, between -180 -> 180.")