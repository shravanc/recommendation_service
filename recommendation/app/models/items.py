from app import db
from sqlalchemy.dialects.postgresql import JSON
import pandas as pd
import tensorflow as tf
from app.models.genre import Genre

class Item(db.Model):
  __tablename__ = 'items'
  __bind_key__  = 'db2'


  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String)
  description = db.Column(db.String)
  state = db.Column(db.String)
  genres = db.Column(db.ARRAY(db.Integer))

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def count(self):
    return Item.query.count()

  def get_item_names(self):
    items = Item.query.all()
    titles = []
    for item in items:
      titles.append(item.title)
  
    return titles

  def all_items(self):
    items = Item.query.all()
    data = []
    titles = []

    for item in items:
      d1 = {}
      d1["id"]    = item.id
      d1["title"] = item.title
      d1["genres"]= item.genres
      
      data.append(d1)
      titles.append(item.title)
  
    return data, titles


  def get_items_features(self):
    items, title = self.all_items()
    total_item_feats = Genre().count()

    df = pd.DataFrame(items)
    features = []
    for index, item in df.iterrows():
      one_hot = [0] * total_item_feats
      for i in item.genres:
        one_hot[i-1] = 1
      features.append(one_hot)

    return tf.constant(features, dtype=tf.float32)
