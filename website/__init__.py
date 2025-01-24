from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo


def create_app():
    global login_manager
    app = Flask(__name__)

    app.config["MONGO_URI"] = "mongodb://localhost:27017/project"
    mongo = PyMongo(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    app.mongo = mongo

    return app

