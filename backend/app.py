import os
import sys
from flask import Flask, request, jsonify, abort
import json
from flask_cors import CORS

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

    @app.route('/add', methods=['POST'])
    def add_new_campsite():
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
            print(e)
            abort(403)

        return jsonify({
            "success": True,
        })

    @app.route('/campsites', methods=['GET'])
    def view_campsites():
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
    def edit_campsite(campsite_id):
        try:
            body = request.get_json()
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

        return({
            'success': True,
            'updated': campsite_id
        })

    @app.route('/campsites/<int:campsite_id>', methods=['DELETE'])
    def delete_campsite(campsite_id):
        campsite = Campsite.query.get(campsite_id)
        if campsite is None:
            abort(404)

        campsite.delete()

        return jsonify({
            'success': True,
            'deleted': campsite_id
        })

    # @app.route('/campsites/<int:campsite_id>', methods=['DELETE'])
    # def delete_campsite(campsite_id):
    #     campsite = Campsite.query.get(campsite_id)
    #     if campsite is None:
    #         abort(404)

    #     campsite_data = []

    #     campsite_data.append({
    #         'id': campsite.id,
    #         'address': campsite.address,
    #         'tents': campsite.tents,
    #         'campervans': campsite.campervans,
    #         'electricity': campsite.electricity,
    #         'toilet': campsite.toilet,
    #         'price': campsite.price
    #     })

    #     return jsonify({
    #         'success': True,
    #         'campsite': campsite_data
    #     })

    return app
