import librosa
import librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt
from functools import reduce
import numpy as np
import os

audio_file_train = os.listdir('vocals')  # Pensar en meter mas de cinco vocales
audio_file_test = os.listdir('test_vocals')  # Audios grabados con nuestras voces


# Train
def mfcc_train():
    mffc_train = []
    vocals_train = []

    for audio in audio_file_train:
        audio_path = os.path.join('vocals', audio)
        signal, fs = librosa.load(audio_path)

        # Extract MFCCs
        mfccs = librosa.feature.mfcc(y=signal, n_mfcc=15, sr=fs)
        mel = []
        for i in mfccs:
            mel_number = reduce(lambda x, y: x + y, i) / len(i)
            # print(mel_number)
            mel.append(mel_number)
            # print(mel)
        mffc_train.append(mel)
        # print(mffc_train)               # Guardado de características

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

        # print(vocals_train)
    # print(mffc_train)
        # visualize MFCCs
        # plt.figure(figsize=(10, 5))
        # librosa.display.specshow(mfccs, x_axis='time', sr=fs)
        # plt.colorbar(format="%+2f")
        # plt.title(vocal)
        # plt.show()

    mffc_train = np.array(mffc_train)
    vocals_train = np.array(vocals_train)
    # print('TRAIN')
    # print(mffc_train)
    # print(vocals_train)

    return mffc_train, vocals_train


# Test
def mfcc_test():
    mfcc_test = []
    vocals_test = []

    for audio in audio_file_test:
        audio_path = os.path.join('test_vocals', audio)
        signal, fs = librosa.load(audio_path)

        # Extract MFCCs
        mfccs = librosa.feature.mfcc(y=signal, n_mfcc=15, sr=fs)
        mel = []
        for i in mfccs:
            mel_number = reduce(lambda x, y: x + y, i) / len(i)
            mel.append(mel_number)
        mfcc_test.append(mel)   # Guardado de características
        # print(mfcc_test)

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

    mfcc_test = np.array(mfcc_test)
    vocals_test = np.array(vocals_test)
    # print('TEST')
    # print(mfcc_test)
    # print(vocals_test)

    return mfcc_test, vocals_test
