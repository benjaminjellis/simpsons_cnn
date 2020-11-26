"""
Script to create a new dataset that over-samples underrepresented classes. This is intended to be used for simple image
classification
"""

import os
from os import listdir, mkdir
from os.path import isdir, isfile, join, split, splitext, exists
from random import sample
from shutil import copyfile
from math import ceil

data_dir = "data/raw/"

# how many images for each class
class_upper_limit = 700

# list the directories inside the data_dir
only_dirs = [data_dir + d + "/" for d in listdir(data_dir) if isdir(join(data_dir, d))]

# loop through these directories
for a_directory in only_dirs:
    print(a_directory)
    # get a list of all files in each directory
    files_in_a_directory = [a_directory + f for f in listdir(a_directory) if isfile(join(a_directory, f))]
    # count the number of files
    num_files_in_a_directory = len(files_in_a_directory)
    print(num_files_in_a_directory)
    if num_files_in_a_directory > class_upper_limit:
        # if there are more than 1000 under-sample
        files_to_move = sample(files_in_a_directory, class_upper_limit)
    else:
        # if there are less than 700 over-sample
        # find how many images we need to have
        delta = 1000 - num_files_in_a_directory
        # if we don't have enoughh files to sample from we need to duplicate our list so that it's large
        # enough to sample from
        multiplier = ceil(delta / num_files_in_a_directory)
        multiplier = range(multiplier + 1 )
        files_to_move = [val for val in files_in_a_directory for _ in multiplier]
        files_to_move = sample(files_to_move, class_upper_limit)
        # move the files

    count = 0
    out_loc = "data/classifier_data/"
    if not exists(out_loc):
        mkdir(out_loc)
    for a_file in files_to_move:
        fp_els = a_file.split("/")
        dir_for_file = out_loc + fp_els[2] + "/"
        if not exists(dir_for_file):
            mkdir(dir_for_file)
        ext = splitext(a_file)
        copyfile(a_file, dir_for_file + "pic_" + str(count) + ext[1])
        count += 1

