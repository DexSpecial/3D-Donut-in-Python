import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create data for a 3D donut
theta = np.linspace(0, 2*np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)
theta, phi = np.meshgrid(theta, phi)
r = 0.4
x = (r + 0.1*np.cos(phi)) * np.cos(theta)
y = (r + 0.1*np.cos(phi)) * np.sin(theta)
z = 0.1 * np.sin(phi)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='gray', linewidth=0)
plt.show()
