import React from 'react'
import NavBar from './NavBar'
import '../stylesheets/Home.css'
import { Link } from 'react-router-dom'

class Home extends React.Component {
    render() {
        return (
            <div>
                <div className='hero-section'>
                    <div className='hero-image'>
                        <img className='hero-image' src='campsite.jpg' alt='campsite shot' />
                    </div>
                    <div className='hero-text'>
                        <h1 className='hero-text'>
                            Find your next camping spot.
                        </h1>
                        <Link to={'/campsites'} style={{ textDecoration: 'none' }}>
                            <div className='cta'>View The Collection...</div>
                        </Link>
                    </div>
                </div>
            </div >
        )
    }
}

export default Home