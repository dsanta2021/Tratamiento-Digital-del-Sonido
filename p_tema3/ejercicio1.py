# %matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
from scipy import io  # Para cargar archivos .mat
import statistics

dat = io.loadmat('prostate_data.mat')
keys = dat.keys()
print(keys)
# Extraemos las variables con las que queremos trabajar
Htrain = dat['Htrain']
Htest = dat['Htest']
xtrain = dat['xtrain']
xtest = dat['xtest']
np.save('xtrain', xtrain)
np.save('xtest', xtest)

i = 1  # indice de subplots
plt.figure(figsize=(15, 7))
for num in range(Htrain.shape[1]):
    plt.subplot(2, 4, i)
    plt.hist(Htrain[:, num], bins=10, color='#0504aa',
             alpha=0.7, rwidth=0.85)
    i = i + 1

plt.show()


# Función normalizado de datos
def normdatos(Htrain, Htest):
    nt, nfeat = Htrain.shape
    Hntrain = np.zeros(np.shape(Htrain))
    Hntest = np.zeros(np.shape(Htest))
    for num in range(Htrain.shape[1]):
        mu = statistics.mean(Htrain[:, num])
        sigma = statistics.stdev(Htrain[:, num])
        Hntrain[:, num] = (Htrain[:,num]-mu) / sigma
        Hntest[:, num] = (Htest[:,num]-mu) / sigma

    return Hntrain, Hntest


# Llamada a normalizado de datos
Htrain_norm, Htest_norm = normdatos(Htrain, Htest)

np.save('Htrain_norm', Htrain_norm)
np.save('Htest_norm', Htest_norm)

# Plotting datos normalizados
plt.figure(figsize=(15, 7))
i = 1  # indice de subplots
for num in range(Htrain_norm.shape[1]):
    plt.subplot(2, 4, i)
    plt.hist(Htrain_norm[:, num], bins=10, color='#0504aa',
             alpha=0.7, rwidth=0.85)

    i = i + 1

plt.show()