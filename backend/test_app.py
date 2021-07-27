import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_test_db, Landowner, Campsite

web_owner_jwt = 'eeyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imo5WUZfSXpBb1JfVnJTUGp3XzV4LSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtMjkuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwZmYwZTM0NGFjZWE2MDA3MmRjNDMzMiIsImF1ZCI6ImNhbXAiLCJpYXQiOjE2Mjc0MDM0NjIsImV4cCI6MTYyNzQ4OTg2MiwiYXpwIjoiYWZCOEptanAwZ1FPZ1VmUzlOTmh6OGtnZ0NORGUyUVgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpjYW1wc2l0ZSIsImdldDpjYW1wc2l0ZXMiLCJnZXQ6bGFuZG93bmVyIiwicGF0Y2g6Y2FtcHNpdGUiLCJwb3N0OmNhbXBzaXRlIl19.dkd4ipuwQSVZ6-nv0MFuNzXDp3yjysaz--yo9R-5UZGj15hqYc5b9e3Z0VBqTI-Nn5REcQRF-Vs0DrMGxmHDfGVqpBYxKdFuDCDHYH0IFS3mOP3HZdLMfnBQP0wS38jTM7jykO6aKPQ0Dil-_a8pBh5YiHlmyAeJ-9uMyssLjVfIiZ6Vy39RTV8UCG2VPnTfG_gvAsuIFM-yVgLtYs5igfw3ELD6nlwnvcec787mlS-oP7EbksSS0ZfI99XPEO81jNF_d39UYXuM53TwXayxQDP3uo2vU1_alJV43KI2VzleH7wxAsKM__0W-kW8lyuRs8MOGq-StZIEjtwVHi1RLw'


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
        res = self.client().post('campsites/new', json=self.new_campsite,
                                 headers=get_headers(web_owner_jwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_new_campsite_error(self):
        res = self.client().post(
            'campsites/new', json={'address': '30 broadwood'}, headers=get_headers(web_owner_jwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Missing details')

    def test_get_campsites(self):
        res = self.client().get('/campsites', headers=get_headers(web_owner_jwt))
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
        res = self.client().delete('/campsites/11', headers=get_headers(web_owner_jwt))
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 11)

    def test_add_landowner(self):
        res = self.client().post('/landowners/add', json={'name': "John Doe", 'phone': "12345678",
                                                          'email': "abc@test.com", 'image-link': "test.image"}, headers=get_headers(web_owner_jwt))
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['landowner'])

    def test_get_landowner_list(self):
        res = self.client().get('/landowners', headers=get_headers(web_owner_jwt))
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_landowners'] > 0)

    def test_delete_landowner(self):
        res = self.client().delete('/landowners/1', headers=get_headers(web_owner_jwt))
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])


if __name__ == "__main__":
    unittest.main()
