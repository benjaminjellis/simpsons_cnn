import pandas as pd
from shutil import copyfile
from os.path import exists
from os import mkdir


annotation = pd.read_csv("data/annotation.txt", header = None)

list_of_files = annotation[0].tolist()

for file in list_of_files:
    fp_els = file.split("/")
    loc_from = "data/raw/" + fp_els[2] + "/" + fp_els[3]
    if not exists("data/bounding_data/"):
        mkdir("data/bounding_data/")
    if not exists("data/bounding_data/" + fp_els[2] ):
        mkdir("data/bounding_data/" + fp_els[2] )
    loc_to = "data/bounding_data/" + fp_els[2] + "/" + fp_els[3]
    copyfile(loc_from, loc_to)