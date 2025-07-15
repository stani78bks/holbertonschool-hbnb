from app.routes.place_routes import place_bp
from app.routes.review_routes import review_bp
from app.routes.amenity_routes import amenity_bp

app.register_blueprint(place_bp, url_prefix="/api/places")
app.register_blueprint(review_bp, url_prefix="/api/reviews")
app.register_blueprint(amenity_bp, url_prefix="/api/amenities")

