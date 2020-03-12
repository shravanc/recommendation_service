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
    self._product.evaluate_users_features()

  def rank_feature_relevance(self):
    self._product.evaluate_rank_feature_relevance()

  def user_ratings(self):
    self._product.evaluate_user_ratings()

  def normalization(self):
    self._product.evaluate_normalization()

  def recommendation(self):
    self._product.evaluate_recommendation()

  def format_recommendation(self):
    return self._product.format_recommendation()




