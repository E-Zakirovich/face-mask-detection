"""
annotations.py
~~~~~~~~~~~~~~~

YOLO(You Only Look Once) works for .txt files, it does not
work like data pipeline as before. So  I made this file to
make new folder and store all annotations  inside other of
another folder.
"""

import os


class Annotations:
    def __init__(self, xml_path : str, classes : list, class_to_idx : dict):
        self.xml_path = xml_path
        self.classes = classes
        self.class_to_idx = class_to_idx