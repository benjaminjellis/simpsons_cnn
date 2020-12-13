# simpsons_cv

This is a quick project to explore computer vision using a [dataset of Simpsons characters.](https://www.kaggle.com/alexattia/the-simpsons-characters-dataset)

## Simple Classifier
First experiment is a simple classifier of images where only one character is present. I built a custom dataset where each character class contains 700 images. I utilised the kaggle dataset (linked above) and over / under sampled where aprropriate. 

The results from this can be found in [simple_classification/classifier.ipynb](https://github.com/benjaminjellis/simpsons_cnn/blob/master/simple_classifer/classifier.ipynb)

## Object Detection
Faster R-CNN (pretrained) to draw bounding boxes around characters. 

The results from this can be found in [object_detection/evaluation.ipynb](https://github.com/benjaminjellis/simpsons_cv/blob/master/object_detection/evaluation.ipynb)

Some validation images can be found [here](https://github.com/benjaminjellis/simpsons_cv/tree/master/object_detection/validation_images). Where green boxes and text are predictions and red boxes are the ground truth boxes. 
