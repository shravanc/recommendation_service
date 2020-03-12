import tensorflow as tf
class UserFeature:
  
  def __init__(self, user_items, item_feats):
    self.user_items = user_items
    self.item_feats = item_feats

    self.user_feats = None

  def evaluate(self):
    
    # user feature matrix
    # matrix containing each user's embedding in the n-dimensional feature space
    users_feats = tf.matmul(self.user_items, self.item_feats)
    # normalize each user feature vector to sum to 1
    self.users_feats = users_feats/tf.reduce_sum(users_feats, axis=1, keepdims=True)
    
    return self.users_feats 
