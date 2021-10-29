import numpy as np
import matplotlib.pyplot as plt


T = 0.00004

def x1(t):
  return np.sin(t)

def x2(t):
  return t

# Let T = 1
def Y1_1 (t): 
  return (t**2)*x1(t)
    
def Y1_2(t):
  return (t**2)*x2(t)
    

def Y1_1plusY1_2(t):
  return (t**2)*(x1(t)+x2(t))

def Y2_1 (t): 
  return t*np.abs(x1(t))
    
def Y2_2(t):
  return t*np.abs(x2(t))
    

def Y2_1plusY2_2(t):
  return t*np.abs(x1(t)+x2(t))

def Y3_1(t): 
  return np.abs(x1(t))
    
def Y3_2(t):
  return np.abs(x2(t))
    

def Y3_1plusY3_2(t):
  return np.abs(x1(t)+x2(t))

def Y4_1 (t): 
  return x1(t-5)
    
def Y4_2(t):
  return x2(t-5)
    

def Y4_1plusY4_2(t):
  return x1(t-5)+x2(t-5)








# Plotting input signals
t = np.linspace(-10 , 10, 1000)
plt.plot(t, x1(t) , 'r', label = "$x_1(t) = sin(t)$")
plt.plot(t , x2(t) , 'b', label = "$x_2(t) = t$")
plt.grid(True)
plt.legend(loc = 'upper right')
plt.title("Input signals")
plt.show()

# Plotting output signals 
plt.plot(t , Y1_1(t) , 'r', label = "$y_1(t)$, For $y(t)=t^2x(t)$")
plt.plot(t , Y1_2(t) , 'b' , label = "$y_2(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Output Signals: $T = 1$")
plt.show()

# Law of Additivity
plt.plot(t , Y1_1(t) + Y1_2(t) , 'r' , label = "$y_1(t) + y_2(t)$ For $y(t)=t^2x(t)$")
plt.plot(t , Y1_1plusY1_2(t) , 'k--' , label = "System acting on $x_1(t) + x_2(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Law of Additivity")
plt.show()

# Law of Homogeneity
plt.plot(t , 2 * Y1_1(t)  , 'r' , label = "$2y_1(t)$ For $y(t)=t^2x(t)$")
plt.plot(t , 2*(t**2)*x1(t) , 'k--' , label = "System acting on $2x_1(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Law of Homogeneity: $k = 2$")
plt.show()

# Time Invariance
# let us introduce a delay of t_0 = 2
plt.plot(t ,  Y1_1(t-2)  , 'r' , label = "$y_1(t-t_0)$ For $y(t)=t^2x(t)$")
plt.plot(t , (t**2)*x1(t-2) , 'k--' , label = "System acting on $x_1(t-t_0)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Time Invariance")
plt.show()


# Plotting output signals 
plt.plot(t , Y2_1(t) , 'r', label = "$y_1(t)$, For $y(t)=t|x(t)|$")
plt.plot(t , Y2_2(t) , 'b' , label = "$y_2(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Output Signals: $T = 1$")
plt.show()

# Law of Additivity
plt.plot(t , Y2_1(t) + Y2_2(t) , 'r' , label = "$y_1(t) + y_2(t)$ For $y(t)=t|x(t)|$")
plt.plot(t , Y2_1plusY2_2(t) , 'k--' , label = "System acting on $x_1(t) + x_2(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Law of Additivity")
plt.show()

# Law of Homogeneity
plt.plot(t , -2 * Y2_1(t)  , 'r' , label = "$-2y_1(t)$ For $y(t)=t|x(t)|$")
plt.plot(t , t*np.abs(-2*x1(t)) , 'k--' , label = "System acting on $-2x_1(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Law of Homogeneity: $k =- 2$")
plt.show()

# Time Invariance
# let us introduce a delay of t_0 = 2
plt.plot(t ,  Y2_1(t-2)  , 'r' , label = "$y_1(t-t_0)$ For $y(t)=t|x(t)|$")
plt.plot(t , t*np.abs(x1(t-2)) , 'k--' , label = "System acting on $x_1(t-t_0)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Time Invariance")
plt.show()

# Plotting output signals 
plt.plot(t , Y3_1(t) , 'r', label = "$y_1(t)$, For $y(t)=t^2x(t)$")
plt.plot(t , Y3_2(t) , 'b' , label = "$y_2(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Output Signals: $T = 1$")
plt.show()

# Law of Additivity
plt.plot(t , Y3_1(t) + Y3_2(t) , 'r' , label = "$y_1(t) + y_2(t)$ For $y(t)=|x(t)|$")
plt.plot(t , Y3_1plusY3_2(t) , 'k--' , label = "System acting on $x_1(t) + x_2(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Law of Additivity")
plt.show()

# Law of Homogeneity
plt.plot(t , -2 * Y3_1(t)  , 'r' , label = "$-2y_1(t)$ For $y(t)=|x(t)|$")
plt.plot(t , np.abs(-2*x1(t)) , 'k--' , label = "System acting on $-2x_1(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Law of Homogeneity: $k = -2$")
plt.show()

# Time Invariance
# let us introduce a delay of t_0 = 2
plt.plot(t ,  Y1_1(t-2)  , 'r' , label = "$y_1(t-t_0)$ For $y(t)=|x(t)|$")
plt.plot(t , np.abs(x1(t-2)) , 'k--' , label = "System acting on $x_1(t-t_0)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Time Invariance")
plt.show()

# Plotting output signals 
plt.plot(t , Y4_1(t) , 'r', label = "$y_1(t)$, For $y(t)=x(t-5)$")
plt.plot(t , Y4_2(t) , 'b' , label = "$y_2(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Output Signals: $T = 1$")
plt.show()

# Law of Additivity
plt.plot(t , Y4_1(t) + Y4_2(t) , 'r' , label = "$y_1(t) + y_2(t)$ For $y(t)=x(t-5)$")
plt.plot(t , Y4_1plusY4_2(t) , 'k--' , label = "System acting on $x_1(t) + x_2(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Law of Additivity")
plt.show()

# Law of Homogeneity
plt.plot(t , 2 * Y4_1(t)  , 'r' , label = "$2y_1(t)$ For $y(t)=x(t-5)$")
plt.plot(t , 2*x1(t-5) , 'k--' , label = "System acting on $2x_1(t)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Law of Homogeneity: $k = 2$")
plt.show()

# Time Invariance
# let us introduce a delay of t_0 = 2
plt.plot(t ,  Y4_1(t-2)  , 'r' , label = "$y_1(t-t_0)$ For $y(t)=x(t-5)$")
plt.plot(t , x1(t-7) , 'k--' , label = "System acting on $x_1(t-t_0)$")
plt.legend(loc = 'upper right')
plt.grid(True)
plt.title("Time Invariance")
plt.show()
