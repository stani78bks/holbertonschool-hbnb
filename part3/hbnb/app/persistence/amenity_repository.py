from app.models.amenity import Amenity, db

class AmenityRepository:
    def get_by_id(self, id):
        return Amenity.query.get(id)

    def get_all(self):
        return Amenity.query.all()

    def create(self, amenity):
        db.session.add(amenity)
        db.session.commit()
        return amenity

    def update(self, amenity):
        db.session.commit()
        return amenity

    def delete(self, amenity):
        db.session.delete(amenity)
        db.session.commit()

