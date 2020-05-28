import { Link } from 'react-router-dom';
import Favourites from './Favourites';

export default class Nav extends React.Component{
    render() {
        return (
            <div class="container">
                <nav>
<Link to="/Recommendations">Recommendations</Link>
<Link to="/Favourites">Favourites</Link>
                </nav>
                <Route
                    path="/Recommendations"
                    component={HomeComponent}
                    exact 
                />
                <Route
                    path="/Favourites"
                    component={Favourites} 
                />
            </div>
        );
    }
}

