import sys
import scipy.signal as sig
from tds_utils import predlin
import scipy.io.wavfile as wf
import matplotlib.pyplot as plt
import numpy as np
import os
import ffmpeg
sys.path.append('../')


audio_file_train = os.listdir('vocals')
audio_file_test = os.listdir('Audios')


def lpc_train():
    lpc_train = []
    vocals_train = []

    for audio in audio_file_train:
        audio_path = os.path.join('vocals', audio)
        fs, y = wf.read(audio_path)

        # obtain frame s2
        s2 = y[0:240]
        # print(y.shape)
        # LPC order
        p = 12
        N = int(fs*0.03)    # length in samples
        h = sig.hamming(N)  # hamming window

        # Extracción y guardado de características
        lpc_coef = predlin(s2, p, h)
        lpc_train.append(lpc_coef.tolist())
        # print(lpc_coef)
        # print(lpc_train)

        # print('Coeficientes LPC:', lpc_coefs)

        # Guardado de etiquetas
        vocal = audio.split('_')[0]
        if vocal == 'A' or vocal == 'a':
            vocals_train.append('a')
        if vocal == 'E' or vocal == 'e':
            vocals_train.append('e')
        if vocal == 'I' or vocal == 'i':
            vocals_train.append('i')
        if vocal == 'O' or vocal == 'o':
            vocals_train.append('o')
        if vocal == 'U' or vocal == 'u':
            vocals_train.append('u')

        # Gráfica de los coeficientes LPC
        # plt.title(n)
        # plt.show()

    lpc_train = np.array(lpc_train)
    vocals_train = np.array(vocals_train)
    # print(lpc_train)

    return lpc_train, vocals_train


def lpc_test():
    lpc_test = []
    vocals_test = []

    for audio in audio_file_test:
        audio_path = os.path.join('Audios', audio)
        audio_mono = None
        # for i in audio_path:
        #     audio_mono = ffmpeg -i stereo.wav -ac 1 mono.wav
        fs, y = wf.read(audio_path)

        # obtain frame s2
        s2 = y[0:240]
        # print(y.shape)
        # LPC order
        p = 12

        N = int((fs-40000) * 0.03)  # length in samples
        h = sig.hamming(N)  # hamming window

        # Extracción y guardado de características
        lpc_coef = predlin(s2, p, h)
        lpc_test.append(lpc_coef.tolist())
        # print('Coeficientes LPC:', lpc_coefs)

        # Guardado de etiquetas
        vocal = audio.split('_')[0]
        if vocal == 'A' or vocal == 'a':
            vocals_test.append('a')
        if vocal == 'E' or vocal == 'e':
            vocals_test.append('e')
        if vocal == 'I' or vocal == 'i':
            vocals_test.append('i')
        if vocal == 'O' or vocal == 'o':
            vocals_test.append('o')
        if vocal == 'U' or vocal == 'u':
            vocals_test.append('u')

        # Gráfica de los coeficientes LPC
        # plt.title(n)
        # plt.show()

    lpc_test = np.array(lpc_test)
    vocals_test = np.array(vocals_test)
    # print(lpc_test)
    # print(vocals_test)

    return lpc_test, vocals_test
lpc_train()
lpc_test()
