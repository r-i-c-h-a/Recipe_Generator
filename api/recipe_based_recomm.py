from flask import Blueprint, jsonify, request
from . import db
from .models import Recipe, Favorites
from .functions import return_csv,return_cos_sim,gen_bag_of_words,recommendation
import pandas as pd
from flask_cors import CORS
import re

main = Blueprint('main',__name__)

print("I am here")
#print(dff.head())

'''i=0
for index, row in df.iterrows():
    print(i)
    i=i+1
    r = Recipe(title=row['title'].strip(),rating=float(row['rating']),categories=row['categories'],desc=row['desc'],calories=int(row['calories']),\
    fat=int(row['fat']),sodium=int(row['sodium']),protein=int(row['protein']),ingredients=row['ingredients'],directions=row['directions'])
    db.session.add(r)
    db.session.commit()
'''
df = return_csv()
dff = gen_bag_of_words(df)
print("I added to db")

@main.route('/recipe_recommendation',methods=['POST'])
def recipe_recommendation():
    #print("Now here")
    recipe_data = request.get_json()

    #recipe_list = recipe['recipes']

    #df1 = []

    #for recipe_data in recipe_list:
    new_recipe = Favorites(title=recipe_data['title'],calories=recipe_data['calories'],\
    ingredients=str(recipe_data['ingredients']),image=recipe_data['image'],site=recipe_data['site'])
    exists = db.session.query(Favorites.title).filter_by(title=new_recipe.title).scalar() is not None
    if(not exists):
        db.session.add(new_recipe)
        db.session.commit()
    #df1.append([recipe_data['title'],recipe_data['calories'],recipe_data['ingredients']])
    #print(df1)


    return 'Done',201

@main.route('/delete_favourite',methods=['POST'])
def delete_favourite():
    recipe_data = request.get_json()

    Favorites.query.filter(Favorites.title==recipe_data).delete()
    db.session.commit()
    #df1.append([recipe_data['title'],recipe_data['calories'],recipe_data['ingredients']])
    #print(df1)

    return 'Done',201

@main.route('/recipe_recommendation',methods=['GET'])
def add_recipes():
    #print("NOW HERE")
    df1 = []

    fav_list = Favorites.query.all()

    for fav in fav_list:
        df1.append([fav.title,fav.calories,fav.ingredients])
    print(df1)
    df1 = pd.DataFrame(df1, columns=['title','calories','ingredients'])

    df1 = gen_bag_of_words(df1)
    #print(df1.head())
    #print(dff.head())

    ind, cosine_sim = return_cos_sim(dff,df1)
    recomm = recommendation(ind,cosine_sim)

    final = []
    #print(recomm)

    for i in recomm:
        food = db.session.query(Recipe).filter(Recipe.title==i).first()
        #print(food)
        if(food):
            final.append({'title':food.title,'rating':food.rating,'categories':food.categories,'desc':food.desc,'calories':food.calories,\
            'fat':food.fat,'sodium':food.sodium,'protein':food.protein,'ingredients':food.ingredients,'directions':food.directions})
    

    return jsonify({'recommendations': final})

@main.route('/display_favourite_recipes')
def display_recipes():
    #print("NOW HERE")
    fav_list = Favorites.query.all()
    favs = []
    
    

    for fav in fav_list:
        favs.append({'key':fav.key,'title':fav.title,'calories':fav.calories,\
        'ingredients':fav.ingredients,'image':fav.image,'site':fav.site})
        
    
    return jsonify({'favorites': favs})