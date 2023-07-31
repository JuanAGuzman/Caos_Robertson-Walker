from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
from funciones import *


def graphPoincare(b, c, n, t, ds, m, k):
    p0 = linspace(b[0], b[1], n)
    pp0 = linspace(c[0], c[1], n)
    fig, ax = subplots()
    for i in range(n):
        for j in range(n):
            zeros = poincare(0,p0[i],pp0[j],t, m, k)
            texto ='$\\varphi=$' + str(p0[i]) + ' , $P_\\varphi =$' + str(pp0[j])
            ax.scatter(zeros[0], zeros[1], s = ds,label = texto, marker = ".")
    
    ax.set_xlabel("$a$")
    ax.set_ylabel("$P_a$")
    xlim(-15,15)
    ylim(-15,15)
    Thetitle = "Mapa de Poincaré"
    ax.set_title(Thetitle)
    savefig('C:\\Users\\juan1\\Downloads\\ProyectoFinal\\Imagenes\\poincare22_p'+str(b)+'_pp'+str(c)+'_k'+str(k)+'_m'+str(m)+'.png')
    show()
    #pos = ax.get_position()
    #ax.set_position([pos.x0, pos.y0, pos.width, pos.height * 0.85])
    #ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.35), ncol=3)


b, c, t = [0, 1.8], [0, 1.5], [0, 2000, 0.1]
ds, m, k = 0.3, 1, 1
#m = [0, 0.25, 0.5, 0.75, 1]
#for i in m:
#    graphPoincare(b, c, 10, t, ds, i, 1)

graphPoincare(b, c, 10, t, ds, m, k)