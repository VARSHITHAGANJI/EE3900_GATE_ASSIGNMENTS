import matplotlib.pyplot as plt
import matplotlib.cm     as cm
from matplotlib.colors import Normalize
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import numpy as np


theta = np.linspace(0, 2*np.pi, 100, endpoint=True)
# fill color in Circle
cmap = cm.jet   # Select colormap U want
# Declare for set range of value for normalization
vmin = 0        
vmax = 1
# Normalize value for cmap
norm = Normalize(vmin, vmax)
fig, ax = plt.subplots(figsize = (6,6))
poles, = plt.plot([0.9,-0.9,0],[0,0,0], 'ro',label = 'Poles')
patches = mpatches.Patch(color="hotpink", label="ROC : |z|>0.9")

dotted_line = mlines.Line2D([],[],color = 'black',label='Unit circle |z| = 1')
dotted_line.set_linestyle('-')
dotted_line1 = mlines.Line2D([],[],color = 'blue',label='Circle |z| = 0.9')
dotted_line1.set_linestyle('-')
ax.set_xlim([-2,2])
ax.set_ylim([-2,2])
draw_circle = plt.Circle((0, 0), 1,fill = False)

p = plt.plot(0.9*np.sin(theta), 0.9*np.cos(theta) , 'k-' , label = "Unit Circle: $|z| = 1$",color='b')
dr = plt.Circle((0, 0), 0.9,color='white',edgecolor='blue',ls='-')
plt.gcf().gca().add_artist(draw_circle)
plt.gcf().gca().add_artist(dr)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Possible ROC of $z^3-0.81z=0$')
plt.legend(handles=[patches,dotted_line,poles,dotted_line1], loc = 'upper right')
ax.set_aspect(1)
ax.set_facecolor('xkcd:pink')
plt.show()
