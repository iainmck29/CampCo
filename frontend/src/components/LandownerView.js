import React from 'react'
import NavBar from './NavBar'
import '../stylesheets/LandownerView.css'
import { Link } from 'react-router-dom'
import '../stylesheets/LandownerView.css'

class LandownerView extends React.Component {


    render() {

        return (
            <div className='container'>
                <h1 className='landowner-description'>
                    {this.props.address}
                </h1>
                <div className='info-divider'>
                    <div>
                        <img src={this.props.image_link} alt='campsite thumbnail' className='thumbnail' />
                    </div>
                    <div className='text-info-div'>
                        <ul className='info-list'>
                            <li>Name: {this.props.name}</li>
                            <li>Phone number: {this.props.phone}</li>
                            <li>Email address: {this.props.email}</li>

                        </ul>
                        <div>
                            <button className='delete-button' onClick={() => this.props.handleDelete('DELETE')}>
                                Delete
                            </button>
                        </div>
                    </div>
                </div>

            </div >
        )
    }
}

export default LandownerView