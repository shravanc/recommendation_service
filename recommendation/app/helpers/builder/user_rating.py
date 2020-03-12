import tensorflow as tf

class UserRating:
  def __init__(self, users_feats, item_feats):
    self.users_feats = users_feats
    self.item_feats  = item_feats


  def evaluate(self):
    return tf.matmul(self.users_feats, tf.transpose(self.item_feats))


