from app.helpers.decorator.decorator import Decorator

class DbToDict(Decorator):
  
  def operation(self): #, data, columns):
    #print("debug****>", self.component.operation())
    print("data******>", self.data)
    collections = []
    for entry in self.component.operation():
      dictionary = {}
      for col in self.data:
        dictionary[col] = getattr(entry, col)
      print("dict--->", dictionary)
      collections.append(dictionary)
    return collections
