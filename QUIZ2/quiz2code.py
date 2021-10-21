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
