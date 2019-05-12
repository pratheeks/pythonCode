import matplotlib.pyplot as plt
import numpy as np
t=np.arange(0,2*np.pi,0.1)
x=16*np.sin(t)**3
y=13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
plt.axis('off')                               #shows axis x and y       
plt.plot(x,y, color='black',linewidth=7.0)    #border/sketch/outline of shape 
plt.fill(x,y, color='red')                    #colr to be filled inside the shape  
plt.text(5,-15,'text',fontsize=20)            #text to be printed(x,y,'text',size of text)
plt.show()                                    #prints the shape  