import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [8,8,6,11,7]
eating =   [1,3,4,3,2]
working =  [7,8,7,2,2]
playing =  [8,5,7,8,13]


plt.plot([],[],color='m',label='Sleepping',linewidth=5)
plt.plot([],[],color='g',label='eating',linewidth=5)
plt.plot([],[],color='c',label='working',linewidth=5)
plt.plot([],[],color='r',label='playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing,colors=['m','g','c','r'])

plt.xlabel('Days')
plt.ylabel('activity')
plt.title('Area plot')
plt.legend()
plt.show()

