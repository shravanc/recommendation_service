from app.helpers.recommendation_engine import RecommendationEngine
from app.helpers.content_based_v1 import ContentBasedV1

class MovieRecommendation(RecommendationEngine):

  def get_engine(self, engine_type):
    if engine_type == 'content_based':
      return ContentBasedV1()
    elif engine_type == 'collaborative':
      return CollaborativeV1()
    elif engine_type == "hybrid":
      return HybridV1()

    return ContentBasedV1()  
