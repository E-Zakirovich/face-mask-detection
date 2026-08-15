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

    """
    load model method will help me to load YOLO model
    without  trouble. First it will check  the status
    and then will help me to load it.
    
    I used encapsulation method in order to hide some 
    methods.
    """
    def __load_model(self):
        if self.model_path:
            print("Loading YOLO model...")
        self.model = YOLO.load_model(self.model_path)

    """
    following method will help me to train my model.
    I also used encapsulation method in order to for 
    safety.
    """
    def __train(self):

        if self.verbose:
            print("Training is started...")

            # training YOLO model
            results = self.model.train(
                dataset=self.data_yaml, # yaml dataset to find the data
                epochs=self.epochs, # the number of epochs
                image_size=self.image_size, # the size of the image
            )

            print("Training is finished...")

            return results # final results are sent to main

        return None

    """
    I created new public method, it will load __train() method
    and send it to main. 
    """
    def train(self):
        result = self.__train()
        return result