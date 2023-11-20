# Get centroids.

import cv2
import numpy as np
from plantcv.plantcv import params
from plantcv.plantcv._helpers import _cv2_findcontours


def get_centroids(bin_img):
    """Get the coordinates (row,column) of the centroid of each connected region in a binary image.

    Inputs:
    bin_img       = Binary image containing the connected regions to consider

    Returns:
    coor  = List of coordinates (row,column) of the centroids of the regions

    :param bin_img: numpy.ndarray
    :return coor: list
    """
    params.device += 1
    # find contours in the binary image
    contours, _ = _cv2_findcontours(bin_img.astype(np.uint8))
    coor = []
    for c in contours:
        # calculate moments for each contour
        M = cv2.moments(c)
        # calculate row,col coordinates of centroid
        col = int(M["m10"] / M["m00"])
        row = int(M["m01"] / M["m00"])
        coor.append([row, col])

    return coor
