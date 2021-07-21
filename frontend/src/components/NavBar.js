import React from 'react'
import '../stylesheets/NavBar.css';

class NavBar extends React.Component {

    navTo(uri) {
        window.location.href = window.location.origin + uri
    }

    render() {
        return (
            <div className='App-header'>
                <h1 onClick={() => { this.navTo('') }}>Camp&Co</h1>
                <h2 onClick={() => { this.navTo('') }}>Home</h2>
                <h2 onClick={() => { this.navTo('/campsites') }}>View Campsites</h2>
                <h2 onClick={() => { this.navTo('/add') }}>Add Campsite</h2>
                <h2 onClick={() => { this.navTo('/login') }}>Login</h2>
            </div>
        )
    }
}

export default NavBar