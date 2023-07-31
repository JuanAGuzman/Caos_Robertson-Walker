from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
from funciones import *
import os


def graphLyapunov(a0, p0, pp0, t, d, m, k):
    Lambdas = lyapunov(a0, p0, pp0, t,d, m, k)
    plot(Lambdas[1],Lambdas[0],linewidth=0.3)
    const0 = zeros(Lambdas[1].shape)
    plot(Lambdas[1],const0)
    xlabel('Tiempo')
    ylabel('Lambda')
    #ylim(-0.02,0.02)
    savefig('C:\\Users\\juan1\\Downloads\\ProyectoFinal\\Imagenes\\lyapunov_a'+str(a0)+'_p'+str(p0)+'_pp'+str(pp0)+'_k'+str(k)+'_m'+str(m)+'.png')
    show()

#t = [10, 120, 1]
#a0, p0, pp0, m, k, d = 0, 0, 1, 1, 1, 0.001
#t = [10, 40, 1]
#a0, p0, pp0, m, k, d = 0.1, 0.1, 1, 1, 1, 0.001

t = [10, 160, 0.0001]
a0, p0, pp0, m, k, d = 3, -4, -0.75, 1, 1, 0.1

graphLyapunov(a0, p0, pp0, t, d, m, k)