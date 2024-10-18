#### EJERCICIO 4 ####

# %matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('../') #allows to import a module in a diff folder
from tds_utils import prob_error

x = np.load('x.npy')
xn = np.load('xn.npy')

gamma = np.linspace(-4,4,20)

Pe = np.zeros(np.size(gamma));
pd = np.zeros(np.size(gamma));
pf = np.zeros(np.size(gamma));

#Probabilidad de detección y falsa alarma
for num in range(np.size(gamma)) :
    (Pe[num], pd[num], pf[num]) = prob_error(xn, x, gamma[num]);

#Plotting
plt.figure(figsize = (7,5))
plt.plot(pf, pd);
plt.xlabel('Pf')
plt.ylabel('Pd')
plt.show()