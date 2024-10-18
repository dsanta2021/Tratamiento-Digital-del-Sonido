from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.naive_bayes import GaussianNB
import MFCC as mfcc
import LPC as lpc

# Base de Datos MFCCs
X_train_mfcc, y_train_mfcc = mfcc.mfcc_train()
X_test_mfcc, y_test_mfcc = mfcc.mfcc_test()

# Base de Datos LPC
X_train_lpc, y_train_lpc = lpc.lpc_train()
X_test_lpc, y_test_lpc = lpc.lpc_test()
#print(X_train_lpc)
#print(y_train_lpc)

# ################################ TRAIN  ################################ #

# Se crea el modelo de NB
model_NB_mfcc = GaussianNB()
model_NB_lpc = GaussianNB()

# Entrenamiento
model_NB_mfcc.fit(X_train_mfcc, y_train_mfcc)
model_NB_lpc.fit(X_train_lpc, y_train_lpc)

# Media y desviación estándar para las características de cada clase:
print("Media de la gaussiana para cada clase:\n Columnas = Características \n Filas = Clases\n")
#print(model_NB_mfcc.theta_)
#print('LPC', model_NB_lpc.theta_)
print("Desviación estándar de la gaussiana para cada clase:\n Columnas = Características \n Filas = Clases\n")
#print(model_NB_mfcc.sigma_)


# ################################ TEST  ################################ #

# Se predicen las muestras de test, utilizando los valores de la función estimados anteriormente en train
y_hat_NB_mfcc = model_NB_mfcc.predict(X_test_mfcc)
y_hat_NB_lpc = model_NB_lpc.predict(X_test_lpc)

# Se calcula el accuracy (exactitud = nº de actiertos/nº de casos totales)
acc_NB_mfcc = np.mean(y_test_mfcc == y_hat_NB_mfcc)
print('MFCC')
print(acc_NB_mfcc)
print(y_hat_NB_mfcc)
print(y_test_mfcc)

acc_NB_lpc = np.mean(y_test_lpc == y_hat_NB_lpc)
print('LPC')
print(acc_NB_lpc)
print(y_hat_NB_lpc)
print(y_test_lpc)
