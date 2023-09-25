#!/usr/bin python2

import numpy as np
from math import cos, sin, atan2


def get_transform_from_data_np(x, y, theta):
    return np.array([[cos(theta), -sin(theta), x],
                     [sin(theta), cos(theta), y],
                     [0, 0, 1]])


def get_offset_from_matrix(mat):
    x = mat[0][2]
    y = mat[1][2]
    angle = atan2(mat[1][0], mat[0][0])
    return (x, y, angle)


if __name__ == '__main__':
    # base_link to cam
    base_link_to_cam = get_transform_from_data_np(-0.428281711692,
                                                  -0.531588184891,
                                                  -0.04710303250830944)
    marker_to_cam = get_transform_from_data_np(-0.0098, -0.035,
                                               6.250024051391694)

    target_to_marker = get_transform_from_data_np(-0.4275, -0.5445,
                                                  0.024686342055599407)

    cam_to_base_link = np.linalg.inv(base_link_to_cam)
    # print(cam_to_base_link)

    target_to_cam = np.matmul(target_to_marker, marker_to_cam)
    # print(target_to_cam)

    target_to_base_link = np.matmul(target_to_cam, cam_to_base_link)
    # print(target_to_base_link)

    params = get_offset_from_matrix(target_to_base_link)
    print(params)
