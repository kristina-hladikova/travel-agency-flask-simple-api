from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from database import db
import os
from resources.customers import Customer, Customers
from resources.homepage import HomePage
from resources.trips import Trips, Trip


# Inicializace aplikace
app = Flask(__name__)
api = Api(app)
basedir = os.path.abspath(os.path.dirname(__file__))


# Konfigurace databáze
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


# Endpoity
api.add_resource(HomePage, '/')
api.add_resource(Customers, '/customers')
api.add_resource(Customer, '/customer/<string:username>')
api.add_resource(Trips, '/trips')
api.add_resource(Trip, '/trip/<int:trip_id>')


# Spuštění aplikace
if __name__ == '__main__':
    app.run(port=3333, debug=True)