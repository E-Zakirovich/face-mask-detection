"""
main.py

I am going to use this file to train  a model. This file
will use  load data  pipeline and will make a .txt files
for YOLO  (You Only Look Once). After that  I will Train
class to train v8 nano model with .txt values and images
"""

# import classes
# from annotations import Annotations
from train import Train
from configs import configs

# annotations = Annotations(
#     xml_path = configs.annotations_path,
#     labels = configs.labels_path,
#     classes = configs.classes,
#     class_to_id = configs.class_to_id,
#     verbose = configs.verbose
# )
#
# annotations.convert()

train = Train(
    data_yaml = configs.data_yaml_path,
    model_path = configs.model_path,
    epochs = configs.epochs,
    image_size = configs.image_size,
    verbose = configs.verbose,
)

train.train()
