"""
annotations.py
~~~~~~~~~~~~~~~

YOLO(You Only Look Once) works for .txt files, it does not
work like data pipeline as before. So  I made this file to
make new folder and store all annotations  inside other of
another folder.
"""

# import libraries
import os
import xml.etree.ElementTree as Et


class Annotations:
    def __init__(self, xml_path : str, labels : str, classes : list, class_to_idx : dict):
        self.xml_path = xml_path
        self.classes = classes
        self.class_to_idx = class_to_idx
        self.labels = labels

    def __convertor(self):
        tree = Et.parse(self.xml_path)
        root = tree.getroot()

        # size settings
        size = root.find("size")
        if size is None:
            print(f"  [skip] Missing <{size}> element in {xml_path}")
            return False

        width_elem = size.find("width")
        height_elem = size.find("height")

        # Get string values directly into local variables
        width_text = width_elem.text if width_elem is not None else None
        height_text = height_elem.text if height_elem is not None else None

        if not width_text or not height_text:
            print(f"  [skip] Missing width/height values in {xml_path}")
            return False

        # PyCharm now knows width_text and height_text are non-None strings
        img_width = int(width_text)
        img_height = int(height_text)

        # I need a list to store results
        lines = []

        # I need a loop to look each elements inside .xml file
        for obj in root.findall("object"):
            ...
        
        return True


    def convert(self):
        ...