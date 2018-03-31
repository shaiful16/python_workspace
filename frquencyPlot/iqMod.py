import matplotlib.pyplot as plot
import numpy as numpy

i = numpy.array([1,0,1,0])
q=numpy.array([1,0,1,0])
#i = numpy.array([-1,0.5,-0.8,0.7,1])
#q=numpy.array([-1,1,0,0.5,-0.5])
#q=numpy.array([0,0,0,0,0])
arrayLength=len(i)
iInverse=numpy.array([])
qInverse=numpy.array([])
x=numpy.array([])
y=numpy.array([])
result=numpy.array([])

for c in numpy.nditer(i):
    iInverse = numpy.append(iInverse, c*(-1))

for c in numpy.nditer(q):
    qInverse = numpy.append(qInverse, c*(-1))

for c in range(0,arrayLength,1):
    result = numpy.append(result, i[c])
    result = numpy.append(result, q[c])
    result = numpy.append(result, iInverse[c])
    result = numpy.append(result, qInverse[c])

print(result)

for c in range(0,arrayLength*4,1):
    x = numpy.append(x, c)
    y = numpy.append(y, result[c])

fig,myplot = plot.subplots(1, 1)
myplot.plot(x,y)
myplot.set_xlabel('x-axis')
myplot.set_ylabel('y-axis')



#plot.savefig('iqmod')
plot.show()
