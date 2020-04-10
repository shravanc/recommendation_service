from abc import ABC, abstractmethod, abstractproperty
from typing import Any



class Recommender:
  
  @abstractproperty
  def product(self):
    pass

  @abstractproperty
  def users_features(self):
    pass

  @abstractproperty
  def rank_feature_relevance(self):
    pass

  @abstractproperty
  def user_ratings(self):
    pass

  @abstractproperty
  def normalization(self):
    pass

  @abstractproperty
  def recommendation(self):
    pass

  @abstractproperty
  def format_recommendation(self):
    pass

