from app.helpers.builder.recommender import Recommender
from app.helpers.builder.genre_based import GenreBased

class ContentBasedBuilder(Recommender):

  def __init__(self):
    self.reset()

  def reset(self):
    self._product = GenreBased()

  @property
  def product(self):
    product = self._product
    self.reset()
    return product

  def users_features(self):
    self._product.evaluate( 'users_features' )

  def rank_feature_relevance(self):
    self._product.evaluate( 'rank_feature_relevance' )

  def user_ratings(self):
    self._product.evaluate( 'user_ratings' )

  def normalization(self):
    self._product.evaluate( 'normalization' )

  def recommendation(self):
    self._product.evaluate( 'recommendation' )

  def format_recommendation(self):
    return self._product.evaluate( 'format_recommendation' )


