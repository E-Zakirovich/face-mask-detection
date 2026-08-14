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
    def __init__(self, xml_path : str, labels : str, classes : list, class_to_idx : dict, verbose : bool):
        self.xml_path = xml_path
        self.classes = classes
        self.class_to_id = class_to_idx
        self.labels = labels
        self.verbose = verbose

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

        # convert coordinate variables into integer variables
        img_width = int(width_text)
        img_height = int(height_text)

        # I need a list to store results
        lines = []

        # I need a loop to look each elements inside .xml file
        for obj in root.findall("object"):
            class_name = obj.find("name").text.strip()

            # identification of class id
            if class_name not in self.class_to_id:
                print(f"  [skip] Missing class {class_name}")
                continue
            class_id = self.class_to_id[class_name]

            # get bounding box part
            bounding_box = obj.find("bndbox")
            if bounding_box is None:
                print(f"  [skip] Missing <{bounding_box}> element in {xml_path}")
                return False

            # bounding box settings
            x_min = bounding_box.find("xmin")
            y_min = bounding_box.find("ymin")
            x_max = bounding_box.find("xmax")
            y_max = bounding_box.find("ymax")

            # checking bounding box elements the elements
            x_min = x_min.text if x_min is not None else None
            y_min = y_min.text if y_min is not None else None
            x_max = x_max.text if x_max is not None else None
            y_max = y_max.text if y_max is not None else None

            # convert bounding box coordinates to float value
            x_minimum = float(x_min) if x_min is not None else None
            y_minimum = float(y_min) if y_min is not None else None
            x_maximum = float(x_max) if x_max is not None else None
            y_maximum = float(y_max) if y_max is not None else None


            # Guard against any missing coordinates
            if (
                    x_minimum is None
                    or y_minimum is None
                    or x_maximum is None
                    or y_maximum is None
            ):
                continue

            # Make sure box dimensions are valid
            if x_maximum <= x_minimum or y_maximum <= y_minimum:
                print(f"  [skip] Invalid bounding box in {self.xml_path}")
                continue

            # Get centers
            x_center = (x_minimum + x_maximum) / 2 / img_width
            y_center = (y_minimum + y_maximum) / 2 / img_height
            width = (x_maximum - x_minimum) / img_width
            height = (y_maximum - y_minimum) / img_height

            # get the final bounding boxes
            lines.append(f"{class_id} {x_center} {y_center} {width} {height}")

        # final check for lines list
        if not lines:
            print(f"  [skip] Missing <{lines}> element in {self.xml_path}")
            return False

        # make new name for new file
        base_name = os.path.splitext(os.path.basename(self.xml_path))[0]
        out_path = os.path.join(self.labels, base_name + ".txt")

        # store new file to out_path
        with open(out_path, "w") as f:
            f.write("\n".join(lines))

        return True

    """
    __convertor() method will help me to read only one file, i need a method
    that can read multiple files using _convertor(). So I created new method 
    called convert.
    """
    def convert(self):

        self.verbose = True
        annotations_path = self.xml_path # path of annotations
        os.makedirs(self.xml_path, exist_ok=True) # making a path for annotations

        # here I am storing all path of .xml file inside of annotations_path which is actually ends with .xml!
        xml_files = [f for f in os.listdir(annotations_path) if f.endswith(".xml")]

        # check the number of .xml files
        if self.verbose:
            print(f"Found {len(xml_files)} xml files in {annotations_path}")

        converted = 0
        skipped = 0

        # read all data from annotations and store them with .txt file extension
        for file in xml_files:
            path = os.path.join(annotations_path, file)

            # I used try catch to avoid stop the program when there is a static error
            try:
                convert = self.__convertor() #
                if convert:
                    converted += 1
                else:
                    skipped += 1

            except Exception as e:
                print(f"  [skip] {e}")
                skipped += 1

        # show final result
        if self.verbose:
            print(f"Converted {converted} xml files in {annotations_path}")

        return converted, skipped