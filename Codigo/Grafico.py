import nuclear
import numpy as np
import matplotlib.pyplot as plt

def grafico():
    # setup the figure and axes
    fig = plt.figure(figsize=(5, 5))
    ax1 = fig.add_subplot(111, projection='3d')

    # fake data
    _z = np.arange(119)
    _a = np.arange(1,296)
    _zz, _aa = np.meshgrid(_z, _a)
    z, a = _zz.ravel(), _aa.ravel()

    top = x + y
    bottom = np.zeros_like(top)
    width = depth = 0.5

    ax1.bar3d(z, a, bottom, width, depth, top, shade=True)
    ax1.set_title('Shaded')

    plt.show()