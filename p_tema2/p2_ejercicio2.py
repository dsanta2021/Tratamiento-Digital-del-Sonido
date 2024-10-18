#### EJERCICIO 2 ####

# %matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm  #Para la función norm.pdf
import math  #Para la función logaritmo
import matplotlib.lines as mlines

mu0 = -1
mu1 = 1
sigma0 = 1
sigma1 = 1
p0 = 0.7
p1 = 0.3

N = 1000 #Secuencia números aleatorios

X = np.linspace(-5,5,N);
#Verosimilitud
fx_H0 = norm.pdf(X, mu0, sigma0)
fx_H1 = norm.pdf(X, mu1, sigma1)

#Umbrales
g_ML = 0
np.save('g_ML', g_ML)
g_MAP = 0.42
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