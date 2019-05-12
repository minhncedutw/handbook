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
__date__ = "5/10/2019"
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

import numpy as np
import open3d as op3
from GeneralUtils import Union, path2str, stack_list_horizontal, sample_arrays

#==============================================================================
# Constant Definitions
#==============================================================================

#==============================================================================
# Function Definitions
#==============================================================================
def label_to_color(labels: np.ndarray) -> np.ndarray:
    """
    Convert labels to colors(label's values must be in range [1, 6])
    :param labels: 1D ndarray, list of labels
    :return: ndarray of color codes
    """
    map_label_to_rgb = {
        0: [0, 0, 0], # black
        1: [0, 255, 0], # green
        2: [0, 0, 255], # blue
        3: [255, 0, 0], # red
        4: [255, 0, 255],  # purple
        5: [0, 255, 255],  # cyan
        6: [255, 255, 0],  # yellow
    }
    colors = np.array([map_label_to_rgb[label] for label in labels])
    return colors

def pc_to_points(point_cloud: op3.PointCloud) -> np.ndarray:
    """
    Convert point cloud of Open3D object to numpy array
    :param point_cloud_object: a Open3D object, of point cloud
    :return: a numpy array of points
    """
    coords = np.asarray(point_cloud.points)
    colors = np.asarray(point_cloud.colors)
    return stack_list_horizontal((coords, colors))

def points_to_pc(points: np.ndarray) -> op3.PointCloud:
    """
    Convert point cloud of numpy array to Open3D object
    :param points: a numpy array of points, that describes the point cloud
    :return: a point cloud object of Open3D
    """
    if isinstance(points, op3.PointCloud): point_cloud = points
    else:
        point_cloud = op3.PointCloud()
        point_cloud.points = op3.Vector3dVector(points[:, :3])
        if points.shape[1] > 5:
            point_cloud.colors = op3.Vector3dVector(points[:, 3:6])
    return point_cloud

def coords_colors_to_points(coords: np.ndarray, colors: np.ndarray) -> np.ndarray:
    return stack_list_horizontal(arrs=(coords, colors))

def coords_colors_to_pc(coords: np.ndarray, colors: np.ndarray) -> op3.PointCloud:
    return points_to_pc(points=coords_colors_to_points(coords=coords, colors=colors))

def coords_labels_to_points(coords: np.ndarray, labels: np.ndarray) -> np.ndarray:
    colors = label_to_color(labels=labels)
    return coords_colors_to_points(coords=coords, colors=colors)

def coords_labels_to_pc(coords: np.ndarray, labels: np.ndarray) -> op3.PointCloud:
    colors = label_to_color(labels=labels)
    points = coords_colors_to_points(coords=coords, colors=colors)
    return points_to_pc(points=points)


def load_ply_as_pc(file_path: Union[str, Path]) -> op3.PointCloud:
    """
    Load a point cloud from a .ply file
    :param file_path: a string, path to the .ply file
    :return: a point cloud object of Open3D
    """
    point_cloud = op3.read_point_cloud(filename=path2str(file_path))
    return point_cloud

def load_ply_as_points(file_path: Union[str, Path]) -> np.ndarray:
    """
    Load a point cloud from a .ply file
    :param file_path: a string, path to the .ply file
    :return: an numpy array of points
    """
    point_cloud = load_ply_as_pc(file_path=path2str(file_path))
    return pc_to_points(point_cloud)

def measure_pc_centroid(point_cloud: Union[np.ndarray, op3.PointCloud]):
    """
    Mesure the centroid of point cloud
    :return: a point as an array(each element in array is x, y, z, ...)
    """
    if isinstance(point_cloud, op3.PointCloud):
        points = pc_to_points(point_cloud)
    centroid = np.mean(points, axis=0)
    return centroid

def sample_pc(point_cloud: op3.PointCloud, n_samples:int) -> op3.PointCloud:
    """
    Sample the point cloud
    :param num_samples: an integer, that is the number of points you want to sample
    """
    points = pc_to_points(point_cloud=point_cloud)
    points = sample_arrays(arrs=(points), n_samples=n_samples)
    return points_to_pc(points)

def visualize_pc(*args):
    """
    Visualize of list of point clouds
    :param *args: a list of Open3D objects, that are point clouds
    """
    point_clouds = [points_to_pc(obj) for obj in args]
    op3.draw_geometries([*point_clouds])

#==============================================================================
# Main function
#==============================================================================
def _main_(args):
    print('Hello World! This is {:s}'.format(args.desc))

    # config_path = args.conf
    # with open(config_path) as config_buffer:    
    #     config = json.loads(config_buffer.read())
    pipe_path1 = 'E:/CLOUD/GDrive(t105ag8409)/Projects/ARLab/Point Cloud Robot Grasping/camera/orbbec_astra_s/recorded_data/00094.ply'
    pipe_path2 = 'E:/CLOUD/GDrive(t105ag8409)/Projects/ARLab/Point Cloud Robot Grasping/camera/orbbec_astra_s/recorded_data/00100.ply'
    point_cloud1 = load_ply_as_pc(file_path=pipe_path1)
    points1 = load_ply_as_points(file_path=pipe_path1)
    point_cloud2 = load_ply_as_pc(file_path=pipe_path2)
    visualize_pc(point_cloud2, point_cloud1)
    visualize_pc(point_cloud2, coords_labels_to_points(coords=points1[:, :3], labels=np.ones(len(points1))))


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Your program name!!!')
    argparser.add_argument('-d', '--desc', help='description of the program', default='HANDBOOK')
    # argparser.add_argument('-c', '--conf', default='config.json', help='path to configuration file')

    args = argparser.parse_args()
    _main_(args)
