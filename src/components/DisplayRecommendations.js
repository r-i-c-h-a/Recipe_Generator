import React, { useEffect, useState } from 'react';
import './recipe/recipe.styles.css';
//import { Recipe } from './components/recipe/recipe.component';
//import { SearchBox } from './components/search-box/search-box.component';
import 'semantic-ui-css/semantic.min.css';
import {List,Header} from "semantic-ui-react";

class Directions extends React.Component{
    render(){
        return(
            <div className="recipe">
                {this.props.direction}
            </div>
        )
    }
}
class Recommendations extends React.Component {
    constructor(props) {
        super(props);
        this.state = {open:false};
      }          
    onClick(){
        this.setState({open:true});
    }
    render(){
        return (
        <List>  <h1 className="title"><center>Recommendations you will like</center></h1>
            {this.props.recommendations.map(recommendation=> {
                return (
                    <div className="row">
                        <div className="column">
                            <div className="recipe">
                                <h1 className="recipe_title">{recommendation.title}</h1>
                            <div className="image_div">
                                <img className="image" src={recommendation.image} alt="" />
                            </div>
                            <p className="calories">Calories: {parseInt(recommendation.calories)} Kcal</p>
                            <h2 className = "ingredient">Ingredients:</h2>
                            <ul className="ingredients">
                                {recommendation.ingredients}))}
                            </ul>
                            <p><a href={recommendation.site}><button className ="site-button" >View more</button></a></p>
                            </div>
                        </div>
                        <div className="column">
                            <Directions direction = {recommendation.directions}/> 
                        </div>
                    </div>
                );
            })}
            </List>
        );
    };
}

export default Recommendations;