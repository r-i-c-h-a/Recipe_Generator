import os
import tempfile

import pytest

from api.models import Recipe, Favorites

from api import create_app


@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def db(app):
    from api import db
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()
        db.session.commit()

# def test_app_create(app):
#     """Start with a blank database."""
#     assert app

#1. invalid method with valid request
def test_invalid_path(app,client):
    with client:
        resp = client.post('/display_favourite_recipes')
        assert resp.status_code == 405

#2. test if database is empty initially and hence no recommendations
def test_recipe_recomm_empty(app,client):
    with client:
        resp = client.get('/recipe_recommendation')
        assert resp.status_code == 204

#3. test if database is empty initially and none to display
def test_display_fav_empty(app,client):
    with client:
        resp = client.get('/display_favourite_recipes')
        assert resp.status_code == 204

#4. pass an valid favourite recipe
def test_valid_recipe_recomm(app,client):
    data = {"key":4889,
		"title": "Chicken Falafel",
		"calories":200,
		"ingredients":"[{'text': '1 1/4 cups sugar         SPLENDA®️ Naturals Sugar & Stevia Sweetener Blend  Looks & acts like sugar with 1/ 2 the calories.  SAVE NOW', 'weight': 1.25}, {'text': '2/3 cup water', 'weight': 158}, {'text': '1/4 cup corn syrup', 'weight': 85.25}, {'text': 'Vegetable-oil cooking spray', 'weight': 3.3251999999999997}]",
		"image":"src",
        "site":"src"
        }
    with client:
        resp = client.post('/recipe_recommendation',json=data)
        assert resp.status_code == 201
        assert len(Favorites.query.all()) == 1
        assert b'Done' in resp.data

#5. pass duplicate valid recipe
def test_duplicate_recipe_recomm(app,client):
    data = {"key":4889,
		"title": "Chicken Falafel",
		"calories":200,
		"ingredients":"[{'text': '1 1/4 cups sugar         SPLENDA®️ Naturals Sugar & Stevia Sweetener Blend  Looks & acts like sugar with 1/ 2 the calories.  SAVE NOW', 'weight': 1.25}, {'text': '2/3 cup water', 'weight': 158}, {'text': '1/4 cup corn syrup', 'weight': 85.25}, {'text': 'Vegetable-oil cooking spray', 'weight': 3.3251999999999997}]",
		"image":"src",
        "site":"src"
        }
    with client:
        resp = client.post('/recipe_recommendation',json=data)
        assert resp.status_code == 409
        assert len(Favorites.query.all()) == 1
        assert b'Duplicate entry' in resp.data

#6. pass an invalid favourite recipe
def test_invalid_recipe_recomm(app,client):
    data = {"key":4889,
		"title": "Chicken Falafel",
		"calories":200,
		"ingredients":"[{'text': '1 1/4 cups sugar         SPLENDA®️ Naturals Sugar & Stevia Sweetener Blend  Looks & acts like sugar with 1/ 2 the calories.  SAVE NOW', 'weight': 1.25}, {'text': '2/3 cup water', 'weight': 158}, {'text': '1/4 cup corn syrup', 'weight': 85.25}, {'text': 'Vegetable-oil cooking spray', 'weight': 3.3251999999999997}]",
		"image":"src"}
    with client:
        resp = client.post('/recipe_recommendation',json=data)
        assert resp.status_code == 400
        assert len(Favorites.query.all()) == 1
        assert b'Invalid Request' in resp.data

#7. pass an empty recipe to recipe recommendation
def test_empty_recipe_recomm(app,client):
    with client:
        resp = client.post('/recipe_recommendation')
        assert resp.status_code == 400
        assert b'Empty request' in resp.data

#8. display all favourite recipes
def test_display_fav(app,client):
    with client:
        resp = client.get('/display_favourite_recipes')
        assert resp.status_code == 200
        assert resp.is_json
        assert len(Favorites.query.all()) == len(resp.json['favorites'])

#9. make recommendation based on favourite recipes
def test_recipe_recomm(app,client):
    with client:
        resp = client.get('/recipe_recommendation')
        assert resp.status_code == 200
        assert resp.is_json
        assert len(resp.json['recommendations']) == 10

#10. pass an empty request to delete
def test_empty_delete(app,client):
    with client:
        resp = client.post('/delete_favourite')
        assert resp.status_code == 204
        assert b'' in resp.data

#11. pass a invalid request to delete
def test_invalid_delete(app,client):
    data = "Chicken Fala"
    with client:
        resp = client.post('/delete_favourite',json = data)
        assert resp.status_code == 400
        assert len(Favorites.query.all()) == 1
        assert b'Invalid Request' in resp.data

#12. pass a valid request to delete
def test_valid_delete(app,client):
    data = "Chicken Falafel"
    with client:
        resp = client.post('/delete_favourite',json = data)
        assert resp.status_code == 200
        assert len(Favorites.query.all()) == 0
        assert b'Done' in resp.data