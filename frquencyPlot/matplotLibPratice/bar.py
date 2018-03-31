import matplotlib.pyplot as plt

plt.bar( [2,4,6,8,10] , [6,7,8,2,4], label='bar1' ,color='r')           # x-axis y-axis
plt.bar( [1,3,5,9,11] , [7,8,2,4,2], label='bar2',color='c' )           # x-axis y-axis

plt.xlabel('xaxis')
plt.ylabel('yaxis')
plt.title('simple bar')

plt.legend()
plt.show()