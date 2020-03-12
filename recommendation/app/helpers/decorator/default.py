from app.helpers.decorator.data_processing import DataProcessing
class Default(DataProcessing):
  
  def __init__(self, items):
    self.data = items

  def operation(self):
    print("----inside-default----", self.data)
    return self.data
