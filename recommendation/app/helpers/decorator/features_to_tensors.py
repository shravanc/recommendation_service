from app.helpers.decorator.decorator import Decorator
import tensorflow as tf

class FeaturesToTensor(Decorator):

  def operation(self): #, features, x=None):
    print("---inside-FeaturesToTensor----", self.component)
    return tf.constant(self.component.operation(), dtype=tf.float32)
