from abc import ABC, abstractmethod, abstractproperty
from typing import Any



class Recommender:
  
  @abstractproperty
  def product(self):
    pass

  @abstractproperty
  def product_part_a(self):
    pass

  @abstractproperty
  def product_part_b(self):
    pass

  @abstractproperty
  def product_part_c(self):
    pass

