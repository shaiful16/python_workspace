import matplotlib.pyplot as plt

plt.plot( [1,2,3] , [5,7,4], label='first' )           # x-axis y-axis
plt.plot( [1,2,3] , [10,14,12], label='second' )           # x-axis y-axis
plt.xlabel('xaxis')
plt.ylabel('yaxis')
plt.title('simple plot')
plt.legend()
plt.show()