# directories
annotations_path = "data/annotations"
labels_path = "data/labels"
data_yaml_path = "data/dataset.yaml"

# class order -> integer id (must match dataset.yaml)
classes = ["with_mask", "without_mask", "mask_weared_incorrect"]
class_to_id = {name: i for i, name in enumerate(classes)}

# train settings
model_path = "yolov8n.pt"
epochs = 50
image_size = 640

# misc
verbose = True