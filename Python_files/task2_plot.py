import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image


#Internal Caliberation marix
focal_length = 2960.37845
principal_points = (1841.68855, 1235.23369)
camera_matrix = np.array([[focal_length,0,principal_points[0]],
                         [0,focal_length,principal_points[1]],
                         [0,0,1]],dtype="double")

d = np.loadtxt("solution_task_2.txt")

#Compute the rotation matrix
rotation_matrix = np.zeros(shape=(3,3))
cv2.Rodrigues(d[0:3],rotation_matrix)

# 3D model points
model_points = np.array([
    (0.0, 0.063, 0.093),  # Point 0
    (0.165, 0.063, 0.093),  # Point 1
    (0.165, 0.0, 0.093),  # Point 2
    (0.0, 0.0, 0.093),  # Point 3
    (0.0, 0.063, 0.0),  # Point 4
    (0.165, 0.063, 0.0),  # Point 5
    (0.165, 0.0, 0.0),  # Point 6
    (0.0, 0.0, 0.0)  # Point 7
])

#Computing the coordinates in the image plane
total = []
for j in range(np.shape(model_points)[0]):
    f = np.dot(rotation_matrix, model_points[j])
    v = f + d[3:6]
    total.append(np.dot(camera_matrix, v))

#Obtain the 2D points on the image plane
k = 0
for k in range(np.shape(model_points)[0]):
    total[k][0] = total[k][0] / total[k][2]
    total[k][1] = total[k][1] / total[k][2]

m = 0
n = 0
img_point_1 = np.zeros(shape=(8, 2))
for m in range(np.shape(model_points)[0]):
    for n in range(np.shape(img_point_1)[1]):
        img_point_1[m][n] = total[m][n]


#Plotting the bounding box
image = Image.open("/home/aditya/Documents/Sem_3/TDCV/Project_1/tracking/color_000006.JPG") #Provide path to the image
plt.imshow(image)
plt.plot([img_point_1[0][0], img_point_1[1][0]], [img_point_1[0][1], img_point_1[1][1]])
plt.plot([img_point_1[1][0], img_point_1[2][0]], [img_point_1[1][1], img_point_1[2][1]])
plt.plot([img_point_1[2][0], img_point_1[3][0]], [img_point_1[2][1], img_point_1[3][1]])
plt.plot([img_point_1[3][0], img_point_1[0][0]], [img_point_1[3][1], img_point_1[0][1]])
plt.plot([img_point_1[4][0], img_point_1[5][0]], [img_point_1[4][1], img_point_1[5][1]])
plt.plot([img_point_1[5][0], img_point_1[6][0]], [img_point_1[5][1], img_point_1[6][1]])
plt.plot([img_point_1[6][0], img_point_1[7][0]], [img_point_1[6][1], img_point_1[7][1]])
plt.plot([img_point_1[7][0], img_point_1[4][0]], [img_point_1[7][1], img_point_1[4][1]])
plt.plot([img_point_1[0][0], img_point_1[4][0]], [img_point_1[0][1], img_point_1[4][1]])
plt.plot([img_point_1[3][0], img_point_1[7][0]], [img_point_1[3][1], img_point_1[7][1]])
plt.plot([img_point_1[1][0], img_point_1[5][0]], [img_point_1[1][1], img_point_1[5][1]])
plt.plot([img_point_1[2][0], img_point_1[6][0]], [img_point_1[2][1], img_point_1[6][1]])
plt.show()



