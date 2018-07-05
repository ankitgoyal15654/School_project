#!/usr/bin/env python3
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from db import db, username, password, host, database
from urls import pages
from logg import logging

print("app run")
print(__name__)


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
    username + ':' + password + '@' + host + '/' + database

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'

jwt = JWTManager(app)
db.init_app(app)
api = Api(app)


pages(api)


if __name__ == '__main__':
    print("going to run")

    app.run()
    print("running")
