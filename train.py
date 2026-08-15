"""
train.py
~~~~~~~~~

I need to teach YOLO(You Only Look Once) with sth, so I created
train.py file. I will train my model with dataset in main.py.
"""

import torchvision
from ultralytics import YOLO
import argparse
import os
import yaml


class Train:
    def __init__(self):
        ...