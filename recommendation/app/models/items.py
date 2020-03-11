from app import db
from sqlalchemy.dialects.postgresql import JSON


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
