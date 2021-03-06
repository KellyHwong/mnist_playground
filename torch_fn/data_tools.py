#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Apr-16-20 08:24
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import json
import numpy as np
from torchvision import datasets, transforms
import torch
import torchvision

import matplotlib.pyplot as plt


def main():
    """ Load Config """
    with open('./config.json', 'r') as f:
        CONFIG = json.load(f)
    DATASETS_DIR = CONFIG["DATASETS_DIR"]
    BATCH_SIZE = CONFIG["BATCH_SIZE"]

    data_train = datasets.MNIST(root=DATASETS_DIR, train=True, download=True)
    data_test = datasets.MNIST(root=DATASETS_DIR, train=False, download=True)

    data_loader_train = torch.utils.data.DataLoader(dataset=data_train,
                                                    batch_size=BATCH_SIZE,
                                                    shuffle=True)
    data_loader_test = torch.utils.data.DataLoader(dataset=data_test,
                                                   batch_size=BATCH_SIZE,
                                                   shuffle=True)

    for i in range(100):
        data, label = data_train[i]
        print(data)  # PIL.Image.Image
        # print(data.mode)  # mode L
        print(label)
        data = np.asarray(data)
        print(data.shape)
        print(np.max(data))  # 255
        plt.imshow(data, cmap="gray")
        plt.show()
        # input()


if __name__ == "__main__":
    main()
