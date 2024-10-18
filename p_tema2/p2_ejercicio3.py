#### EJERCICIO 3 ####

# %matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('../')  # allows to import a module in a diff folder
from tds_utils import prob_error

#Load variables
g_MAP = np.load('g_MAP.npy')
g_ML = np.load('g_ML.npy')
x = np.load('x.npy')
xn = np.load('xn.npy')


# Cálculo probabilidad de error
Pe_ML, pd_ML, pf_ML  = prob_error(xn, x, g_ML)
Pe_MAP, pd_MAP, pf_MAP = prob_error(xn, x, g_MAP)
print(Pe_ML)
print(Pe_MAP)