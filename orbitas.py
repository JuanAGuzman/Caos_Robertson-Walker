from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
from funciones import *


t = [0, 1000, 0.02]


a0, p0, pp0, m, k = 3, -2, 0.75, 1, 1
a0, p0, pp0, m, k = 1, 0.75, 0.255, 1, 1

a0, p0, pp0, m, k = 1, 0.75, 0.255, 1, 1

sol = orbita(a0, p0, pp0, t, m, k)
graph2D(sol, pp0, m)
graph3D(sol, pp0, m)

"""
pp = linspace(-2, 2, 5)
m = linspace(0, 1, 3)
for i in pp:
    for j in m:
        sol = orbita(a0, p0, i, t, j, k)
        graph2D(sol, i, j)
        graph3D(sol, i, j)
"""


