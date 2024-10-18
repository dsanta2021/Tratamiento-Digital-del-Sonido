# %matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np

xtrain = np.load('xtrain.npy')
Htrain_norm_ext = np.load('Htrain_norm_ext.npy')

#Coeficientes theta
theta = np.dot(np.linalg.pinv(Htrain_norm_ext), xtrain) #np.dot para hacer operación matricial (* da error por dimensiones)

np.save('theta', theta)