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

class App extends React.Component {
  render() {
    return (
      <Router>
        <NavBar />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/campsites" exact component={Campsites} />
          <Route path="/add" component={AddCampsite} />
          <Route path="/campsites/:campsite_id/edit" component={EditCampsite} />


          {/* 
          <Route path="/login" component={Login} />
          <Route path="/logout" component={Logout} />
           */}
        </Switch>
      </Router>
    )
  }
}

export default App