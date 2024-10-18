# %matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np

Hntrain = np.load('Htrain_norm.npy')
Hntest = np.load('Htest_norm.npy')

#Concateno matrices para añadir columna de 1s a la vez a train y test
Hn = np.concatenate((Hntrain,Hntest),axis=0)
Hext = np.concatenate((np.ones((97,1)),Hn),axis=1)

Htrain_norm_ext = Hext[0:67,:]
Htest_norm_ext = Hext[67:,:]

np.save('Htrain_norm_ext', Htrain_norm_ext)
np.save('Htest_norm_ext', Htest_norm_ext)