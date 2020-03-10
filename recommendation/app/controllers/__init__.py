import os
from flask import Blueprint, current_app

from app.controllers.recommends_controller import index as recommends_index
from app.controllers.recommends_controller import home  as recommends_home


template_dir = os.path.abspath('app/views/recommends')

recommends_blueprints = Blueprint('recommends', 'api', template_folder=template_dir)
recommends_blueprints.add_url_rule('/recommend', view_func=recommends_index, methods=['GET'])
recommends_blueprints.add_url_rule('/home', view_func=recommends_home, methods=['GET'])

