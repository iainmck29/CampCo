import React from 'react'
import NavBar from './NavBar'
import '../stylesheets/Campsites.css'
import { Link } from 'react-router-dom'
import ViewCampsite from './ViewCampsite'
import $ from 'jquery'

class Campsites extends React.Component {
    state = {
        campsites: [],
        totalCampsites: 0,

    }

    componentDidMount() {
        this.getCampsites();
    }

    getCampsites = () => {
        $.ajax({
            url: `/campsites`,
            type: "GET",
            success: (result) => {
                this.setState({
                    campsites: result.campsites,
                    totalCampsites: result.total_campsites
                })
                return;
            },
            error: (error) => {
                alert('Unable to load campsites. Please try request again')
            }
        })
    }

    handleAction = (id) => (action) => {
        if (action === 'DELETE') {
            if (window.confirm('are you sure you want to delete this campsite?')) {
                $.ajax({
                    url: `campsites/${id}`,
                    type: "DELETE",
                    success: (result) => {
                        this.getCampsites();
                    },
                    error: (error) => {
                        alert('Unable to load questions. Please try your request again.')
                        return;
                    }
                })
            }
        }
    }



    render() {

        if (this.state.campsites.length === 0) {
            return (
                <h1>Loading</h1>
            )
        }


        return (
            <div>
                {this.state.campsites.map((c) => (
                    <ViewCampsite
                        key={c.id}
                        id={c.id}
                        address={c.address}
                        tents={c.tents}
                        campervans={c.campervans}
                        electricity={c.electricity}
                        toilet={c.toilet}
                        price={c.price}
                        handleDelete={this.handleAction(c.id)} />
                )
                )
                }
            </div>
        )
    }
}

export default Campsites