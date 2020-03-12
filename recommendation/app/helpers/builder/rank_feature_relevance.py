import tensorflow as tf
class RankFeatureRelevance():
  def __init__(self, user_feats, num_feats, num_users, feats, users):
    self.user_feats = user_feats  
    self.num_feats  = num_feats
    self.num_users  = num_users
    self.feats      = feats 
    self.users      = users
    self.top_user_features = None

  def evaluate(self):
    self.top_user_features = tf.nn.top_k(self.user_feats, self.num_feats)[1]

    for i in range(self.num_users):
      feature_names = [self.feats[int(index)] for index in self.top_user_features[i]]
      print('{}: {}'.format(self.users[i],feature_names))

    return self.top_user_features
