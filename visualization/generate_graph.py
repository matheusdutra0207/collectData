import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d

def loadTxt(file):
    with open(file, 'r') as filePoints:
        points = [point.split() for point in filePoints]
        return points

class PlotPoints:
    def __init__(self, limit=[-3, 3]):
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title('Lemniscate')
        self.ax.set_xlim(limit)
        self.ax.set_xlabel("y axis")
        self.ax.set_ylim(limit)
        self.ax.set_ylabel("x axis")
        #self.ax.set_facecolor((1.0, 0.47, 0.42))
        self.ax.plot(current_pose_list_x[:1000], current_pose_list_y[:1000] ,'red', label = 'red')
        self.ax.plot(current_pose_list_x[1001:-1], current_pose_list_y[1001:-1] ,'blue', label = 'blue')



current_pose_list_string = np.array(loadTxt('file/current_pose_list.txt'))
current_pose_list_number =  current_pose_list_string.astype(np.float64)

desired_pose_list_string = np.array(loadTxt('file/desired_pose_list.txt'))
desired_pose_list_number =  desired_pose_list_string.astype(np.float64)

current_pose_list_x = []
current_pose_list_y = []

desired_pose_list_x = []
desired_pose_list_y = []

for i in range(0, len(current_pose_list_string)):
    if i%2 == 0:
        current_pose_list_x.append(current_pose_list_number[i][0])
        desired_pose_list_x.append(desired_pose_list_number[i][0])
    else:
        current_pose_list_y.append(current_pose_list_number[i][0])
        desired_pose_list_y.append(desired_pose_list_number[i][0])

plot = PlotPoints(limit=[-2.5, 2.5])
plt.legend()
plt.show()
