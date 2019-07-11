import matplotlib.pyplot as plt 
  
x = [2,5,70,40,30,45,50,45,43,40,44,60,7,13,57,18,90,77,32,21,20,40] 
  
range = (0, 100) 
bins = 10  
  
plt.hist(x, bins, range,color = 'blue',rwidth = 0.8) 
  
plt.xlabel('X-axis') 
plt.ylabel('y-axis') 
plt.title('Histogram') 
  
plt.show()

