from app.persistence.repositories.place_repository import PlaceRepository
from app.models.place import Place

class PlaceService:
    def __init__(self):
        self.repo = PlaceRepository()

    def create_place(self, data: dict):
        place = Place(**data)
        return self.repo.add(place)

    def get_place(self, place_id: str):
        return self.repo.get(place_id)

    def get_all_places(self):
        return self.repo.get_all()

    def update_place(self, place_id: str, data: dict):
        place = self.repo.get(place_id)
        if place:
            return self.repo.update(place, data)
        return None

    def delete_place(self, place_id: str):
        place = self.repo.get(place_id)
        if place:
            self.repo.delete(place)
            return True
        return False

