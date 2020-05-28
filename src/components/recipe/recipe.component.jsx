import React from 'react';
import './recipe.styles.css';

export const Recipe = ({ title, calories, image, ingredients,site }) => (

//  let { recipe } = this.props;

  <div className="recipe">
    <h1 className="recipe_title">{title}</h1>
    <div className="image_div">
      <img className="image" src={image} alt="" />
    </div>
    <p className="calories">Calories: {parseInt(calories)} Kcal</p>
    <h2>Ingredients:</h2>
    <ul className="ingredients">
      {ingredients.map((ingredient, index) => (
        <li className="ingredient" key={index}>
          <i className="fas fa-caret-right" /> {ingredient.text}
        </li>
      ))}
    </ul>
    
    <p><a href={site}><button className ="site-button">View link</button></a> <button className="site-button" onClick=
     {async () => {
      //cal={parseInt(calories)};
        const recipes={title,image,calories,ingredients,site};
    
    const response = await fetch("/recipe_recommendation",{ method :"POST",
  headers: { "Content-Type" : "application/json"},
body: JSON.stringify(recipes)});
if(response.ok) {console.log("Favourite added!");}
      }}> Add to Favourites </button> </p>
    
      </div>

);
