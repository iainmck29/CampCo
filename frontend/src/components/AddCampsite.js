import React from 'react'
import NavBar from './NavBar'
import '../stylesheets/AddCampsite.css'
import { Link } from 'react-router-dom'
import '../stylesheets/AddCampsite.css'
import $ from 'jquery'

class AddCampsite extends React.Component {
    state = {
        address: '',
        tents: false,
        campervans: false,
        electricity: false,
        toilet: false,
        price: 0
    }

    handleChange = (e) => {
        const property = e.target.name
        const val = e.target.value
        this.setState({
            [property]: val
        })
    }

    handleCheck = (e) => {
        const property = e.target.name
        const val = e.target.checked
        this.setState({
            [property]: val
        })
    }

    handleSubmit = (e) => {
        e.preventDefault();
        const { address, tents, campervans, electricity, toilet, price } = this.state
        $.ajax({
            url: '/add',
            type: "POST",
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({
                address: address,
                tents: tents,
                campervans: campervans,
                electricity: electricity,
                toilet: toilet,
                price: price
            }),
            success: (result) => {
                this.setState({
                    address: '',
                    tents: false,
                    campervans: false,
                    electricity: false,
                    toilet: false,
                    price: 0
                })
            }
        })
    }




    render() {
        const { address, tents, campervans, electricity, toilet, price } = this.state

        return (

            <div className='container-2'>
                <form onSubmit={this.handleSubmit} className="add-campsite-form">
                    <input type="text" value={address} onChange={this.handleChange} className="add-campsite-form-input" placeholder="Campsite address" name="address" />
                    <div className='checkbox-label'>
                        <label for="tents">Tents allowed?</label>
                        <input type="checkbox" value={tents} onChange={this.handleCheck} name="tents" />
                    </div>
                    <div className='checkbox-label'>
                        <label for="campervans">Campervans allowed?</label>
                        <input type="checkbox" value={campervans} onChange={this.handleCheck} name="campervans" />
                    </div>
                    <div className='checkbox-label'>
                        <label for="electricity">Electricity available?</label>
                        <input type="checkbox" value={electricity} onChange={this.handleCheck} name="electricity" />
                    </div>
                    <div className='checkbox-label'>
                        <label for="toilets">Toilets available?</label>
                        <input type="checkbox" value={toilet} onChange={this.handleCheck} name="toilets" />
                    </div>
                    <div className='checkbox-label'>
                        <label for="price">Price</label>
                        <input type="number" value={price} min="1" max="100" onChange={this.handleChange} name="price" />
                    </div>
                    <div className="submit">
                        <button type="submit" >Submit Campsite</button>
                    </div>
                </form>
            </div>

        )
    }
}

export default AddCampsite