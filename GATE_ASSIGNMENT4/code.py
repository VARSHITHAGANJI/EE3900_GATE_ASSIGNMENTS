##Plotting the poles of the system or roots of the characteristic equation
import numpy as np
import matplotlib.pyplot as plt
pole1 = [-0.9,0]
pole2 = [0.9 , 0]
pole3 = [0,0]

theta = np.linspace(0, 2*np.pi, n, endpoint=True)

ax = plt.subplot(111, aspect='equal')

plt.plot(np.sin(theta), np.cos(theta) , 'k-' , label = "Unit Circle: $|z| = 1$")
plt.plot([pole1[0] , pole2[0],pole3[0]] , [pole1[1],pole2[1],pole3[1]] , 'rx' , label = "Roots of $z^3-0.81z=0$")

plt.title("Poles plot")
plt.grid(True)
plt.legend(loc='upper right')
plt.show()

