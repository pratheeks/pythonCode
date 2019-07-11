import matplotlib.pyplot as plt

names = 'Python', 'C++', 'Ruby', 'Java'

sizes = [200, 130, 150, 210]

color = ['orange', 'yellow', 'blue', 'red']

out = (0, 0, 0, 0.5)

plt.pie(sizes, explode=out, labels=names, colors=color,
        autopct='%1.2f%%', shadow=True, startangle=90)

#plt.axis('equal')

plt.show()

