from abc import ABC, abstractmethod


class RecommendationEngine:
  
  @abstractmethod
  def get_engine(self):
    pass

  def recommend_movies(self, engine_type):

    engine = self.get_engine(engine_type)
    
    return engine.recommend()

