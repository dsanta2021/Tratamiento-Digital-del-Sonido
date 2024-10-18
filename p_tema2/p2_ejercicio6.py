#### EJERCICIO 4 ####

# 1

# %matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
from random import randint, uniform, random #Otra forma de usar función random en lugar de con numpy

#Parámetros ejercicios
mu0 = -1
mu1 = 1
sigma0 = 1
sigma1 = 2
p0 = 0.7
p1 = 0.3

N = 1000 #Secuencia números aleatorios

#Generación de N números aleatorios entre 0 y 1
x = np.random.rand(N)

#x = [random() for _ in range(N)]  #otra forma de usar función random
#Si uso random (no numpy) convierto en array para poder realizar la operación de resta posterior
#np_x = np.asarray(x)

# 70% de elementos = -1 y 30% = 1
x = np.sign(x-p0)
np.save('x',x)


#Compruebo porcentaje de valores de 1s y -1s
sum_pos = sum(x==1)/N
sum_neg = sum(x==-1)/N

#Genero variable aleatoria n con distribución normal o gaussiana
n = np.random.randn(N) * sigma0


#Variable aleatoria x
xn = x + n
np.save('xn',xn)


#Histograma variable aleatoria xn
plt.hist(xn, bins=100)
plt.show()   # Para que se muestre solo el histograma


#### 2 ####
mu0 = -1
mu1 = 1
sigma0 = 1
sigma1 = 2
p0 = 0.7
p1 = 0.3

N = 1000 #Secuencia números aleatorios

X = np.linspace(-5,5,N);
#Verosimilitud
fx_H0 = norm.pdf(X, mu0, sigma0)
fx_H1 = norm.pdf(X, mu1, sigma1)

#Umbrales
g_ML =
np.save('g_ML', g_ML)
g_MAP =
np.save('g_MAP', g_MAP)

#plotting
fig = plt.figure(figsize=(7,5))
ax = fig.subplots()
ax.plot(X, fx_H0*p0)
ax.plot(X, fx_H1*p1, 'r')
line_ML = mlines.Line2D([g_ML, g_ML], [0, max(fx_H0*p0)], color='g')
ax.add_line(line_ML)
line_MAP = mlines.Line2D([g_MAP, g_MAP], [0, max(fx_H0*p0)], color='y')
ax.add_line(line_MAP)
legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.grid()
plt.show()


#plotting
fig = plt.figure(figsize=(7,5))
ax = fig.subplots()
ax.plot()
ax.plot()
line_ML =
ax.add_line(line_ML)
line_MAP =
ax.add_line(line_MAP)
legend = ax.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.grid()
plt.show()


#### 3 ####
 #%matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('../') #allows to import a module in a diff folder
from tds_utils import prob_error

#Load variables
g_MAP = np.load('g_MAP_new_sigma.npy')
g_ML = np.load('g_ML_new_sigma.npy')
x = np.load('x_new_sigma.npy')
xn = np.load('xn_new_sigma.npy')


#Cálculo probabilidad de error
Pe_ML, pd_ML, pf_ML  = prob_error()
Pe_MAP, pd_MAP, pf_MAP = prob_error()
print(Pe_ML)
print(Pe_MAP)


#4
# %matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('../') #allows to import a module in a diff folder
from tds_utils import prob_error

x = np.load('x_new_sigma.npy')
xn = np.load('xn_new_sigma.npy')

gamma =

Pe = np.zeros(np.size(gamma));
pd = np.zeros(np.size(gamma));
pf = np.zeros(np.size(gamma));

#Probabilidad de error para cada gamma
for  in range :
    (, , ) = prob_error();

#Plotting
plt.figure(figsize = (7,5))
plt.plot();
plt.xlabel('')
plt.ylabel('')
plt.show()


#5
# %matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('../') #allows to import a module in a diff folder
from tds_utils import prob_error

x = np.load('x_new_sigma.npy')
xn = np.load('xn_new_sigma.npy')

gamma =

Pe = np.zeros(np.size(gamma));
pd = np.zeros(np.size(gamma));
pf = np.zeros(np.size(gamma));

#Probabilidad de detección y falsa alarma
for  in range :
    (, , ) = prob_error()

#Plotting
plt.figure(figsize = (7,5))
plt.plot();
plt.xlabel('')
plt.ylabel('')
plt.show()