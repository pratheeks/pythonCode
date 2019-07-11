import matplotlib.pyplot as plt 
  
x = [1, 2, 3, 4, 5] 
  
y = [10, 20, 30, 40, 50] 
  
label = ['one', 'two', 'three', 'four', 'five'] 
  
plt.bar(x, y, tick_label = label, width = 0.8, color = ['red', 'green']) 
  
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 

plt.title('Bar Chart') 
  
