import React from 'react'
import NavBar from './NavBar'
import '../stylesheets/Campsites.css'
import { Link } from 'react-router-dom'
import ViewCampsite from './ViewCampsite'
import $ from 'jquery'
import LandownerView from './LandownerView'

class LandownerList extends React.Component {
    state = {
        landowners: [],
        totalLandowners: 0,

    }

    componentDidMount() {
        this.getLandowners();
    }

    getLandowners = () => {
        $.ajax({
            url: `/landowners`,
            type: "GET",
            success: (result) => {
                this.setState({
                    landowners: result.landowners,
                    totalLandowner: result.total_landowners
                })
                return;
            },
            error: (error) => {
                alert('Unable to load landowners. Please try request again')
            }
        })
    }

    handleAction = (id) => (action) => {
        if (action === 'DELETE') {
            if (window.confirm('are you sure you want to delete yourself as a landowner?')) {
                $.ajax({
                    url: `landowners/${id}`,
                    type: "DELETE",
                    success: (result) => {
                        this.getLandowners();
                    },
                    error: (error) => {
                        alert('Unable to load landowners. Please try your request again.')
                        return;
                    }
                })
            }
        }
    }



    render() {

        if (this.state.landowners.length === 0) {
            return (
                <h1>Loading</h1>
            )
        }


        return (
            <div>
                {this.state.landowners.map((l) => (
                    <LandownerView
                        key={l.id}
                        id={l.id}
                        name={l.name}
                        phone={l.phone}
                        email={l.email}
                        image_link={l.image_link}
                        handleDelete={this.handleAction(l.id)} />
                )
                )
                }
            </div>
        )
    }
}

export default LandownerList