import os
import sys
from flask import Flask, request, jsonify, abort
import json
from flask_cors import CORS, cross_origin
from auth import AuthError, requires_auth

from models import setup_test_db, Landowner, Campsite

CAMPSITES_PER_PAGE = 10


# def paginate_selection(request, selection):
#     page = request.args.get('page', 1, type=int)
#     start = (page - 1) * CAMPSITES_PER_PAGE
#     end = page + CAMPSITES_PER_PAGE

#     campsites = [campsite.format() for campsite in selection]
#     current_campsites = campsites[start:end]

#     return current_campsites


def create_app(test_config=None):
    # Create and configure app
    app = Flask(__name__)
    CORS(app)
    setup_test_db(app)

    # @app.after_request
    # def after_request(response):
    #     response.headers.add('Access-Control-Allow-Headers',
    #                          'Content-Type,Authorization,True')
    #     response.headers.add('Access-Control-Allow-Methods',
    #                          'GET,POST,PATCH,DELETE,OPTIONS')

    @app.route('/add-campsite', methods=['POST'])
    @cross_origin(headers=['Content-Type', 'Authorization'])
    @requires_auth('post:campsite')
    def add_new_campsite(payload):
        body = request.get_json()

        address = body.get('address', None)
        tents = body.get('tents')
        campervans = body.get('campervans')
        electricity = body.get('electricity')
        toilet = body.get('toilet')
        price = body.get('price', 0)

        try:
            new_campsite = Campsite(address=address, tents=tents, campervans=campervans,
                                    electricity=electricity, toilet=toilet, price=price)
            new_campsite.insert()

        except Exception as e:
            abort(403)

        return jsonify({
            "success": True,
            "campsite": new_campsite.id
        })

    @app.route('/campsites', methods=['GET'])
    @cross_origin(headers=['Content-Type', 'Authorization'])
    @requires_auth('get:campsites')
    def view_campsites(payload):
        campsites = Campsite.query.order_by(Campsite.id).all()
        # current_campsites = paginate_selection(request, campsites)

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

            campsite = Campsite.query.get(campsite_id)

            campsite.address = address
            campsite.tents = tents
            campsite.campervans = campervans
            campsite.electricity = electricity
            campsite.toilet = toilet
            campsite.price = price

            campsite.update()

        except Exception as e:
            print(sys.exc_info)
            abort(400)

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
        # current_campsites = paginate_selection(request, campsites)

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
            abort(404)

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


# app = create_app()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')
