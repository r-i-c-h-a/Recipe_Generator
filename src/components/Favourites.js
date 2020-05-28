import React, { useEffect, useState } from 'react';
//import { SearchBox } from './components/search-box/search-box.component';
import 'semantic-ui-css/semantic.min.css';
import {Favorites} from './DisplayFavourites';


function Favourites() {
    const [favorites,showFavourites]= useState([]);
    
    useEffect(()=> { 
    fetch("/display_favourite_recipes").then(response =>
    response.json().then(data =>
    { showFavourites(data.favorites);
    })
);
    },[]);

    console.log(favorites);

    return (
    <div className="Favorites">
        

    <Favorites favorites = {favorites} />
    </div>
    );
}


export default Favourites;