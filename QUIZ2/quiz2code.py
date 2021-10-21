# QUIZ 2
# PLOT OF DISCRETE TIME SIGNAL
import numpy as np
import matplotlib.pyplot as plt
# Defining unit step function
def u(n):
  if (n >= 0):
    return 1
  else:
    return 0

n = np.linspace(-10,10,20)
n=n.astype(int)
a=np.zeros(20)
for i in range(20):
  a[i] =np.abs(1/2*u(n[i])*(np.e**(1j*n[i]*(np.pi))+np.cos((n[i]*np.pi)/2)+np.sin((np.pi/2)+2*np.pi*n[i])))



plt.stem(n, a,use_line_collection=True,label="$a[n] = e^{j\pi n}+\cos(n \pi/2)+\sin(\pi/2 + 2n\pi)$") 
plt.title('Stem plot of sequence a[n]')
plt.grid()
plt.xlim([-11, 11])
plt.ylim([-1, 2])
plt.xlabel("n")
plt.ylabel("|a[n]|")
plt.legend(loc='upper right')

plt.show()

#Plotting zeros and poles of z tranform

import matplotlib.patches as mpatches
import matplotlib.lines as mlines

fig, ax = plt.subplots(figsize = (6,6))

ax.set_xlim([-3,3])
ax.set_ylim([-3,3])

pole, = plt.plot(1,0, 'rx',label = 'Poles')
zero, = plt.plot(0,1/3, 'ro',label = 'Zeros')
zero2, =plt.plot(0,-1/3, 'ro',label = 'Zeros')

legend = plt.legend(handles =[pole,zero], loc = 'lower right')
fig.gca().add_artist(legend)

circle = plt.Circle([0,0],1,color = 'orange')
fig.gca().add_artist(circle)

circle = plt.Circle([0,0],1,edgecolor = 'black',fill = 0,linestyle = '-')
fig.gca().add_artist(circle)

patches = mpatches.Patch(color="orange", label="ROC")
dotted_line = mlines.Line2D([],[],color = 'black',label='Unit circle')
dotted_line.set_linestyle('-')
plt.legend(handles=[patches,dotted_line], loc = 'upper right')
ax.set_facecolor('xkcd:cyan')

plt.grid()
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
