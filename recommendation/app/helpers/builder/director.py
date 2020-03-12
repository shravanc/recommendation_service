class Director:
  def __init__(self):
    self._builder = None

  @property
  def builder(self):
    return self._builder

  @builder.setter
  def builder(self, builder):
    self._builder = builder

  def recommendation_with_normalization(self):
    self.builder.users_features()
    self.builder.rank_feature_relevance()
    self.builder.user_ratings()
    self.builder.normalization()
    self.builder.recommendation()
    return self.builder.format_recommendation()

  def recommendation_without_normalization():
    self.builder.users_features()
    self.builder.rank_feature_relevance()
    self.builder.user_ratings()
    self.builder.recommendation()
    return self.builder.format_recommendation()



