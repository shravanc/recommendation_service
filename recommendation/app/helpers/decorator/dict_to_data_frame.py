from app.helpers.decorator.decorator import Decorator
import pandas as pd

class DictToDataFrame(Decorator):

  def operation(self): #, data, x=None):
    print("----inside-DictToDataFrame----", self.component)
    #print("debug****>", self.component.operation())
    return pd.DataFrame(self.component.operation())
