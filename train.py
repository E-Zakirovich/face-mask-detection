"""
train.py
~~~~~~~~~

I need to teach YOLO(You Only Look Once) with sth, so I created
train.py file. I will train my model with dataset in main.py.
"""

from ultralytics import YOLO


class Train:
    def __init__(self, data_yaml : str, model_path : str, epochs : int, image_size: int, verbose : bool = True):
        self.data_yaml = data_yaml
        self.model_path = model_path
        self.epochs = epochs
        self.image_size = image_size
        self.verbose = verbose
        self.model = None

    def load_model(self):
        ...

    def train(self):
        ...