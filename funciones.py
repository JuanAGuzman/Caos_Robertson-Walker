from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
from scipy.integrate import odeint
import seaborn as sns
sns.set_theme()

def H(a, p, pa, pp):
    ac, pc, pac, ppc = a**2, p**2, pa**2, pp**2
    return 

def V(a, p, m, k):
    ac, pc, mc = a**2, p**2, m**2
    return 0.5*(k*pc - k*ac + mc*ac*pc)

def ecuaciones(x, t, m, k):
    a, p, pa, pp =  x[0], x[1], x[2], x[3]
    ac, pc, mc = a**2, p**2, m**2
    return [-pa, pp, a*(k - mc*pc), -p*(k + mc*ac)]


def modelo(x, n, dt, m):
    mc = m**2
    t, a, p, pa, pp = x[0], x[1], x[2], x[3], x[4]
    for i in range(n):
        ac, pc = a[i]**2, p[i]**2
        t.append(t[i]+dt)
        a.append(a[i] - pa[i]*dt)
        p.append(p[i] + pp[i]*dt)
        pa.append(pa[i] + a[i]*(1 + mc*pc)*dt)
        pp.append(pp[i] + p[i]*(1 - mc*ac)*dt)
    return t, [a, p, pa, pp]

def dinamica(x0, t, m, k):
    t0 = np.arange(t[0], t[1], t[2])
    return t0, odeint(ecuaciones, x0, t0, args=(m,k))

def superficie(f, xi, xf, yi, yf, n, m, k):
    x = linspace(xi,xf,n)
    y = linspace(yi,yf,n)
    X, Y = meshgrid(x, y)
    Z = f(X, Y, m, k)
    return [X,Y,Z,x,y]

def poincare(a0, p0, pp0, t, m, k):
    V0 = V(a0, p0, m, k) #Potencial en el punto inicial
    pa0 = sqrt(pp0**2 + 2*V0)
    x0 = [a0, p0, pa0, pp0] #Vector de estado inicial
    
    t0, sol = dinamica(x0, t, m, k)
    a, p, pa, pp   = sol[:, 0], sol[:, 1], sol[:, 2], sol[:, 3]

    prueba = 0.0
    zeros = array([[],[]])
    i = 0
    while i < (a.shape[0]-1):
        if ((a[i] < prueba) and (a[i+1] > prueba)) or ((a[i] > prueba) and (a[i+1] < prueba)):
            puntos = array([[0.5*(p[i]+p[i+1])], [0.5*(pp[i]+pp[i+1])]])
            zeros = hstack((zeros,puntos))
        i = i + 1
    return zeros

def cor(a0, p0, pp0, t, m, k):
    V0 = V(a0, p0, m, k) #Potencial en el punto inicial
    pa0 = sqrt(pp0**2 + 2*V0)
    x0 = [a0, p0, pa0, pp0] #Vector de estado inicial
    
    t0, sol = dinamica(x0, t, m, k)
    a, p, pa, pp   = sol[:, 0], sol[:, 1], sol[:, 2], sol[:, 3]

    prueba = 0.0
    zeros = array([[],[]])
    i = 0
    while i < (a.shape[0]-1):
        if ((a[i] < prueba) and (a[i+1] > prueba)) or ((a[i] > prueba) and (a[i+1] < prueba)):
            puntos = array([[0.5*(p[i]+p[i+1])], [0.5*(pp[i]+pp[i+1])]])
            zeros = hstack((zeros,puntos))
        i = i + 1
    return zeros

def orbita(a0, p0, pp0, t, m, k):
    V0 = V(a0, p0, m, k)
    pa0 = sqrt(pp0**2+ 2*V0)
    x = [a0, p0, pa0, pp0]
    t0, sol = dinamica(x, t, m, k)
    return sol

def lyapunov(a0, p0, pp0, t, d, m, k):
    V0 = V(a0, p0, m, k)
    pa0 = sqrt(pp0**2 + 2*V0)
    x = [a0,p0,pa0,pp0]
    t0, Sol = dinamica(x, t, m, k)
    V0d = V(a0+d, p0, m, k)
    pa0d = sqrt(pp0**2 + 2*V0d)
    xd = [a0+d, p0, pa0d, pp0]
    t0, Sold = dinamica(xd, t, m, k)
    da0, dp0, dpa0, dpp0 = d, 0, pa0d - pa0, 0
    a, p, pa, pp = Sol[:, 0], Sol[:, 1], Sol[:, 2], Sol[:, 3]
    ad, pd, pad, ppd = Sold[:, 0], Sold[:, 1], Sold[:, 2], Sold[:, 3]
    da, dp, dpa, dpp  = ad-a, pd-p, pad-pa, ppd-pp 
    s0 = sqrt(da0**2 + dp0**2 + dpa0**2 + dpp0**2)
    s = sqrt(da**2 + dp**2 + dpa**2 + dpp**2)
    Lambda = (log(s/(s0)))/(t0)    
    return [Lambda,t0]

def graph2D(Sol, p, m):
    figure()
    plot(Sol[:,0],Sol[:,1],linewidth=0.1)
    xlabel('$a$')
    ylabel('$\\varphi$')
    savefig('C:\\Users\\juan1\\Downloads\\ProyectoFinal\\Imagenes\\orbitas2d_pp'+str(p)+'_m'+str(m)+'.png')
    show()

def graph3D(Sol, p, m):
    fig = figure()
    ax = fig.add_subplot(111, projection='3d')
    cset = ax.plot(Sol[:,1],Sol[:,0],Sol[:,3],linewidth=0.1)
    ax.clabel(cset, fontsize=9, inline=1)
    ax.set_xlabel('$\\varphi$')
    ax.set_ylabel('$a$')
    ax.set_zlabel('$P_\\varphi$')
    savefig('C:\\Users\\juan1\\Downloads\\ProyectoFinal\\Imagenes\\orbitas3d_pp'+str(p)+'_m'+str(m)+'.png')
    show()

def g(x, y, *args):
    plot(x, y)
    title(args[0])
    xlabel(args[1])
    ylabel(args[2])
    if args[3]:
        savefig(args[4])
    show()


