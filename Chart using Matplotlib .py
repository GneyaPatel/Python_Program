pie chart--------------------------
import matplotlib.pyplot as plt
values = [2,4,3,3,4,2]
colors = ['b', 'g', 'r', 'c', 'm', 'y']
labels = ['DE', 'DS', 'DM', 'PS', 'OOP', 'PEM']
explode = (0, 0, 0, 0.3, 0, 0)
plt.pie(values, colors=colors,labels=labels,explode=explode,autopct='%.1f%%',counterclock=True,shadow=True)
plt.title('Credits')
plt.show()

bar chart---------------------------
import matplotlib.pyplot as plt
values = [1, 5, 8, 9, 2, 1, 3, 10, 4, 7]
colors = ['b', 'r', 'b', 'b', 'b', 'r','b', 'b', 'b', 'g']
plt.bar(range(1, 11), values,color=colors,align='edge')
plt.xlabel('Day of Date')
plt.ylabel('Temparure')
plt.title('Temprature per Day')
plt.show()

histogram------------------------
import matplotlib.pyplot as plt
population_age=[11,12,12,12,15,21,22,23,24,35,40,25,27,45,28,29,55,28,27,31,32,33,41, 42,45,46,47,40,50,59,57,56,55]
bins=[10,20,30,40,50,60]
plt.hist(population_age,bins,histtype='bar',rwidth=0.5,color='c')
plt.show()

line plot--------------------------

import matplotlib.pyplot as plt
values = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
values2 = [3, 8, 9, 2, 1, 2, 4, 7, 6, 6]
plt.plot(range(1,11), values,'-.')
plt.plot(range(1,11), values2,':', color='m')
plt.show()

box plot--------------------------

values = [10,20,30,40,50,60,70,80,90,100,125]
plt.boxplot(values,sym='go',notch=True)
plt.show()

scatter plot---------------------

1.-------
x = [1,2,3,4,5] 
y = [1,4,9,16,25] 
color = ['r','g','y','lightblue','purple']
plt.scatter(x,y,color=color,s=180,marker='*')
plt.show()

2.-------
import numpy as np
x1 = np.random.rand(50) * 5
x2 = np.random.rand(10) * 5 + 25
x3 = np.random.rand(50) * 25
x = np.concatenate((x1,x2,x3))
y1 = np.random.rand(50) * 5
y2 = np.random.rand(10) * 5 + 25
y3 = np.random.rand(50) * 25
y = np.concatenate((y1,y2,y3))
color = ['r']*50 + ['g']*10 + ['b']*50
plt.scatter(x,y,color=color)
plt.show()