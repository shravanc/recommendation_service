import tensorflow as tf
#tf.enable_eager_execution()
"""
from app.models.rating  import Rating
from app.models.items   import Item
from app.models.user    import User
from app.models.genre   import Genre
"""
from app.helpers.builder.director import Director
from app.helpers.builder.content_based_builder import ContentBasedBuilder

class ContentBasedV1:

  def __init__(self):
    """
    self.num_recommendations = 2

    self.num_users = User().count()
    self.num_items = Item().count()
    self.num_feats = Genre().count()

    self.users = User().get_usernames()
    self.items = Item().get_item_names()
    self.feats = Genre().get_genres()

    # each row represents a user's rating for the different movies
    self.user_items = Rating().get_user_items()
    
    # features of the movies one-hot encoded
    # e.g. columns could represent ['Action', 'Sci-Fi', 'Comedy', 'Cartoon', 'Drama']
    self.item_feats = Item().get_items_features()

    print(self.user_items)
    """
    pass

  """
  def recommend1(self):

    # user feature matrix
    # matrix containing each user's embedding in the n-dimensional feature space
    users_feats = tf.matmul(self.user_items, self.item_feats) 
    # normalize each user feature vector to sum to 1
    users_feats = users_feats/tf.reduce_sum(users_feats, axis=1, keepdims=True) 


    # Ranking feature relevance for each user
    top_user_features = tf.nn.top_k(users_feats, self.num_feats)[1]

    for i in range(self.num_users):
      feature_names = [self.feats[int(index)] for index in top_user_features[i]]
      print('{}: {}'.format(self.users[i],feature_names))

    # Determining movie recommendations
    users_ratings = tf.matmul(users_feats, tf.transpose(self.item_feats))

    # If a user has already rated a movie, we ignore that rating
    users_ratings_new = tf.where(tf.equal(self.user_items, tf.zeros_like(self.user_items)),
                                    users_ratings,
                                    tf.zeros_like(tf.cast(self.user_items, tf.float32)))


    # Print out the top 2 rated movies for each user
    top_movies = tf.nn.top_k(users_ratings_new, self.num_recommendations)[1]

    recommendations = []

    for i in range(self.num_users):
      item_names = [self.items[index] for index in top_movies[i]]

      data = {}
      data["user"] = self.users[i]
      data["movies"] = item_names
  
      recommendations.append(data)

    return recommendations
    """
   

  def recommend(self):
    
    director = Director()
    content_based_builder = ContentBasedBuilder()

    director.builder = content_based_builder
    return director.recommendation_with_normalization()



