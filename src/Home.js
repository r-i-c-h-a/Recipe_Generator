import React from 'react';
import img_cookies from './images/img1.jpg';
import img_fizz from './images/img5.jpg';
import img_veggies from './images/img6.jpg';
import ReactDOM from 'react-dom';
import './home.css';
import './App.css'
import './components/recipe/recipe.styles.css'
//import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Route, Switch,Link } from "react-router-dom";
//import { NavigationBar } from './components/Navigationbar';
import App from './App';
import Favourites  from './components/Favourites';
 import  Recommend  from './components/Recommendations';
//import {Link} from 'react-router';




export default function Hello() {  
        return (
        <Router>
          <div>
            <h1>Recipe Generator</h1>       
              <div className="row">
                <div className="column">
                  <img src={img_cookies} height="400" width="600" alt="Snow" ></img>
                </div>
                <div className="column">
                  <img src={img_fizz} alt="Forest" height="400" width="600"></img>
                </div>
                <div className="column">
                  <img src={img_veggies} alt="Mountains" height="400" width="600"></img>
                </div>
                <div className="wrapper">
                  <Link to='/app'><button className="site-button"><a href="C:\Users\KIRHIKAGURUMURTHY\Desktop\WT2_Project\wt2_recipe\src\Home.js" />Let's get started</button></Link>
                </div>
                <div className="wrapper">
                  <Link to='/favourites'><button className="site-button"><a href="C:\Users\KIRHIKAGURUMURTHY\Desktop\WT2_Project\wt2_recipe\src\Home.js" />Favourites</button></Link>
                </div>
                <div className="wrapper">
                  <Link to='/recommendation'><button className="site-button"><a href="C:\Users\KIRHIKAGURUMURTHY\Desktop\WT2_Project\wt2_recipe\src\Home.js" />Recommendation</button></Link>
                </div>
              </div>
              <Switch>
                <Route path="/app">
                  <App />
                </Route>
                <Route path="/favourites">
                  <Favourites/>
                </Route>
                <Route path="/recommendation">
                  <Recommend />
                </Route>
              </Switch>
          </div>
        </Router>
      );
}

// export default Hello;