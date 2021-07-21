import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_test_db, Landowner, Campsite


class AppTestCase(unittest.TestCase):
    def setUp(self):
        # Define test variables and initialise app
        self.app = create_app()
        self.client = self.app.test_client
        setup_test_db(self.app)

        # Define test data
        self.new_campsite = {
            'address': '29 broadwood',
            'tents': True,
            'campervans': True,
            'electricity': True,
            'toilet': True,
            'price': 40
        }

        self.new_owner = {
            'name': 'iain',
            'phone': 7455135290,
            'email': 'abc@test.co.uk',
            'image_link': 'test@image'
        }

    def tearDown(self):
        # Executed after each test
        pass

    def test_add_new_campsite(self):
        res = self.client().post('campsites/new', json=self.new_campsite)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_new_campsite_error(self):
        res = self.client().post(
            'campsites/new', json={'address': '30 broadwood'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Missing details')

    def test_get_campsites(self):
        res = self.client().get('/campsites')
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_campsites'] > 0)

    def test_edit_campsites(self):
        res = self.client().patch('/campsites/11/edit', json={
            "address": "30 Thorne Av",
            "tents": False,
            "campervans": True,
            "electricity": True,
            "toilet": True,
            "price": 20
        })
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated'], 11)

    def test_delete_campsite(self):
        res = self.client().delete('/campsites/11')
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 11)


if __name__ == "__main__":
    unittest.main()
