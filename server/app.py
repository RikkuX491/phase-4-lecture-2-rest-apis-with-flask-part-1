#!/usr/bin/env python3

import ipdb

from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Hotel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

class Hotels(Resource):
    
    def get(self):
        hotels = Hotel.query.all()

        response_body = []

        for hotel in hotels:
            hotel_dictionary = {
                "id": hotel.id,
                "name": hotel.name
            }
            response_body.append(hotel_dictionary)

        return make_response(jsonify(response_body), 200)
    
    def post(self):
        new_hotel = Hotel(name=request.get_json().get('name'))
        db.session.add(new_hotel)
        db.session.commit()

        response_body = {
            "id": new_hotel.id,
            "name": new_hotel.name
        }

        return make_response(jsonify(response_body), 201)

api.add_resource(Hotels, '/hotels')

class HotelByID(Resource):

    def get(self, id):
        hotel = Hotel.query.filter(Hotel.id == id).first()

        if not hotel:
            response_body = {
                "error": "Hotel not found"
            }
            status = 404

        else:
            response_body = {
                "id": hotel.id,
                "name": hotel.name
            }
            status = 200

        return make_response(jsonify(response_body), status)

api.add_resource(HotelByID, '/hotels/<int:id>')

# Below is the code that we used previously before implementing flask_restful into our Flask app

# @app.route('/hotels', methods=['GET', 'POST'])
# def all_hotels():
#     if request.method == 'GET':
#         hotels = Hotel.query.all()

#         response_body = []

#         for hotel in hotels:
#             hotel_dictionary = {
#                 "id": hotel.id,
#                 "name": hotel.name
#             }
#             response_body.append(hotel_dictionary)

#         return make_response(jsonify(response_body), 200)
    
#     elif request.method == 'POST':
#         new_hotel = Hotel(name=request.get_json().get('name'))
#         db.session.add(new_hotel)
#         db.session.commit()

#         response_body = {
#             "id": new_hotel.id,
#             "name": new_hotel.name
#         }

#         return make_response(jsonify(response_body), 201)

# @app.route('/hotels/<int:id>')
# def hotel_by_id(id):
#     hotel = Hotel.query.filter(Hotel.id == id).first()

#     if not hotel:
#         response_body = {
#             "error": "Hotel not found"
#         }
#         status = 404

#     else:
#         response_body = {
#             "id": hotel.id,
#             "name": hotel.name
#         }
#         status = 200

#     return make_response(jsonify(response_body), status)

if __name__ == '__main__':
    app.run(port=7000, debug=True)