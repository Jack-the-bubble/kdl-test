#!/usr/bin python2

from PyKDL import Frame, Vector, Rotation

from kdl_test import get_transform_from_data


# ---------INIT VARS----------
# base_link to cam
base_link_to_cam = get_transform_from_data(-0.428281711692, -0.531588184891,
                                           -0.04710303250830944)
# print(base_link_to_cam)

# marker to cam
marker_to_cam = get_transform_from_data(-0.0098, -0.035, 6.250024051391694)
# marker_to_cam = get_transform_from_data(-0.0098, -0.035, 0)

# target to marker
target_to_marker_t = get_transform_from_data(-0.4275, -0.5445,
                                             0.024686342055599407)
#  ---------FINISH INIT--------

# base_link to cam into cam to base_link
cam_to_base_link = base_link_to_cam.Inverse()
# print(cam_to_base_link)

# target to cam
target_to_cam = target_to_marker_t * marker_to_cam
# print(target_to_cam)

# target to base_link
target_to_base_link = target_to_cam * cam_to_base_link
# print(target_to_base_link)
print(target_to_base_link.p.x())
print(target_to_base_link.p.y())
print(target_to_base_link.M.GetRPY()[2])
