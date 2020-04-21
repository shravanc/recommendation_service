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
    self._builder.users_features()
    self._builder.rank_feature_relevance()
    self._builder.user_ratings()
    self._builder.normalization()
    self._builder.recommendation()
    return self._builder._product.evaluate()
    #return self._builder.format_recommendation()

  def recommendation_without_normalization():
    self._builder.users_features()
    self._builder.rank_feature_relevance()
    self._builder.user_ratings()
    self._builder.recommendation()
    return self._builder.format_recommendation()



