# %matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
import statistics

Htest_norm_ext = np.load('Htest_norm_ext.npy')
xtest = np.load('xtest.npy')
theta = np.load('theta.npy')

#Valor antígeno
xest  = np.dot(Htest_norm_ext,theta)
error = np.linalg.norm(xtest-xest)

#Error cuadrático medio
mse_1 = ((xest-xtest)**2).mean()
print(mse_1)

#Plotting valores estimados vs valores reales
fig = plt.figure(figsize=(14,5))
ax = fig.subplots()
ax.plot(xest,'rx')
ax.plot(xtest,'.')
plt.show()