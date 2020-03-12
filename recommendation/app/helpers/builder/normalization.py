import tensorflow as tf

class Normalization:

  def __init__(self, user_items, users_ratings):
    self.user_items   = user_items
    self.users_ratings = users_ratings

  def evaluate(self):
    return tf.where(tf.equal(self.user_items, tf.zeros_like(self.user_items)),
                       self.users_ratings,
                       tf.zeros_like(tf.cast(self.user_items, tf.float32)))

