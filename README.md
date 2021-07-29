# FULL STACK CAPSTONE PROJECT

## Camp & co by Iain McKenzie

In England, it is currently illegal to wild camp in the countryside however great amounts of land exist for potential tent dwellers to spend a night under the stars. Camp & co is a platform which allows landowners in England to register spots they have for wild camping and some basic details (toilets/electricty available etc.) for campers to view and get in contact with them should they wish to stay there. This brings a potential source of income to those with land to spare and that wild camping experience (without the illegality) to those would be woodsmen and women. Enjoy!

## Starting

Fork the project repo and clone it to your machine. The app uses a React Frontend and Flask backend. Further details for running this project locally can be found in the README's in Frontend and Backend respectively.

## About the Stack

### Backend

The backend directory contains a complete Flask and SQLAlchemy server. Authorization is set up using Auth0. The backend is currently set up to run on a local server.

### Frontend

The frontend directory contains a React framework built using the create-react-app starter code. The default routes for the frontend are to work with a local server. To change this simply change the url's to a chosen endpoint.


### Auth0 tests

Website owner with add landowner permission: email: test@email.com password: Test-123

Landowner with add campsite permissions: email: campownertest@amil.com password: Test-123


## Getting Started

### Installing Dependencies

#### Python 3.9

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/api` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we use handle the postgresql database.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we use to handle cross origin requests from our frontend server.

## Database Setup

You will first need to reset postgresql database path to yours in `models.py`

With Postgres running, restore a database using migration file provided.

1. In psql terminal, run:

```bash
create database campsites;
```

2. From the api folder in terminal run:

```bash
flask db init
flask db migrate
flask upgrade
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file to find the application.

## API Reference

### Getting Started

- Base URL: The backend app is hosted at the default, `https://camp&co.herokuapp.com/`. If you are running the app using the backend API locally, API app is hosted at `http://127.0.0.1:5000/`, which you need to set as a proxy in the frontend configuration.

### Authentication

The app enables RBAC(roles-based access control) and uses Auth0 for the authentication.

Here are two roles and its permissions:

- Website owner: `get:campsites`, `post:campsite`, `patch:campsite`, `delete:campsite`, `delete:landowner`, `post:landowner`, `get:landowner`
- CampsiteOwner: `get:campsites`, `post:campsite`, `patch:campsite`, `delete:campsite`, `get:landowner`

Here are test accounts for each role:
TODO

### Endpoints

#### GET '/campsites'

- Returns success value, an object containing all the data of the available campsites and the total amount of campsites in the list
- Sample:
```
{
    "success": True,
    "campsites": {
        "id": 1,
        "address": "30 high road"
        "tents": True,
        "campervans": False,
        "electricity": True,
        "toilet": True,
        "price": 40
    },
    "total_campsites": 1
}
```

#### POST '/add-campsite

- Returns success value and the id of the newly created campsite
- Sample:
```
{
    "success": True,
    "campsite_id": 1
}
```

#### PATCH '/campsite/<int:campsite_id>/edit'

- Returns success value and the id of the edited campsite
- Sample:
```
{
    "success": True,
    "updated": 1
}
```

#### DELETE '/campsites/<int:campsite_id>'

- Returns the success value and the id of the recently deleted campsite
- Sample:
```
{
    "success": True,
    "deleted": 1
}
```

#### GET '/landowners'

- Returns the success value, the data for the available landowners and the total amount of landowners
- Sample:
```
{
    "success": True,
    "landowers": {
        "id": 1,
        "name": "John Doe",
        "email": "abc@test.com",
        "image_link": "landowner.link"
    },
    "total_landowners": 1
}
```

#### DELETE '/landowners/<int:landowner_id>

- Returns the success value and the id of the recently deleted landowner
- Sample:
```
{
    "success": True,
    "deleted": 1
}
```

#### POST '/landowners/add'

- Returns the success value and the id of the newly created landowner
- Sample:
```
{
    "success": True,
    "landowner": 1
}
```


### Error Handling

Errors are handled as JSON object in the following format: 
```
{
    "success": False,
    "error": 404,
    "message": "page not found"
}
```


## Testing
To run the tests, run:

```
dropdb campsites
createdb campsites
python3 test_app.py
```

