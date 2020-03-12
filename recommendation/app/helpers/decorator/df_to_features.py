from app.helpers.decorator.decorator import Decorator

class DFToFeatures(Decorator):

  def operation(self): #, data, number_of_features):
    print("----inside-DFToFeatures----", self.component)
    df = self.component.operation()
    features = []
    for index, item in df.iterrows():
      onehot = [0] * self.data #number_of_features
      for i in item.genres:
        onehot[i-1] = 1
      features.append(onehot)

    return features
