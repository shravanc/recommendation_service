from app.helpers.decorator.data_processing import DataProcessing

class Decorator(DataProcessing):
  _component: DataProcessing = None

  def __init__(self, component: DataProcessing, data=None, var=None):
    self._component = component
    self.data = data
    self.var = var

  @property
  def component(self):
    return self._component

  def operation(self):
    self._component.operation()
