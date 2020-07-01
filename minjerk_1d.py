import numpy as np
import bswarm.trajectory as traj
import matplotlib.pyplot as plt

T = [20,5,10,4]
waypoints = np.array([0,-5,2,5,3])
traj_1d = traj.min_deriv_1d(3,waypoints,T,False,velocities=[1,2,-1,5,0])
res = traj_1d.eval()

plt.title('1D Trajectory: 5th order, Velocities Specified')
plt.plot(res[0],res[1])
plt.plot(np.concatenate( (np.array([0]),np.cumsum(T)) ),waypoints,'x')
plt.ylabel('Position')
plt.xlabel('Time')

traj_1d = traj.min_deriv_1d(3,waypoints,T,False)
res = traj_1d.eval()

plt.figure()
plt.title('1D Trajectory: 5th order, Velocities NOT Specified')
plt.plot(res[0],res[1])
plt.plot(np.concatenate( (np.array([0]),np.cumsum(T)) ),waypoints,'x')
plt.ylabel('Position')
plt.xlabel('Time')
plt.show()