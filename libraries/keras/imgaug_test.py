'''
    File name: robot-grasping
    Author: minhnc
    Date created(MM/DD/YYYY): 6/18/2018
    Last modified(MM/DD/YYYY HH:MM): 6/18/2018 6:44 AM
    Python Version: 3.5
    Other modules: [tensorflow-gpu 1.3.0]

    Copyright = Copyright (C) 2017 of NGUYEN CONG MINH
    Credits = [None] # people who reported bug fixes, made suggestions, etc. but did not actually write the code
    License = None
    Version = 0.9.0.1
    Maintainer = [None]
    Email = minhnc.edu.tw@gmail.com
    Status = Prototype # "Prototype", "Development", or "Production"
    Code Style: http://web.archive.org/web/20111010053227/http://jaynes.colorado.edu/PythonGuidelines.html#module_formatting
'''

#==============================================================================
# Imported Modules
#==============================================================================
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os.path
import sys
import time

import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np

import cv2

#==============================================================================
# Constant Definitions
#==============================================================================
class CMImageType:
    COLOR = cv2.IMREAD_COLOR
    GRAYSCALE = cv2.IMREAD_GRAYSCALE
    UNCHANGED = cv2.IMREAD_UNCHANGED

class CMColor:
    # Opencv color definition
    RED = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLUE = (255, 0, 0)
    SKY = (255, 255, 0)
    PINK = (255, 0, 255)
    YELLOW = (0, 255, 255)
    WHITE = (255, 255, 255)

PI = np.pi
def DEGREE_2_RADIAN(X):
    return (X * PI / 180)
def RADIAN_2_DEGREE(X):
    return (X*180/PI)
def M_2_MM(X):
    return (X*1000)
def MM_2_M(X):
    return (X/1000.0)
#==============================================================================
# Function Definitions
#==============================================================================
def ask_what_to_do():
    while True:
        yourvar = input('What should do (Take image/Find position/ ?: ')
        print('you entered: ' + yourvar)
        if yourvar == 'g' or yourvar == 'u':
            return yourvar

def load_image(image_file, image_type=CMImageType.UNCHANGED):
    _image = cv2.imread(image_file, image_type)
    if _image is None:
        return False, []
    return True, _image

def show_image(image, windowname=None, wait=None):
    if windowname is None:
        windowname = "Unknown"
    cv2.namedWindow(winname=windowname, flags=cv2.WINDOW_NORMAL)
    cv2.imshow(winname=windowname, mat=image)
    if wait is not None:
        cv2.waitKey(wait)
    return True, []

def plot_rectangle(image, rect_points, edge1_color=CMColor.RED, edge2_color=CMColor.RED, edge3_color=CMColor.RED, edge4_color=CMColor.RED, size=1):
    rect_points = np.array(rect_points).astype(np.int32)
    row1, col1, row2, col2, row3, col3, row4, col4 = rect_points[0, 0], rect_points[0, 1], \
                                                     rect_points[1, 0], rect_points[1, 1], \
                                                     rect_points[2, 0], rect_points[2, 1], \
                                                     rect_points[3, 0], rect_points[3, 1]
    _image = np.copy(image)
    cv2.line(_image, (col1, row1), (col2, row2), edge1_color, size)
    cv2.line(_image, (col2, row2), (col3, row3), edge2_color, size)
    cv2.line(_image, (col3, row3), (col4, row4), edge3_color, size)
    cv2.line(_image, (col4, row4), (col1, row1), edge4_color, size)
    return True, _image


def test_quick_aug(images):
    sequence = iaa.Sequential([iaa.Fliplr(0.5), iaa.GaussianBlur((0, 3.0))])
    images_aug = sequence.augment_images(images)

    show_image(image=images[0], wait=0)
    show_image(image=images_aug[0], wait=0)
    return True, []

def test_heavy_aug(images):
    sometimes = lambda aug: iaa.Sometimes(0.5, aug)
    seq = iaa.Sequential([
        # apply the following augmenters to most images
        iaa.Fliplr(0.5),  # horizontally flip 50% of all images
        iaa.Flipud(0.2),  # vertically flip 20% of all images
        # crop images by -5% to 10% of their height/width
        sometimes(iaa.CropAndPad(
            percent=(-0.05, 0.1),
            pad_mode=ia.ALL,
            pad_cval=(0, 255)
        )),
        sometimes(iaa.Affine(
            scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},  # scale images to 80-120% of their size, individually per axis
            translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},  # translate by -20 to +20 percent (per axis)
            rotate=(-45, 45),  # rotate by -45 to +45 degrees
            shear=(-16, 16),  # shear by -16 to +16 degrees
            order=[0, 1],  # use nearest neighbour or bilinear interpolation (fast)
            cval=(0, 255),  # if mode is constant, use a cval between 0 and 255
            mode=ia.ALL  # use any of scikit-image's warping modes (see 2nd image from the top for examples)
        )),
        # execute 0 to 5 of the following (less important) augmenters per image
        # don't execute all of them, as that would often be way too strong
        iaa.SomeOf((0, 5),
                   [
                       sometimes(iaa.Superpixels(p_replace=(0, 1.0), n_segments=(20, 200))),
                       # convert images into their superpixel representation
                       iaa.OneOf([
                           iaa.GaussianBlur((0, 3.0)),  # blur images with a sigma between 0 and 3.0
                           iaa.AverageBlur(k=(2, 7)),  # blur image using local means with kernel sizes between 2 and 7
                           iaa.MedianBlur(k=(3, 11)),
                           # blur image using local medians with kernel sizes between 2 and 7
                       ]),
                       iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5)),  # sharpen images
                       iaa.Emboss(alpha=(0, 1.0), strength=(0, 2.0)),  # emboss images
                       # search either for all edges or for directed edges,
                       # blend the result with the original image using a blobby mask
                       iaa.SimplexNoiseAlpha(iaa.OneOf([
                           iaa.EdgeDetect(alpha=(0.5, 1.0)),
                           iaa.DirectedEdgeDetect(alpha=(0.5, 1.0), direction=(0.0, 1.0)),
                       ])),
                       iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05 * 255), per_channel=0.5),
                       # add gaussian noise to images
                       iaa.OneOf([
                           iaa.Dropout((0.01, 0.1), per_channel=0.5),  # randomly remove up to 10% of the pixels
                           iaa.CoarseDropout((0.03, 0.15), size_percent=(0.02, 0.05), per_channel=0.2),
                       ]),
                       iaa.Invert(0.05, per_channel=True),  # invert color channels
                       iaa.Add((-10, 10), per_channel=0.5),
                       # change brightness of images (by -10 to 10 of original value)
                       iaa.AddToHueAndSaturation((-20, 20)),  # change hue and saturation
                       # either change the brightness of the whole image (sometimes
                       # per channel) or change the brightness of subareas
                       iaa.OneOf([
                           iaa.Multiply((0.5, 1.5), per_channel=0.5),
                           iaa.FrequencyNoiseAlpha(
                               exponent=(-4, 0),
                               first=iaa.Multiply((0.5, 1.5), per_channel=True),
                               second=iaa.ContrastNormalization((0.5, 2.0))
                           )
                       ]),
                       iaa.ContrastNormalization((0.5, 2.0), per_channel=0.5),  # improve or worsen the contrast
                       iaa.Grayscale(alpha=(0.0, 1.0)),
                       sometimes(iaa.ElasticTransformation(alpha=(0.5, 3.5), sigma=0.25)),
                       # move pixels locally around (with random strengths)
                       sometimes(iaa.PiecewiseAffine(scale=(0.01, 0.05))),  # sometimes move parts of the image around
                       sometimes(iaa.PerspectiveTransform(scale=(0.01, 0.1)))
                   ],
                   random_order=True
                   )
    ], random_order=True)

    images_aug = seq.augment_images(images)

    show_image(image=images[0], wait=0)
    show_image(image=images_aug[0], wait=0)

    return True, []

#==============================================================================
# Main function
#==============================================================================
def main(argv=None):
    print('Hello! This is XXXXXX Program')

    _, images = load_image('cat.jpg', image_type=CMImageType.UNCHANGED)
    images = np.expand_dims(images, axis=0)

    test_heavy_aug(images)

if __name__ == '__main__':
    main()
