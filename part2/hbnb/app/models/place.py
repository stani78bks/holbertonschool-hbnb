#!/usr/bin/python3
"""Module place business logic class
"""
import uuid
from datetime import datetime
from .base_model import BaseModel
from .user import User
from .amenity import Amenity


class Place(BaseModel):
    def __init__(self, id, created_at, updated_at, title, description, price, latitude, longitude, owner_id: str, amenities: list):
        from ..services.facade import facade
        super().__init__(id, created_at, updated_at)
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id

        self.owner = facade.get_user(owner_id)
        if self.owner is None:
            raise ValueError(f"Owner with ID {owner_id} not found.")

        self.amenities = []
        for amenity in amenities:
            amenity_obj = facade.get_amenity(amenity)
            if amenity_obj is None:
                raise ValueError(f"Amenity with ID {amenity} not found.")
            self.amenities.append(amenity_obj)

        self.reviews = []  # List to store related reviews
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