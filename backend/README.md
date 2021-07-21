This doc will be used during development to give the order of tasks to be completed as they go and provide general structure in development.

Camping Connections App
This app has been created to allow landowners to advertise their land to would-be campers in England who are looking for wild places to camp. Since wild camping is illegal in England but many people in the country have lots of spare land, this app will allow those people to connect for the wild camping experience without breaking the law. 

Task: Structure app correctly to begin with development
    1. Find out how to structure app backend properly.
        - Follow other users who have used a react frontend for their application.

    2. Models completed

    3. Work in TDD. Write tests for endpoint and ensure they pass/fail as expected
        -Use Postman to test each endpoint as you go.


Endpoints:

    /
    Landing page, only need to add in react

    /campsites (GET)
    Get available campsites to view as a list

    /campsites/create (POST)
    Add a new campsite to list

    /campsites/<campsite_id>/edit (PATCH)
    Edit details of an existing campsite

    /campsites/<campsite_id> (DELETE)

    