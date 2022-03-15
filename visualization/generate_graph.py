import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d

def loadTxt(file):
    with open(file, 'r') as filePoints:
        points = [point.split() for point in filePoints]
        return points

class PlotPoints:


    def __init__(self, limit=[-3*10, 3*10]):
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title('Lemniscate')
        self.ax.set_xlim(limit)
        self.ax.set_xlabel("Y [mm] ")
        self.ax.set_ylim(limit)
        self.ax.set_ylabel("X [mm]")
        self.ax.xaxis.set_ticks(np.arange(-3*1000, 3*1000, 0.5*1000))
        self.ax.yaxis.set_ticks(np.arange(-3*1000, 3*1000, 0.5*1000))
        #self.ax.set_facecolor((1.0, 0.47, 0.42))

        #self.ax.plot(current_pose_list_x[:int(propotion/2)], current_pose_list_y[:int(propotion/2)] ,'deeppink')
        #self.ax.plot(current_pose_list_x[int(propotion/2):propotion], current_pose_list_y[int(propotion/2):propotion] ,'forestgreen', label = 'Part 1')

        #self.ax.plot(current_pose_list_x[propotion:2*propotion +1], current_pose_list_y[propotion:2*propotion +1] ,'deeppink', label = 'Part 2')

        #self.ax.plot(current_pose_list_x[2*propotion +1:2*propotion +1 +int(propotion/2)], current_pose_list_y[2*propotion +1:2*propotion +1 +int(propotion/2)] ,'deepskyblue', label = 'Part 3')
        #self.ax.plot(current_pose_list_x[2*propotion +1 +int(propotion/2):], current_pose_list_y[2*propotion +1 +int(propotion/2):] ,'deeppink')

        #self.ax.plot(desired_pose_list_x, desired_pose_list_y, 'black', label = 'Ground truth')

        #self.ax.plot(current_pose_list_x, current_pose_list_y, 'blue', label = 'real')


        self.ax.plot(current_pose_list_y[:int(propotion/2)], current_pose_list_x[:int(propotion/2)] ,'deeppink')
        self.ax.plot(current_pose_list_y[int(propotion/2):propotion], current_pose_list_x[int(propotion/2):propotion] ,'forestgreen', label = 'Part 1')

        self.ax.plot(current_pose_list_y[propotion:2*propotion +1], current_pose_list_x[propotion:2*propotion +1] ,'deeppink', label = 'Part 2')

        self.ax.plot(current_pose_list_y[2*propotion +1:2*propotion +1 +int(propotion/2)], current_pose_list_x[2*propotion +1:2*propotion +1 +int(propotion/2)] ,'deepskyblue', label = 'Part 3')
        self.ax.plot(current_pose_list_y[2*propotion +1 +int(propotion/2):], current_pose_list_x[2*propotion +1 +int(propotion/2):] ,'deeppink')

        self.ax.plot(desired_pose_list_y, desired_pose_list_x, 'black', label = 'Ground truth')

class PlotError:

    
    def __init__(self, limit=[-3, 3]):
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title('Error')
        self.ax.set_xlim([0, 95])
        self.ax.set_xlabel("Time [s]")
        self.ax.set_ylim([0, 0.500*1000])
        self.ax.set_ylabel("Error [mm]")

        self.time_discret = 90/len(current_pose_list_x)
        self.time = []
        self.med_error = []
        for i in range(len(current_pose_list_x)):
            self.time.append(i*self.time_discret) 
            self.med_error.append(erro_med) 

        self.ax.plot(self.time[:int(propotion/2)], erro[:int(propotion/2)], 'deeppink')
        self.ax.plot(self.time[int(propotion/2):propotion], erro[int(propotion/2):propotion], 'forestgreen', label = 'Error part 1')

        self.ax.plot(self.time[propotion:2*propotion +1], erro[propotion:2*propotion +1], 'deeppink', label = 'Error part 2')

        self.ax.plot(self.time[2*propotion +1:2*propotion +1 +int(propotion/2)], erro[2*propotion +1:2*propotion +1 +int(propotion/2)], 'deepskyblue', label = 'Error part 3')
        self.ax.plot(self.time[2*propotion +1 +int(propotion/2):], erro[2*propotion +1 +int(propotion/2):], 'deeppink')

        self.ax.plot(self.time, self.med_error, 'black', label = 'Mean Error')


id_data = input("Digite Id:")

current_pose_list_string = np.array(loadTxt(f'file/current_pose_list_{id_data}.txt'))
current_pose_list_number =  current_pose_list_string.astype(np.float64)

desired_pose_list_string = np.array(loadTxt(f'file/desired_pose_list_{id_data}.txt'))
desired_pose_list_number =  desired_pose_list_string.astype(np.float64)

current_pose_list_x = []
current_pose_list_y = []

desired_pose_list_x = []
desired_pose_list_y = []
erro = []


for i in range(0, len(current_pose_list_string)):
    if desired_pose_list_number[i][0] != 0:
        if i%2 == 0:
            current_pose_list_x.append(1000*current_pose_list_number[i][0])
            desired_pose_list_x.append(1000*desired_pose_list_number[i][0])
        else:
            current_pose_list_y.append(1000*current_pose_list_number[i][0])
            desired_pose_list_y.append(1000*desired_pose_list_number[i][0])

length = len(current_pose_list_x)
propotion = int(length/3)

erro_x = np.array(desired_pose_list_x) - np.array(current_pose_list_x)
erro_y = np.array(desired_pose_list_y) - np.array(current_pose_list_y)


for i in range(0, length):
    valuer = math.sqrt(math.pow(erro_x[i],2)+math.pow(erro_y[i],2))
    erro.append(valuer)

erro_med = sum(erro)/len(erro)
errox_med = sum(abs(erro_x))/len(erro_x)
erroy_med = sum(abs(erro_y))/len(erro_y)

print(f"erro em x: {errox_med/1000},  erro em y; {erroy_med/1000},   erro euclidiano:{erro_med/1000}")

plot = PlotPoints(limit=[-1.5*1000, 1*1000])
plt.legend()
plt.grid()
plot = PlotError()
plt.legend()
plt.grid()
plt.show()
