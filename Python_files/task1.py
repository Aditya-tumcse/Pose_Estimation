import numpy as np
import cv2
import argparse


parser = argparse.ArgumentParser(description = "Code for feature detection")
parser.add_argument('--input',help="Path to input image")
args = parser.parse_args()

img = cv2.imread(cv2.samples.findFile(args.input))

if img is None:
    print("Error!Could not open or find the input file.",args.input)
    exit(0)

#2D image points.Manually enter the 2D coordinates of the visible vertices of the box.
image_points = np.array([
    (1460, 1140),#Point 0
    (2056, 964),#Point 1
    (2296, 1024),#Point 2
    (1696, 1232),#Point 3
    (1472, 1608), #Point 4
    #(1348, 1340), #Point 5
    (2264, 1444),#Point 6
    (1700, 1724)#Point 7
],dtype="double")

#3D model points
model_points = np.array([
    (0.0, 0.063, 0.093), #Point 0
    (0.165, 0.063, 0.093), #Point 1
    (0.165, 0.0, 0.093), #Point 2
    (0.0, 0.0, 0.093), #Point 3
    (0.0, 0.063, 0.0), #Point 4
    #(0.165, 0.063, 0.0), #Point 5
    (0.165, 0.0, 0.0), #Point 6
    (0.0, 0.0, 0.0) #Point 7
])

#Camera internal parameters
focal_length = 2960.37845
principal_points = (1841.68855,1235.23369)
camera_matrix = np.array([[focal_length,0,principal_points[0]],
                          [0,focal_length,principal_points[1]],
                          [0,0,1]],dtype="double")

distortion_params = None
success,rotation_vector,translation_vector = cv2.solvePnP(model_points, image_points, camera_matrix, distortion_params)
print("Rotation vector:\n{0}".format(rotation_vector))
print("Translation vector:\n{0}".format(translation_vector))


file = open("Solution_file.txt",'a')
np.savetxt(file,rotation_vector.flatten(), newline="\t")
np.savetxt(file,translation_vector.flatten(),newline="\t")

file.close()






