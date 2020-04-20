from app.helpers.builder.director import Director
from app.helpers.builder.content_based_builder import ContentBasedBuilder

class ContentBasedV1:

  def __init__(self):
    self.director = Director()
    self.director.builder = ContentBasedBuilder()

  def recommend(self):
    return self.director.recommendation_with_normalization()

