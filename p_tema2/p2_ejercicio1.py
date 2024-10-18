#### EJERCICIO 1 ####

# %matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
from random import randint, uniform, random #Otra forma de usar función random en lugar de con numpy

#Parámetros ejercicios
mu0 = -1
mu1 = 1
sigma0 = 1
sigma1 = 1
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
