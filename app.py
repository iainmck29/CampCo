import os
import sys
from flask import Flask, request, jsonify, abort
import json
from flask_cors import CORS, cross_origin
from .backend.auth import AuthError, requires_auth

from .backend.models import setup_test_db, Landowner, Campsite

CAMPSITES_PER_PAGE = 10


def create_app(test_config=None):
    # Create and configure app
    app = Flask(__name__)
    CORS(app)
    setup_test_db(app)

    @app.route('/add-campsite', methods=['POST'])
    @cross_origin(headers=['Content-Type', 'Authorization'])
    @requires_auth('post:campsite')
    def add_new_campsite(payload):
        body = request.json
        address = body.get('address')
        tents = body.get('tents')
        campervans = body.get('campervans')
        electricity = body.get('electricity')
        toilet = body.get('toilet')
        price = body.get('price', 0)
        region = body.get('region')
        description = body.get('description')
        campsite_image = body.get('campsite_image')
        campsite_owner = body.get('campsite_owner')

        try:
            new_campsite = Campsite(address=address, tents=tents, campervans=campervans,
                                    electricity=electricity, toilet=toilet, price=price, region=region, description=description, campsite_image=campsite_image, campsite_owner=campsite_owner)
            new_campsite.insert()

        except Exception as e:
            print(sys.exc_info())
            return jsonify({
                "success": False,
                "message": "Missing details"
            }), 422

        return jsonify({
            "success": True
        }), 200

    @app.route('/campsites', methods=['GET'])
    @cross_origin(headers=['Content-Type', 'Authorization'])
    @requires_auth('get:campsites')
    def view_campsites(payload):
        campsites = Campsite.query.order_by(Campsite.id).all()

        if len(campsites) == 0:
            abort(404)

        campsite_data = []
        for campsite in campsites:
            campsite_data.append({
                'id': campsite.id,
                'address': campsite.address,
                'tents': campsite.tents,
                'campervans': campsite.campervans,
                'electricity': campsite.electricity,
                'toilet': campsite.toilet,
                'price': campsite.price
            })

        return jsonify({
            'success': True,
            'campsites': campsite_data,
            'total_campsites': len(campsites)
        })

    @app.route('/campsites/<int:campsite_id>/edit', methods=['PATCH'])
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def edit_campsite(campsite_id):
        try:
            body = request.get_json()
            print(body)
            # unpack data
            address = body.get('address')
            tents = body.get('tents')
            campervans = body.get('campervans')
            electricity = body.get('electricity')
            toilet = body.get('toilet')
            price = body.get('price')
            region = body.get('region')
            description = body.get('description')
            campsite_image = body.get('campsite_image')
            campsite_owner = body.get('campsite_owner')

            campsite = Campsite.query.get(campsite_id)

            campsite.address = address
            campsite.tents = tents
            campsite.campervans = campervans
            campsite.electricity = electricity
            campsite.toilet = toilet
            campsite.price = price
            campsite.region = region
            campsite.description = description
            campsite.campsite_image = campsite_image
            campsite.campsite_owner = campsite_owner

            campsite.update()

        except Exception as e:
            print(sys.exc_info())
            return jsonify({
                'success': False,
                'Message': 'Unable to update'
            }), 400

        return({
            'success': True,
            'updated': campsite_id
        })

    @app.route('/campsites/<int:campsite_id>', methods=['DELETE'])
    @cross_origin(headers=['Content-Type', 'Authorization'])
    @requires_auth('delete:campsite')
    def delete_campsite(payload, campsite_id):
        campsite = Campsite.query.get(campsite_id)
        if campsite is None:
            abort(404)

        campsite.delete()

        return jsonify({
            'success': True,
            'deleted': campsite_id
        })

    @app.route('/landowners', methods=['GET'])
    @cross_origin(headers=['Content-Type', 'Authorization'])
    @requires_auth('get:landowner')
    def view_landowners(payload):
        landowners = Landowner.query.order_by(Landowner.id).all()

        if len(landowners) == 0:
            abort(404)

        landowner_data = []
        for landowner in landowners:
            landowner_data.append({
                'id': landowner.id,
                'name': landowner.name,
                'phone': landowner.phone,
                'email': landowner.email,
                'image_link': landowner.image_link,
            })

        return jsonify({
            'success': True,
            'landowners': landowner_data,
            'total_landowners': len(landowners)
        })

    @app.route('/landowners/<int:landowner_id>', methods=['DELETE'])
    @cross_origin(headers=['Content-Type', 'Authorization'])
    @requires_auth('delete:landowner')
    def delete_landowner(payload, landowner_id):
        landowner = Landowner.query.get(landowner_id)

        if landowner is None:
            return jsonify({
                'success': False,
                'message': 'Could not find owner'
            }), 404

        landowner.delete()

        return jsonify({
            'success': True,
            'deleted': landowner_id
        })

    @app.route('/landowners/add', methods=['POST'])
    @cross_origin(headers=['Content-Type', 'Authorization'])
    @requires_auth('post:landowner')
    def add_new_landowner(payload):
        body = request.get_json()

        name = body.get('name', None)
        phone = body.get('phone')
        email = body.get('email')
        image_link = body.get('image_link')

        try:
            new_landowner = Landowner(name=name, phone=phone, email=email,
                                      image_link=image_link)
            print(new_landowner)
            new_landowner.insert()

        except Exception as e:
            print(e)
            abort(403)

        return jsonify({
            "success": True,
            "landowner": new_landowner.id
        })

    return app
