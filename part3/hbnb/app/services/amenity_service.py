from app.persistence.repositories.amenity_repository import AmenityRepository
from app.models.amenity import Amenity

class AmenityService:
    def __init__(self):
        self.repo = AmenityRepository()

    def create_amenity(self, data: dict):
        amenity = Amenity(**data)
        return self.repo.add(amenity)

    def get_amenity(self, amenity_id: str):
        return self.repo.get(amenity_id)

    def get_all_amenities(self):
        return self.repo.get_all()

    def update_amenity(self, amenity_id: str, data: dict):
        amenity = self.repo.get(amenity_id)
        if amenity:
            return self.repo.update(amenity, data)
        return None

    def delete_amenity(self, amenity_id: str):
        amenity = self.repo.get(amenity_id)
        if amenity:
            self.repo.delete(amenity)
            return True
        return False

