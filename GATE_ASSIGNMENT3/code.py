## Author: Ganji Varshitha (AI20BTECH11009) ##
## Code to plot the ROC for Unilateral Laplace Transform ##
#importing numpy and matplotlib libraries
import numpy as np
import matplotlib.pyplot as plt

#Defining limits for axis
plt.xlim(-2,7)
plt.ylim(-2, 7)
y = np.linspace(-2,7,100)
x1 = [2]*y.shape[0]
plt.plot(x1, y,color = 'r',label="x=a(say 2)") # Plotting x = a+2 line(taking a = 0)
x2 = [4]*y.shape[0]
plt.plot(x2, y,color = 'black',label="x=a+2")
x= np.linspace(4,7,100)
y1 = [7]*y.shape[0]


plt.text(4 * (1 - 0.1), -2 * (1 + 0.7) , 'Re(s)=a+2')

y2 = [-2]*y.shape[0]
plt.fill_between(x, y2, y1, color='orange',label = "Roc = Re(s)>a+2")

plt.xlabel('$\sigma$')
plt.ylabel('$j\omega$')
plt.legend(loc='upper left')
plt.show()

