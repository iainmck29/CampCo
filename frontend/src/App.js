import React from 'react'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import Home from './components/Home'
import Campsites from './components/Campsites'
import Login from './components/Login'
import Logout from './components/Logout'
import EditCampsite from './components/EditCampsite'
import AddCampsite from './components/AddCampsite'
import ViewCampsite from './components/ViewCampsite'
import NavBar from './components/NavBar'
import LoginButton from './components/LoginButton'
import { withAuth0 } from '@auth0/auth0-react'
import LandownerView from './components/LandownerView'
import LandownerList from './components/LandownerList'
import AddLandowner from './components/AddLandowner'

class App extends React.Component {
  render() {
    const { isLoading, isAuthenticated } = this.props.auth0
    return (
      <Router>
        <NavBar />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/campsites" exact component={Campsites} />
          <Route path="/add" component={AddCampsite} />
          <Route path="/campsites/:campsite_id/edit" component={EditCampsite} />
          <Route path="/logout" component={Logout} />
          <Route path="/login" component={LoginButton} />
          <Route path="/landowners" exact component={LandownerList} />
          <Route path="/landowners/add" component={AddLandowner} />

        </Switch>
      </Router>
    )
  }
}

export default withAuth0(App)