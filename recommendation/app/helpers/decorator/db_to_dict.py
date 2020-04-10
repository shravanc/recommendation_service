from app.helpers.decorator.decorator import Decorator

class DbToDict(Decorator):
  
  def operation(self): #, data, columns):
    collections = []
    for entry in self.component.operation():
      dictionary = {}
      for col in self.data:
        dictionary[col] = getattr(entry, col)
      collections.append(dictionary)
    return collections
