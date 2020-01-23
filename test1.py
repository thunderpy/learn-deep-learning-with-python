# Loading the MNIST dataset in Keras


"""
from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

>>> train_images.shape
(60000, 28, 28)
>>> len(train_labels)
60000
>>> train_labels
array([5, 0, 4, ..., 5, 6, 8], dtype=uint8)
And here’s the test data:
>>> test_images.shape
(10000, 28, 28)
>>> len(test_labels)
10000
>>> test_labels
array([7, 2, 1, ..., 4, 5, 6], dtype=uint8)
"""
