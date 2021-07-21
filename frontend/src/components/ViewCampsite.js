import React from 'react'
import NavBar from './NavBar'
import '../stylesheets/ViewCampsite.css'
import { Link } from 'react-router-dom'
import '../stylesheets/ViewCampsite.css'

class ViewCampsite extends React.Component {


    render() {

        return (
            <div className='container'>
                <h1 className='campsite-description'>
                    {this.props.address}
                </h1>
                <div className='info-divider'>
                    <div>
                        <img src='campsiteThumbnail.jpg' alt='campsite thumbnail' className='thumbnail' />
                    </div>
                    <div className='text-info-div'>
                        <ul className='info-list'>
                            <li>Tents: {this.props.tents === true ? 'Y' : 'N'}</li>
                            <li>Campervans allowed: {this.props.campervans === true ? 'Y' : 'N'}</li>
                            <li>Electricity: {this.props.electricity === true ? 'Y' : 'N'}</li>
                            <li>Toilets: {this.props.toilets === true ? 'Y' : 'N'}</li>
                            <li>Price: {this.props.price}</li>
                        </ul>
                        <div>
                            <Link to={{ pathname: `/campsites/${this.props.id}/edit` }} id={this.props.id}>
                                <button className='edit-button'>
                                    Edit
                                </button>
                            </Link>
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

export default ViewCampsite