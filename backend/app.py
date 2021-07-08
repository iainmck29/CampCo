import os
from flask import Flask, request, jsonify, abort
import json
from flask_cors import CORS

from models import setup_test_db, Landowner, Campsite

CAMPSITES_PER_PAGE = 10


def paginate_selection(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * CAMPSITES_PER_PAGE
    end = page + CAMPSITES_PER_PAGE

    campsites = [campsite.format() for campsite in selection]
    current_campsites = campsites[start:end]

    return current_campsites


def create_app(test_config=None):
    # Create and configure app
    app = Flask(__name__)
    CORS(app)
    setup_test_db(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,True')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,POST,PATCH,DELETE,OPTIONS')

    @app.route('/campsites', methods=['GET'])
    def index():

        return

    return app
