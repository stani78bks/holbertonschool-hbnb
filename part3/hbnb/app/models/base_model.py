#!/usr/bin/python3
"""Module base_model
"""
import uuid
from datetime import datetime
from app.models.db_app import db


class BaseModel(db.Model):
    __tablename__ = True # No table name specified, using default
    
    # Define the primary key and other fields to be used in the database
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def save(self):
        # add the current timestamp and commit the changes to the database
        db.session.add(self)
        db.session.commit()

    def delete(self):
        # Delete the object from the database
        db.session.delete(self)
        db.session.commit()
