import tensorflow as tf

class Recommendation():
  def __init__(self, users_ratings, num_recommendations, num_users, items, users):
    self.users_ratings       = users_ratings
    self.num_recommendations = num_recommendations

    self.top_movies = None
    self.recommendations = None
    self.num_users  = num_users
    self.items      = items
    self.users      = users

  def evaluate(self):
    self.top_movies = tf.nn.top_k(self.users_ratings, self.num_recommendations)[1]

    self.recommendations = []

    for i in range(self.num_users):
      item_names = [self.items[index] for index in self.top_movies[i]]

      data = {}
      data["user"] = self.users[i]
      data["movies"] = item_names

      self.recommendations.append(data)


    print("Recommendation---->", self.recommendations)
    return self.recommendations
