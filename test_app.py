import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from app import create_app
from models import setup_test_db, Landowner, Campsite, test_campsite, test_owner


load_dotenv()

MANAGER_TOKEN = os.environ['MANAGER_TOKEN']
CAMP_OWNER_TOKEN = os.environ['CAMP_OWNER_TOKEN']


def get_headers(token):
    return {'Authorization': f'Bearer {token}'}


class AppTestCase(unittest.TestCase):

    def setUp(self):
        # Define test variables and initialise app
        self.app = create_app()
        self.client = self.app.test_client
        setup_test_db(self.app)

        # Define test data
        self.new_campsite = {
            "address": "29 broadwood",
            "tents": True,
            "campervans": True,
            "electricity": True,
            "toilet": True,
            "price": 40,
            "region": "south-east",
            "description": "small campsite",
            "campsite_image": "image.com",
            "campsite_owner": 1
        }

        self.new_owner = {
            "name": "iain",
            "phone": 7455135290,
            "email": "abc@test.co.uk",
            "image_link": "test@image"
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # drop all existing table
            self.db.drop_all()
            # create all tables
            self.db.create_all()

    def tearDown(self):
        # Executed after each test
        pass

    # Test add landowner for website manager

    def test_add_landowner(self):
        res = self.client().post('/landowners/add', json={'name': "John Doe", 'phone': "12345678",
                                                          'email': "abc@test.com", 'image-link': "test.image"}, headers=get_headers(MANAGER_TOKEN))
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['landowner'])

    # Test add landowner for a camp owner

    def test_add_landowner_unauthorized(self):
        res = self.client().post('/landowners/add', json={'name': "John Doe", 'phone': "12345678",
                                                          'email': "abc@test.com", 'image-link': "test.image"}, headers=get_headers(CAMP_OWNER_TOKEN))
        self.assertEqual(res.status_code, 500)

    def test_get_landowner_list(self):
        res = self.client().get('/landowners', headers=get_headers(MANAGER_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_landowners'] > 0)

    def test_add_new_campsite(self):
        res = self.client().post('/add-campsite', json=self.new_campsite,
                                 headers=get_headers(MANAGER_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_new_campsite_error(self):
        res = self.client().post(
            '/add-campsite', json={"campsite_image": "missing"}, headers=get_headers(MANAGER_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_get_campsites(self):
        res = self.client().get('/campsites', headers=get_headers(MANAGER_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_campsites'] > 0)

    def test_edit_campsites(self):
        res = self.client().patch('/campsites/3/edit', json={
            "address": "30 Thorne Av",
            "tents": False,
            "campervans": True,
            "electricity": True,
            "toilet": True,
            "price": 20,
            "region": "SOUTH",
            "description": "large",
            "campsite_image": "camp.uk",
            "campsite_owner": 2
        })
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated'], 3)

    def test_delete_campsite(self):
        res = self.client().delete('/campsites/14', headers=get_headers(MANAGER_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 14)

    # Test for deleting landowners for website manager

    def test_delete_landowner(self):
        res = self.client().delete('/landowners/2', headers=get_headers(MANAGER_TOKEN))
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    # Test for deleting landowners for camp owner

    def test_delete_landowner_unauthorized(self):
        res = self.client().delete('/landowners/2', headers=get_headers(CAMP_OWNER_TOKEN))

        self.assertEqual(res.status_code, 500)


if __name__ == "__main__":
    unittest.main()
