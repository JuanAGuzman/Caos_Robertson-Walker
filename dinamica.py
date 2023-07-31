import os
from funciones import *

def P(a, pa, pp, m):
    ac, pac, ppc, mc = a**2, pa**2, pp**2, m**2
    return (pac-ppc)/(mc*ac)

#x = [0, 0.1,0.01,-1,2]
#t, a, p = dinamica(x, 1,1000,0.01, 1)

#x = [0, 0.1,0.01,-2,1]
#t, a, p = dinamica(x, 1,100,0.01,1)

#x = [0, 0.1,0.01,-2,0.1]
#t, a, p = dinamica(x, 1,4500,0.01,1)


t0 = [0, 80, 0.1]
a, pa, pp, p = 3,-2, -0.75, -1
a, pa, pp, p = 1,1.032, 0.255, 0.75
#p = P(a, pa, pp, 1)
#print(p) 

x, m, k = [a, p, pa, pp], 1, 1
t, sol = dinamica(x, t0, m, k)
g(t, sol[:, 0], 'Dinamica del factor de escala', 'Tiempo', '$a$', True, 'C:\\Users\\juan1\\Downloads\\ProyectoFinal\\Imagenes\\dinamica_a_k'+str(k)+'a'+str(a)+'p'+str(p)+'pa'+str(pa)+'pp'+str(pp)+'.png')
g(t, sol[:, 1], 'Dinamica del campo', 'Tiempo', '$\\varphi$', True, 'C:\\Users\\juan1\\Downloads\\ProyectoFinal\\Imagenes\\dinamica_p_k'+str(k)+'a'+str(a)+'p'+str(p)+'pa'+str(pa)+'pp'+str(pp)+'.png')





