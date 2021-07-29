import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json


database_name = "campsites"
database_path = os.environ.get('DATABASE_URL')

database_test_path = "postgresql://{}/{}".format(
    'localhost:5432', database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)


def setup_test_db(app, database_path=database_test_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.create_all()


class Landowner(db.Model):
    __tablename__ = 'landowners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String())
    email = db.Column(db.String())
    image_link = db.Column(db.String())
    campsites = db.relationship(
        "Campsite", backref="landowner", cascade="all, delete")

    def __init__(self, name, phone, email, image_link):
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
    address = db.Column(db.String(), nullable=False)
    tents = db.Column(db.Boolean, default=False)
    campervans = db.Column(db.Boolean, default=False)
    electricity = db.Column(db.Boolean, default=False)
    toilet = db.Column(db.Boolean, default=False)
    price = db.Column(db.Integer)
    region = db.Column(db.String())
    description = db.Column(db.String())
    campsite_image = db.Column(db.String())
    campsite_owner = db.Column(
        db.Integer, db.ForeignKey('landowners.id'), nullable=False)

    def __init__(self, address, tents,
                 campervans, electricity, toilet,
                 price, region, description,
                 campsite_image, campsite_owner):
        self.address = address
        self.tents = tents
        self.campervans = campervans
        self.electricity = electricity
        self.toilet = toilet
        self.price = price
        self.region = region
        self.description = description
        self.campsite_image = campsite_image
        self.campsite_owner = campsite_owner

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
            'price': self.price,
            'region': self.region,
            'description': self.description,
            'campsite_image': self.campsite_image,
            'campsite_owner': self.campsite_owner
        }


test_campsite = Campsite(address="new address", tents=True, campervans=False,
                         electricity=True, toilet=True,
                         price=40, region="region",
                         description="description",
                         campsite_image="campsite_image",
                         campsite_owner="campsite_owner")

test_owner = Landowner(name="name", phone="12345", email="email@test.com",
                       image_link="image_link.com")
