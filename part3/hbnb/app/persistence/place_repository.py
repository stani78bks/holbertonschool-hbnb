from app.models.place import Place
from app.persistence.database import db

class PlaceRepository:
    def add(self, place: Place):
        db.session.add(place)
        db.session.commit()
        return place

    def get(self, place_id: str):
        return Place.query.get(place_id)

    def get_all(self):
        return Place.query.all()

    def update(self, place: Place, data: dict):
        for key, value in data.items():
            if hasattr(place, key):
                setattr(place, key, value)
        db.session.commit()
        return place

    def delete(self, place: Place):
        db.session.delete(place)
        db.session.commit()

