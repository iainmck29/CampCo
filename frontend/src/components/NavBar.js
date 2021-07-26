import React from 'react'
import '../stylesheets/NavBar.css';
import { withAuth0 } from '@auth0/auth0-react'

class NavBar extends React.Component {

    navTo(uri) {
        window.location.href = window.location.origin + uri
    }

    render() {
        const { isAuthenticated } = this.props.auth0


        return (
            <div className='App-header'>
                <h1 onClick={() => { this.navTo('') }}>Camp&Co</h1>
                <h2 onClick={() => { this.navTo('') }}>Home</h2>
                <h2 onClick={() => { this.navTo('/campsites') }}>View Campsites</h2>
                <h2 onClick={() => { this.navTo('/add') }}>Add Campsite</h2>
                <h2 onClick={() => { this.navTo('/landowners') }}>View Landowners</h2>
                <h2 onClick={() => { this.navTo('/landowners/add') }}>Register</h2>

                {isAuthenticated ? (
                    <h2 onClick={() => { this.navTo('/logout') }}>Logout</h2>
                ) : (
                    <h2 onClick={() => { this.navTo('/login') }}>Login</h2>
                )}
            </div>
        )
    }
}

export default withAuth0(NavBar)