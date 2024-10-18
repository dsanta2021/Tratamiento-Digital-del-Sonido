# %matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
import statistics

xtrain = np.load('xtrain.npy')
Htrain_norm_ext = np.load('Htrain_norm_ext.npy')
Htest_norm_ext = np.load('Htest_norm_ext.npy')
xtest = np.load('xtest.npy')
theta = np.load('theta.npy')

print(theta)
#Quito características 3, 4, 6 y 8
Htrain_2 = Htrain_norm_ext.take([0,1,2,5,7],axis=1)
Htest_2 = Htest_norm_ext.take([0,1,2,5,7],axis=1)

#Cálculo nuevo theta
theta_2 = np.dot(np.linalg.pinv(Htrain_2), xtrain)

#Valor nuevo antígeno
xest  = np.dot(Htest_2, theta_2)
error = np.linalg.norm(xtest-xest)

#Error cuadrático medio
mse_2 = ((xest-xtest)**2).mean()
print(mse_2)

#Plotting valores estimados vs valores reales
fig = plt.figure(figsize=(14,5))
ax = fig.subplots()
ax.plot(xest,'rx')
ax.plot(xtest,'.')
plt.show()
#--------------------------------------------------------------#
#Quito característica 3, 6 y 7
Htrain_3 = Htrain_norm_ext.take([0,1,2,4,5,8],axis=1)
Htest_3 = Htest_norm_ext.take([0,1,2,4,5,8],axis=1)

#Cálculo nuevo theta
theta_3 = np.dot(np.linalg.pinv(Htrain_3), xtrain)

#Valor nuevo antígeno
xest  = np.dot(Htest_3, theta_3)
error = np.linalg.norm(xtest-xest)

#Error cuadrático medio
mse_3 = ((xest-xtest)**2).mean()
print(mse_3)

#Plotting valores estimados vs valores reales
fig = plt.figure(figsize=(14,5))
ax = fig.subplots()
ax.plot(xest, 'rx')
ax.plot(xtest, '.')
plt.show()