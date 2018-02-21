from PIL import Image
import os
import pandas as pd
import numpy as np



## defineing the directory of data set

root = '/Users/sharath/Desktop/Datascience/officeimages'

directoryamazon = root + "/amazon"

directorydslr = root + "/dslr"

directoryweb = root + "/webcam"

print directoryamazon

def get_image_list(dic):
    image_list = []
    image_label = []
    for root, dirs, files in os.walk(dic):
        for file in files:
            if file.endswith('.jpg'):
                # print file
                temp = str(root).split('/')
                label = temp[-1]
                im = Image.open(root + '/' + file)

                ### changing images to numpy array varialbe
                imagedata = np.array(im)
                image_list.append(imagedata)
                image_label.append(label)

    ## returing the appended list
    return image_list, image_label



## load images from the directory

## get amazon images
trainamazon, amazonlabel = get_image_list(directoryamazon)

## get dslr images
traindslr, dslrlabel = get_image_list(directorydslr)

## get webcam images
trainweb, weblabel = get_image_list(directoryweb)

