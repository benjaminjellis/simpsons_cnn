from PIL import Image, ImageDraw
import pandas as pd
import numpy as np
import torch
import torchvision.transforms.functional as FT
from numpy import round


def resize(image, boxes, dims = (300, 300), return_percent_coords = True):
    """
    Resize image. For the SSD300, resize to (300, 300).
    Since percent/fractional coordinates are calculated for the bounding boxes (w.r.t image dimensions) in this process,
    you may choose to retain them.
    :param image: image, a PIL Image
    :param boxes: bounding boxes in boundary coordinates, a tensor of dimensions (n_objects, 4)
    :return: resized image, updated bounding box coordinates (or fractional coordinates, in which case they remain the same)
    """
    # Resize image
    new_image = FT.resize(image, dims)

    # Resize bounding boxes
    old_dims = torch.FloatTensor([image.width, image.height, image.width, image.height]).unsqueeze(0)
    new_boxes = boxes / old_dims  # percent coordinates

    if not return_percent_coords:
        new_dims = torch.FloatTensor([dims[1], dims[0], dims[1], dims[0]]).unsqueeze(0)
        new_boxes = new_boxes * new_dims
        new_boxes = torch.round(new_boxes)

    return new_image, new_boxes


def get_bounding_detials_for_image(image_path):
    annotations = pd.read_csv("data/annotation.txt", header = None)
    all_image_paths = annotations[0].tolist()
    x_0s = annotations[1].tolist()
    y_0s = annotations[2].tolist()
    x_1s = annotations[3].tolist()
    y_1s = annotations[4].tolist()
    labels = annotations[5].tolist()
    index = all_image_paths.index(image_path)
    return x_0s[index], y_0s[index], x_1s[index], y_1s[index], labels[index]


test_im_path = "data/bounding_data/ned_flanders/pic_1206.jpg"
base = Image.open(test_im_path)
bounding_details = get_bounding_detials_for_image(test_im_path)

test = [bounding_details[0], bounding_details[1], bounding_details[2], bounding_details[3]]
test = torch.FloatTensor(test)
new_im, new_boxes = resize(base, boxes = test, return_percent_coords = True)
a = new_boxes.numpy().squeeze().tolist()
print(a[2])
print(new_im.size[1])
b = [a[0]*new_im.size[0], a[1]*new_im.size[1], a[2]*new_im.size[0], a[3]*new_im.size[1]]
print(b)
draw_obj = ImageDraw.Draw(new_im)
draw_obj.rectangle(b, outline = "red")
new_im.show()