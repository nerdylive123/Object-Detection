import cv2
import time
import os
import numpy as np
import tensorflow as tf

from tensorflow.python.keras.utils.data_utils import get_file


class Detection:
    def __init__(self):
        self.colorList = None
        self.classList = None

    def read_class(self, ClassFileAt):
        with open(ClassFileAt, 'rb') as f:
            self.classList = f.read().splitlines()
        self.colorList = np.random.uniform(low=0, high=255, size=(len(self.classList), 3))
        print(len(self.classList), len(self.colorList))

    def download_model(self, model_url):

