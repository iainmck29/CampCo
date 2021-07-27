# Full Stack Capstone API Backend

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

#### POST '/add-campsite

- Returns success value and the id of the newly created campsite

#### PATCH '/campsite/<int:campsite_id>/edit'

- Returns success value and the id of the edited campsite

#### DELETE '/campsites/<int:campsite_id>'

- Returns the success value and the id of the recently deleted campsite

#### GET '/landowners'

- Returns the success value, the data for the available landowners and the total amount of landowners

#### DELETE '/landowners/<int:landowner_id>

- Returns the success value and the id of the recently deleted landowner

#### POST '/landowners/add'

- Returns the success value and the id of the newly created landowner


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
dropdb campsites_test
createdb campsites_test
python3 test_app.py
```


https://fsnd-29.eu.auth0.com/authorize?audience=camp&response_type=token&client_id=afB8Jmjp0gQOgUfS9NNhz8kggCNDe2QX&redirect_uri=http://localhost:3000