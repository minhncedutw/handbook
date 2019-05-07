#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Description
'''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__author__ = "CONG-MINH NGUYEN"
__copyright__ = "Copyright (C) 2019, HANDBOOK"
__credits__ = ["CONG-MINH NGUYEN"]
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "5/5/2019"
__maintainer__ = "CONG-MINH NGUYEN"
__email__ = "minhnc.edu.tw@gmail.com"
__status__ = "Development"  # ["Prototype", "Development", or "Production"]
# Project Style: https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6
# Code Style: http://web.archive.org/web/20111010053227/http://jaynes.colorado.edu/PythonGuidelines.html#module_formatting

#==============================================================================
# Imported Modules
#==============================================================================
import argparse
from pathlib import Path
import os.path
import sys
import time

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = ""  # The GPU id to use, usually either "0" or "1"

import numpy as np

#==============================================================================
# Constant Definitions
#==============================================================================

#==============================================================================
# Function Definitions
#==============================================================================
def makedir(path, mode=0o777, parents=True, exist_ok=True):
    """
    Description:
    :param path: [Path, str], path
    :param mode: [0o777, 0o444, ...], chmod(refer: https://help.ubuntu.com/community/FilePermissions)
    :param parents: [Path, str], True: if path is relative & False: if path is absolute
    :param exist_ok: boolean, if path already exists, True: force overwrite & False: raise error
    :return: TYPE, MEAN
    """
    Path(path).mkdir(mode=mode, parents=parents, exist_ok=exist_ok)


def onehot_encoding(labels, n_classes):
    """
    Description: convert integer labels to one hot
    :param labels: an [int, ndarray], a label array of shape (d0, d1, d2, ...dn)
    :param n_classes: an int, number of classes
    :return: [ndarray], an one hot array of shape (d0, d1, ...dn, n_classes)
    """
    onehot = np.identity(n_classes)[labels]
    return onehot


def onehot_decoding(probs, class_axis):
    """
    Description: convert one-hot encoding to labels
    :param probs: [ndarray], an probability array, one-hot-encoding type of shape (d0, d1, ...dn)
    :param class_axis: int, axis of classes in 'probs' array(0 <= class_axis <= n)
    :return: [int, ndarray], an label array of shape (d0, d1, ...dn-1)
    """
    labels = np.argmax(np.asarray(probs), axis=class_axis)
    return labels


def _sigmoid(x):
    return 1. / (1. + np.exp(-x))


def _softmax(x, axis=-1, t=-100.):
    x = x - np.max(x)

    if np.min(x) < t:
        x = x / np.min(x) * t

    e_x = np.exp(x)

    return e_x / e_x.sum(axis, keepdims=True)



#==============================================================================
# Main function
#==============================================================================
def _main_(args):
    print('Hello World! This is {:s}'.format(args.desc))

    # config_path = args.conf
    # with open(config_path) as config_buffer:    
    #     config = json.loads(config_buffer.read())




if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='General utils')
    argparser.add_argument('-d', '--desc', help='description of the program', default='utils')
    # argparser.add_argument('-c', '--conf', default='config.json', help='path to configuration file')

    args = argparser.parse_args()
    _main_(args)
