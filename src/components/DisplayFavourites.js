import React, { useEffect, useState } from 'react';
import './recipe/recipe.styles.css';
//import { Recipe } from './recipe/recipe.component';
//import { SearchBox } from './components/search-box/search-box.component';
//import { Recipe } from './components/recipe/recipe.component';
import 'semantic-ui-css/semantic.min.css';
import {List,Header} from "semantic-ui-react";

export const Favorites = ({favorites}) => {
    return (
      <List>  <h1 className="title"><center>Your favourite recipes</center></h1>
        {favorites.map(favorite => {
            return (
                <div className="recipe">
    <h1 className="recipe_title">{favorite.title}</h1>
    <div className="image_div">
      <img className="image" src={favorite.image} alt="" />
    </div>
    <p className="calories">Calories: {parseInt(favorite.calories)} Kcal</p>
    <h2 className = "ingredient">Ingredients:</h2>
    <ul className="ingredients">
      {favorite.ingredients}
        
      ))
    </ul>
    <p><a href={favorite.site}><button className ="site-button">View link</button></a> 
  <button className ="site-button" onClick=
     {async () => {
      //cal={parseInt(calories)};
      var fav=favorite.title;
    
    const response = await fetch("/delete_favourite",{ method :"POST",
  headers: { "Content-Type" : "application/json"},
body: JSON.stringify(fav)});
if(response.ok) {console.log("Favourite deleted!");}
      }}> Delete Favourite </button> </p>}

</div>
        );
            })}
            </List>
        );
    };