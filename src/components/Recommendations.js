import React, { useEffect, useState } from 'react';
//import { SearchBox } from './components/search-box/search-box.component';
import 'semantic-ui-css/semantic.min.css';
import Recommendations from './DisplayRecommendations';


function Recommend() {
    const [recommendations,showRecommendations]= useState([]);
    
    useEffect(()=> { 
    fetch('/recipe_recommendation').then(response =>
    response.json().then(data =>
    { showRecommendations(data.recommendations);
    })
);
    },[]);

    console.log(recommendations);

    return (
    <div className="Recommendations">
        

    <Recommendations recommendations = {recommendations} />
    </div>
    );
}


export default Recommend;