import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import cv2

s = np.loadtxt("Solution_file.txt")

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlim3d(-0.6,0.6)
ax.set_ylim3d(-0.6,0.6)
ax.set_zlim3d(0,0.6)

#Plotting the box
vertices = np.loadtxt("box.txt")

#list of sides' polygon of figure
faces = [[vertices[0],vertices[1],vertices[2],vertices[3]],
         [vertices[0],vertices[4],vertices[7],vertices[3]],
         [vertices[0],vertices[1],vertices[5],vertices[4]],
         [vertices[1],vertices[5],vertices[6],vertices[2]],
         [vertices[3],vertices[2],vertices[6],vertices[7]],
         [vertices[4],vertices[5],vertices[6],vertices[7]]]


#plot sides
ax.add_collection3d(Poly3DCollection(faces,linewidths=1,edgecolors='black'))

#Camera internal parameters
focal_length = 2960.37845
principal_points = (1841.68855,1235.23369)
camera_matrix = np.array([[focal_length,0,principal_points[0]],
                          [0,focal_length,principal_points[1]],
                          [0,0,1]],dtype="double")

X_centre = 0.0
Y_centre = 0.0
Z_centre = 0.0
for i in range(8):
    X_centre += vertices[i][0]
    Y_centre += vertices[i][1]
    Z_centre += vertices[i][2]


for i in range(8):
    #Computing the rotation matrix
    rotation_matrix = np.zeros(shape=(3, 3))
    cv2.Rodrigues(s[i][0:3], rotation_matrix)

    #Computing the optical centres
    Q = np.dot(camera_matrix,rotation_matrix) #Camera intrinsics and rotation matrix
    q = np.dot(camera_matrix,s[i][3:6])#Camera intrinsics and translation vector
    opt_centre = -np.dot(np.linalg.inv(Q),q) #Optical centre


    #Projecting the image centre to the 3D point

    x_values = [opt_centre[0], X_centre/8.0]
    y_values = [opt_centre[1], Y_centre/8.0]
    z_values = [opt_centre[2], Z_centre/8.0]
    ax.scatter(opt_centre[0], opt_centre[1], opt_centre[2])
    plt.plot(x_values, y_values, z_values)

plt.show()
