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

from app.persistence.database import db
import uuid
from datetime import datetime

class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # par ex. note 1-5

    user_id = db.Column(db.String(60), nullable=False)   # relation vers User.id (à faire plus tard)
    place_id = db.Column(db.String(60), nullable=False)  # relation vers Place.id (à faire plus tard)

    def delete(self):
        """Delete the review from the database"""
        super().delete()

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

