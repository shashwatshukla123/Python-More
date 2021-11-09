#Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
#pip install matplotlib
import matplotlib

print(matplotlib.__version__)

#-----------------------------------
#Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:
#Example
#Draw a line in a diagram from position (0,0) to position (6,250):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
#-----------------------------------------
