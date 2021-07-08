import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

database_name = "campsites"
database_path = os.environ.get('DATABASE_URL')

database_test_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    # db.create_all()


def setup_test_db(app, database_path=database_test_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Landowner(db.Model):
    __tablename__ = 'landowners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.Integer)
    email = db.Column(db.String())
    image_link = db.Column(db.String())

    def __init__(self, id, name, phone, email, image_link):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.image_link = image_link

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'image_link': self.image_link
        }


class Campsite(db.Model):
    __tablename__ = 'campsites'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String())
    tents = db.Column(db.Boolean, default=False)
    campervans = db.Column(db.Boolean, default=False)
    electricity = db.Column(db.Boolean, default=False)
    toilet = db.Column(db.Boolean, default=False)
    price = db.Column(db.Integer)

    def __init__(self, address, tents, campervans, electricity, toilet, price):
        self.id = id
        self.address = address
        self.tents = tents
        self.campervans = campervans
        self.electricity = electricity
        self.toilet = toilet
        self.price = price

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'address': self.address,
            'tents': self.tents,
            'campervans': self.campervans,
            'electricity': self.electricity,
            'toilet': self.toilet,
            'price': self.price
        }
