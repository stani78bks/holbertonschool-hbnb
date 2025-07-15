from app.models.review import Review, db

class ReviewRepository:
    def get_by_id(self, id):
        return Review.query.get(id)

    def get_all(self):
        return Review.query.all()

    def create(self, review):
        db.session.add(review)
        db.session.commit()
        return review

    def update(self, review):
        db.session.commit()
        return review

    def delete(self, review):
        db.session.delete(review)
        db.session.commit()

