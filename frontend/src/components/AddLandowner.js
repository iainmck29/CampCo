import React from 'react'
import NavBar from './NavBar'
import '../stylesheets/AddLandowner.css'
import { Link } from 'react-router-dom'
import '../stylesheets/AddLandowner.css'
import $ from 'jquery'
import PhoneInput from 'react-phone-input-2'
import 'react-phone-input-2/lib/style.css'

class AddLandowner extends React.Component {
    state = {
        name: '',
        phone: '',
        email: '',
        image_link: ''
    }

    handleChange = (e) => {
        const property = e.target.name
        const val = e.target.value
        this.setState({
            ...this.state,
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
        const { name, phone, email, image_link } = this.state
        console.log(this.state)
        $.ajax({
            url: '/landowners/add',
            type: "POST",
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({
                name: name,
                phone: phone,
                email: email,
                image_link: image_link
            }),
            success: (result) => {
                this.setState({
                    name: '',
                    phone: '',
                    email: '',
                    image_link: ''
                })
            }
        })
    }




    render() {
        const { name, email, image_link } = this.state

        return (

            <div className='container-2'>
                <form onSubmit={this.handleSubmit} className="add-Landowner-form">
                    <input type="text" value={name} onChange={this.handleChange} className="add-Landowner-form-input" placeholder="Landowner name" name="name" />
                    <div className='input-label'>
                        <label>Phone Number: </label>
                        <PhoneInput
                            country={'uk'}
                            value={this.state.phone}
                            onChange={phone => this.setState({ phone })}
                        />
                    </div>
                    <div className='input-label'>
                        <label for="email">Email Address: </label>
                        <input type="email" value={email} onChange={this.handleChange} name="email" />
                    </div>
                    <div className='input-label'>
                        <label for="image_link">Image Link: </label>
                        <input type="text" value={image_link} onChange={this.handleChange} name="image_link" />
                    </div>
                    <div className="submit">
                        <button type="submit" >Submit Landowner</button>
                    </div>
                </form>
            </div>

        )
    }
}

export default AddLandowner