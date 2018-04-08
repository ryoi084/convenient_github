import numpy
import matplotlib.pyplot

x = numpy.linspace(-10,10,100)

fig = matplotlib.pyplot.figure()

matplotlib.pyplot.plot(x,x**2)

matplotlib.pyplot.show()
