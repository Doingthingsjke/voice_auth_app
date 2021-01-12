import numpy as np
from python_speech_features import mfcc
from python_speech_features import delta


def get_features(fs, signal):
    mfcc_feature = mfcc(signal, fs, nfft=1600)
    d_mfcc_feature = delta(mfcc_feature, 2)
    dd_mfcc_feature = delta(d_mfcc_feature, 2)
    feature = mfcc_feature + d_mfcc_feature + dd_mfcc_feature
    if len(mfcc_feature) == 0:
        raise ValueError
    features = np.mean(feature, axis=0).reshape(13, 1)  # можно еще улучшить
    # print(features.shape)
    return features
