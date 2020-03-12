import tensorflow as tf
from app.helpers.decorator.decorator import Decorator

class ArrayToTensor(Decorator):
  def operation(self, data, keys=None):
    return tf.constant(data, dtype=tf.float32)
