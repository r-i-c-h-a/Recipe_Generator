from . import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(150))
    rating = db.Column(db.Float)
    categories = db.Column(db.String(500))
    desc = db.Column(db.String(2000))
    calories = db.Column(db.Integer)
    fat = db.Column(db.Integer)
    sodium = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    ingredients = db.Column(db.String(10000))
    directions = db.Column(db.String(8500))

class Favorites(db.Model):
    key = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(150))
    calories = db.Column(db.Integer)
    image = db.Column(db.String(150))
    ingredients = db.Column(db.String(2500))
    site = db.Column(db.String(200))
