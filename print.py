# pip install numpy pandas scikit-learn tensorflow keras torch maplotlib
import numpy as np
#import pandas as pandas
import sklearn as sklearn
#import tensorflow as tensorflow
#import torch as torch
#import matplotlib as matplotlib

array = [1,2,3]

np_array = np.array(array)

print(type(np_array))

print("The program works.")

from sklearn.datasets import load_iris
iris_dataset = load_iris()

print("Keys of iris dataset: \n{}".format(iris_dataset.keys()))

print(iris_dataset['DESCR'][:193] + "\n...")

print("Target names: {}".format(iris_dataset['target_names']))

print("Feature names: \n{}".format(iris_dataset['feature_names']))

print("Type of data: {}".format(type(iris_dataset['data'])))

print("Shape of data: {}".format(iris_dataset['data'].shape))

print("First five columns of data:\n{}".format(iris_dataset['data'][:5]))