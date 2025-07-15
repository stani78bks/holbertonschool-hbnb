
#!/usr/bin/python3
"""Module amenity business logic class
"""
from .base_model import BaseModel
from app.models.db_app import db

class Amenity(BaseModel):
    __tablename__ = 'amenities'  # Specify the table name for the Amenity model

    # Define the fields for the Amenity model
    name = db.Column(db.String(255), nullable=False)

from app.persistence.database import db
import uuid
from datetime import datetime

class Amenity(db.Model):
    __tablename__ = "amenities"

    id = db.Column(db.String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(128), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def delete(self):
        """Delete the amenity from the database"""
        super().delete()

    @staticmethod
    def validate_request_data(data: dict):
        for key in data.keys():
            value = data[key]
            if key == 'name':
                if isinstance(value, str) and (len(value) > 50 or len(value) < 1):
                    raise ValueError(f'Name must be less than 50 chars')
