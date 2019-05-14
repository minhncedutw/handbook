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
import copy

import numpy as np
import open3d as op3
from GeneralUtils import Union, Tuple, path2str, stack_list_horizontal, sample_arrays

#==============================================================================
# Constant Definitions
#==============================================================================
one_divided_pi = 1. / np.pi
one_divided_180 = 1. / 180
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
    
def visualize_registration(source: op3.PointCloud, target: op3.PointCloud, transformation: np.ndarray=np.eye(4)) -> None:
    """
    Visualize the matching performance of source on target through transformation
    Default transformation is I(it means no transform)
    :param num_samples: an integer, that is the number of points you want to sample
    :return: a point as an array(each element in array is x, y, z, ...)
    """
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0, 0]) # source point cloud: red
    target_temp.paint_uniform_color([0, 0, 1]) # target point cloud: blue
    source_temp.transform(transformation)
    visualize_pc(source_temp, target_temp)
    
def sample_point_cloud_feature(point_cloud: op3.PointCloud, voxel_size: float, verbose=False):
    """
    Down sample and sample the point cloud feature
    :param point_cloud: an object of Open3D
    :param voxel_size: a float value, that is how sparse you want the sample points is
    :param verbose: a boolean value, display notification and visualization when True and no notification when False
    :return: 2 objects of Open3D, that are down-sampled point cloud and point cloud feature fpfh
    """
    if verbose: print(":: Downsample with a voxel size %.3f." % voxel_size)
    point_cloud_down_sample = op3.voxel_down_sample(point_cloud, voxel_size)

    radius_normal = voxel_size * 2
    if verbose: print(":: Estimate normal with search radius %.3f." % radius_normal)
    op3.estimate_normals(point_cloud_down_sample, op3.KDTreeSearchParamHybrid(radius=radius_normal, max_nn=30))

    radius_feature = voxel_size * 5
    if verbose: print(":: Compute FPFH feature with search radius %.3f." % radius_feature)
    point_cloud_fpfh = op3.compute_fpfh_feature(point_cloud_down_sample, op3.KDTreeSearchParamHybrid(radius=radius_feature, max_nn=100))
    return point_cloud_down_sample, point_cloud_fpfh

def execute_global_registration(source_down: op3.PointCloud, target_down: op3.PointCloud, 
                                source_fpfh: op3.PointCloud, target_fpfh: op3.PointCloud, 
                                voxel_size: float, verbose=False):
    """
    Do global matching, find gross transformation form source to target
    :param source_down, target_down: 2 objects of Open3D, that are point clouds of source and target after down-sampling
    :param source_fpfh, target_fpfh: 2 objects of Open3D, that are point cloud features of source and target
    :param voxel_size: a float value, that is how sparse you want the sample points is
    :param verbose: a boolean value, display notification and visualization when True and no notification when False
    :return: a transformation object
    """
    distance_threshold = voxel_size * 1.5
    if verbose:
        print(":: RANSAC registration on downsampled point clouds.")
        print("   Since the downsampling voxel size is %.3f," % voxel_size)
        print("   we use a liberal distance threshold %.3f." % distance_threshold)
    result = op3.registration_ransac_based_on_feature_matching(
            source_down, target_down, source_fpfh, target_fpfh,
            distance_threshold,
            op3.TransformationEstimationPointToPoint(False), 4,
            [op3.CorrespondenceCheckerBasedOnEdgeLength(0.9),
            op3.CorrespondenceCheckerBasedOnDistance(distance_threshold)],
            op3.RANSACConvergenceCriteria(4000000, 500)
    )
    return result

def execute_fast_global_registration(source_down: op3.PointCloud, target_down: op3.PointCloud, 
                                     source_fpfh: op3.PointCloud, target_fpfh: op3.PointCloud, 
                                     voxel_size: float, verbose=False):
    """
    Find registertration to transform source point cloud to target point cloud
    :param source, target: 2 objects of Open3D, that are point clouds of source and target
    :param voxel_size: a float value, that is how sparse you want the sample points is
    :param verbose: a boolean value, display notification and visualization when True and no notification when False
    :return: a transformation object
    """
    distance_threshold = voxel_size * 0.5
    if verbose: 
        print(":: Apply fast global registration with distance threshold %.3f" % distance_threshold)
    result = op3.registration_fast_based_on_feature_matching(
        source_down, target_down, source_fpfh, target_fpfh, 
        op3.FastGlobalRegistrationOption(maximum_correspondence_distance = distance_threshold))
    return result

def refine_registration(source: op3.PointCloud, target: op3.PointCloud, 
                        voxel_size: float, gross_matching: np.ndarray, verbose=False):
    """
    Refine the matching
    :param source, target: 2 objects of Open3D, that are point clouds of source and target
    :param voxel_size: a float value, that is how sparse you want the sample points is
    :param gross_matching: a transformation matrix, that grossly matches source to target
    :param verbose: a boolean value, display notification and visualization when True and no notification when False
    :return: a transformation object
    """
    distance_threshold = voxel_size * 1
    if verbose:
        print(":: Point-to-plane ICP registration is applied on original point")
        print("   clouds to refine the alignment. This time we use a strict")
        print("   distance threshold %.3f." % distance_threshold)
    result = op3.registration_icp(source, target, distance_threshold,
                                  gross_matching.transformation,
                                  op3.TransformationEstimationPointToPlane(),
                                  op3.ICPConvergenceCriteria(max_iteration=2000))
    return result

def global_icp(source: op3.PointCloud, target: op3.PointCloud, voxel_size = 0.005, verbose=False):
    """
    Find registertration to transform source point cloud to target point cloud
    :param source, target: 2 objects of Open3D, that are point clouds of source and target
    :param voxel_size: a float value, that is how sparse you want the sample points is
    :param verbose: a boolean value, display notification and visualization when True and no notification when False
    :return: a transformation object
    
    248 ms ± 36.9 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    """
    if verbose: visualize_registration(source=source, target=target, transformation=np.identity(4))  # visualize point cloud
    
    # downsample data
    source_down, source_fpfh = sample_point_cloud_feature(point_cloud=source, voxel_size=voxel_size, verbose=verbose)
    target_down, target_fpfh = sample_point_cloud_feature(point_cloud=target, voxel_size=voxel_size, verbose=verbose)

    # 1st: gross matching(RANSAC)
    result_ransac = execute_global_registration(source_down=source_down, target_down=target_down, 
                                                source_fpfh=source_fpfh, target_fpfh=target_fpfh, 
                                                voxel_size=voxel_size, verbose=verbose)
    if verbose: visualize_registration(source=source_down, target=target_down, transformation=result_ransac.transformation)

    # 2nd: fine-tune matching(ICP)
    result_icp = refine_registration(source=source_down, target=target_down, voxel_size=voxel_size, gross_matching=result_ransac)
    if verbose: visualize_registration(source=source_down, target=target_down, transformation=result_icp.transformation)
    return result_icp

def fast_global_icp(source: op3.PointCloud, target: op3.PointCloud, voxel_size = 0.005, verbose=False):
    """
    Find registertration to transform source point cloud to target point cloud
    :param source, target: 2 objects of Open3D, that are point clouds of source and target
    :param voxel_size: a float value, that is how sparse you want the sample points is
    :param verbose: a boolean value, display notification and visualization when True and no notification when False
    :return: a transformation object
    
    19.9 ms ± 1.28 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
    """
    if verbose: visualize_registration(source=source, target=target, transformation=np.identity(4))  # visualize point cloud
    
    # downsample data
    source_down, source_fpfh = sample_point_cloud_feature(point_cloud=source, voxel_size=voxel_size, verbose=verbose)
    target_down, target_fpfh = sample_point_cloud_feature(point_cloud=target, voxel_size=voxel_size, verbose=verbose)

    # 1st: gross matching(Fast global registration)
    result_ransac = execute_fast_global_registration(source_down=source_down, target_down=target_down, 
                                                source_fpfh=source_fpfh, target_fpfh=target_fpfh, 
                                                voxel_size=voxel_size, verbose=verbose)
    if verbose: visualize_registration(source=source_down, target=target_down, transformation=result_ransac.transformation)

    # 2nd: fine-tune matching(ICP)
    result_icp = refine_registration(source=source_down, target=target_down, voxel_size=voxel_size, gross_matching=result_ransac)
    if verbose: visualize_registration(source=source_down, target=target_down, transformation=result_icp.transformation)
    return result_icp

def adjust_pc_coords(point_cloud: op3.PointCloud, coord: Tuple[float, float, float]):
    new_point_cloud = copy.deepcopy(point_cloud)
    new_point_cloud.points = op3.Vector3dVector(np.asarray(new_point_cloud.points) - np.asarray(coord))
    return new_point_cloud

def radian2degree(angles: np.ndarray):
    return angles * one_divided_pi * 180

def degree2radian(angles: np.ndarray):
    return angles * one_divided_180 * np.pi

def m2mm(coords: np.ndarray):
    return coords * 1000

def mm2m(coords: np.ndarray):
    return coords * 0.001

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
