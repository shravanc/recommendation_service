from flask import request, jsonify, render_template
#from app.models.user import User
from app.models.rating import Rating
from app.models.items import Item

#from app import mongo


def index():
  #users = User.get()
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
  items = Item.query.all()
  data = []
  for item in items:
    d1 = {}
    d1["id"]    = item.id
    d1["title"] = item.title 
    #d1["state"] = item.state
    d1["genres"]= item.genres
    data.append(d1)

  return jsonify({'data': data})
  #return render_template('index.html')
