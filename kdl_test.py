#!/usr/bin python2

from PyKDL import Frame, Vector, Rotation


def get_transform_from_data(x, y, theta):
    target_to_marker_v = Vector(x, y, 0)
    target_to_marker_r = Rotation()
    target_to_marker_r.DoRotZ(theta)
    target_to_marker_t = Frame(target_to_marker_r, target_to_marker_v)
    return target_to_marker_t


if __name__ == '__main__':

    # ------------INIT VARS----------------
    # transform from target to base_link
    target_to_base_link = get_transform_from_data(-0.029, -0.032,
                                                  0.03862811877601662)
    # print(target_to_base_link)


    # transform from target center to marker
    target_to_marker_t = get_transform_from_data(-0.4275, -0.5445,
                                                 0.024686342055599407)
    # print(target_to_marker_t)

    # transform from marker to camera
    marker_to_cam_t = get_transform_from_data(-0.0098, -0.035,
                                              6.250024051391694)
    # print(marker_to_cam_t)

    # ------------FINISH INIT-------------

    # base_link to target
    base_link_to_target_t = target_to_base_link.Inverse()
    # print(base_link_to_target_t)

    # base_link to cam
    base_link_to_marker = base_link_to_target_t * target_to_marker_t
    # print(base_link_to_marker)
    base_link_to_cam = base_link_to_marker * marker_to_cam_t
    # print(base_link_to_cam)
    print(base_link_to_cam.p.x())
    print(base_link_to_cam.p.y())
    print(base_link_to_cam.M.GetRPY())
