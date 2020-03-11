from app import db
from app.models.items import Item
from sqlalchemy.dialects.postgresql import JSON
import pandas as pd
import tensorflow as tf

class Rating(db.Model):
  __tablename__ = 'ratings'
  __bind_key__  = 'db1'
  

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer)
  item_id = db.Column(db.Integer)
  rating  = db.Column(db.Integer)


  def __repr__(self):
    return '<id {}>'.format(self.id)

  def all_user_ratings(self):
    all_ratings = Rating.query.all()
    ratings = []
    for rating in all_ratings:
      data = {}
      data["user_id"] = rating.user_id
      data["item_id"] = rating.item_id
      data["rating"]  = rating.rating
      ratings.append(data)
  
    return ratings

  def get_user_items(self):
    ratings = self.all_user_ratings()
    total_movies = len(Item().get_item_names())    
   
    print("*********>", ratings) 
    features = pd.DataFrame(ratings).groupby('user_id')
    user_ratings = []
    for user_id, df in features:
      data = [0] * total_movies
      for index, item in df.iterrows():
        data[item.item_id-1] = item.rating

      user_ratings.append(data)

    return tf.constant(user_ratings, dtype=tf.float32)




