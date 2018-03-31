import matplotlib.pyplot as plot
import numpy as numpy

m = 0.2   #ratio

samplingRate = 150.0  # sampling rate
samplingInterval = 1.0/samplingRate  # sampling interval

t = numpy.arange(0, 2, samplingInterval)    #min,max,inc

theta = m*numpy.sin(2 * numpy.pi * 2 * t)

#sin(2*pi*f*t+theta)
y = numpy.sin(2 * numpy.pi * 10 * t + theta)

print(y)
fig,myplot = plot.subplots(2, 1)
myplot[0].plot(t,y)
myplot[0].set_xlabel('Time')
myplot[0].set_ylabel('Amplitude')



plot.show()