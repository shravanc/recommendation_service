from app.models.rating  import Rating
from app.models.items   import Item
from app.models.user    import User
from app.models.genre   import Genre


from app.helpers.builder.user_feature           import UserFeature
from app.helpers.builder.rank_feature_relevance import RankFeatureRelevance
from app.helpers.builder.user_rating            import UserRating
from app.helpers.builder.normalization          import Normalization
from app.helpers.builder.recommendation         import Recommendation


class GenreBased():

  def __init__(self):
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

    self.parts              = []
    self.users_feats        = None
    self.top_user_features  = None
    self.users_ratings      = None
    self.users_ratings_new  = None
    self.recommendation     = None

  def add(self, parts):
    self.parts.append(parts)

  def evaluate(self):
    import sys
    for part in self.parts:
      getattr(self, f"_evaluate_{part}")()

    return self.recommendation

  def evaluate1(self, arg):
    import sys
    return getattr(self, f"_evaluate_{arg}")()



  # private methods

  def _evaluate_users_features(self):
    self.users_feats = UserFeature(self.user_items,
                                   self.item_feats).evaluate()

  def _evaluate_rank_feature_relevance(self):
    self.top_user_features = RankFeatureRelevance(self.users_feats, 
                                                  self.num_feats, 
                                                  self.num_users, 
                                                  self.feats, 
                                                  self.users).evaluate()

  def _evaluate_user_ratings(self):
    self.users_ratings = UserRating(self.users_feats,
                                    self.item_feats).evaluate()

  def _evaluate_normalization(self):
    self.users_ratings = Normalization(self.user_items, 
                                       self.users_ratings).evaluate()

  def _evaluate_recommendation(self):
    self.recommendation = Recommendation(self.users_ratings, 
                                         self.num_recommendations, 
                                         self.num_users, 
                                         self.items, 
                                         self.users).evaluate()

  def _evaluate_format_recommendation(self):
    return self.recommendation

