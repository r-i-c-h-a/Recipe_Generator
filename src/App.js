import React, { useEffect, useState } from 'react';
import { Recipe } from './components/recipe/recipe.component';
import { SearchBox } from './components/search-box/search-box.component';


import './App.css';

const App = () => {
  const APP_ID = 'cbd5427a';
  const APP_KEY = '0581fbaced9877b09a650da30df37af1';

  const [recipes, setRecipes] = useState([]);
  const [search, setSearch] = useState('');
  const [query, setQuery] = useState('');

  useEffect(() => {
    const getRecipes = async () => {
      const response = await fetch(
        `https://api.edamam.com/search?q=${query}&app_id=${APP_ID}&app_key=${APP_KEY}`
      );
      const data = await response.json();
      setRecipes(data.hits);
    };
    getRecipes();
  }, [query]);

  const updateSearch = e => {
    setSearch(e.target.value);
  };

  const getSearch = e => {
    e.preventDefault();
    if(!search)
      alert("Search box can't be empty");
    for(e.target.value of search.split(',')){
        if (!isNaN(e.target.value))
          alert("Please enter only text values");
        }
    setQuery(search);
  };

 /* const filterLogic = e => {
    e.target.classList.toggle('active-filter');
    const li = e.target;
    if (li.classList.contains('active-filter')) {
      setQuery(li.innerText);
    } else {
      setQuery('');
    }
  };*/

  return (
    <div className="App">
      <header className="header">
        <h1 className="title">Recipe Generator</h1>
        <form onSubmit={getSearch} className="search-form">
          <SearchBox updateSearch={updateSearch} placeholder="Search recipe" />
        </form>
      </header>
      <div className="recipes">
        {recipes.map((recipe, index) => (
          <Recipe
            key={index}
            title={recipe.recipe.label}
            calories={recipe.recipe.calories}
            image={recipe.recipe.image}
            ingredients={recipe.recipe.ingredients}
            site={recipe.recipe.url}
            //recipe={key,title,calories,image,ingredients,site}
          />
        ))}
      </div>
    </div>
  );
};

export default App;
