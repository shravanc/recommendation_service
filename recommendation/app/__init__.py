from flask import Flask

from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app(config_filename=None):
  application = Flask( 'recommendation', instance_relative_config=True)
  #application.config.from_pyfile(config_filename)
  #initialize_extensions(application)
  #register_blueprints(application)
  


def initialize_extension(application):
  mongo.init_app(application)
  from app.models.user import User


def register_blueprints(application):
  from app.controllers import user_blueprints
  application.register_blueprint(user_blueprints)


