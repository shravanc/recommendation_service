from flask import Flask
import os
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy


mongo = PyMongo()

print("**************", os.path.abspath(os.path.dirname(__file__)))


def create_app(config_filename=None):
  application = Flask( 'recommendation', instance_relative_config=True)
  application.config.from_pyfile(config_filename)
  initialize_extensions(application)
  register_blueprints(application)
  
  return application

def initialize_extensions(application):
  mongo.init_app(application)
  from app.models.user import User
  from app.models.rating import Rating  

  db = SQLAlchemy(application)


def register_blueprints(application):
  from app.controllers import recommends_blueprints
  application.register_blueprint(recommends_blueprints)


path = os.path.abspath(os.path.dirname(__file__)) + "/../instance/development.cfg"
print("path******>", path)
app = Flask(__name__)
app.config.from_pyfile(path)
db = SQLAlchemy(app)
#db = SQLAlchemy(create_app(path))

