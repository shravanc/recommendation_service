from flask import request, jsonify, render_template
from app.models.user import User
from app.models.rating import Rating

from app import mongo


def index():
  users = User.get()
  user_ratings = Rating.query.all()
  ratings = []
  for rating in user_ratings:
    d1 = {}
    d1["user_id"] = rating.user_id
    d1["item_id"] = rating.item_id
    d1["rating"]  = rating.rating
    ratings.append(d1)
  return jsonify({'data': ratings})


def home():
  return render_template('index.html')
