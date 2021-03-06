#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : May-09-20 19:58
# @Author  : Kelly Hwong (you@example.org)
# @RefLink    : https://keras.io/examples/mnist_cnn/


import os
import keras
import tensorflow as tf
from tensorflow.keras.datasets.mnist import load_data


def main():
    (x_train, y_train), (x_test, y_test) = load_data(path="mnist.npz")
    print(y_train.shape)

    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255.0
    x_test /= 255.0
    print('x_train shape:', x_train.shape)
    print(x_train.shape[0], 'train samples')
    print(x_test.shape[0], 'test samples')

    num_classes = 10
    # convert class vectors to binary class matrices
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)


if __name__ == "__main__":
    main()
