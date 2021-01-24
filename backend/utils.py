#!/usr/bin/env python
# coding: utf-8

import os
import io
import re
import sys
import json
from scipy.io import wavfile
from os.path import dirname
import pymorphy2
import audiosegment


def voice_activity_detection(fname):
    signal = audiosegment.from_file(fname) 
    signal = signal.resample(sample_rate_Hz=64000, sample_width=2, channels=1)
    signal = signal.filter_silence(duration_s=0.5, threshold_percentage=1.0)
    dir = os.path.dirname(fname)
    new_fname = fname.replace(dir, dir+'aftervad')
    new_dir = dirname(new_fname)
    if not os.path.exists(dirname(new_dir)):
        os.mkdir(dirname(new_dir))
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    signal.export(new_fname, format="wav") 
    return new_fname


def get_wav_signal(fname):
    sound_after_vad = voice_activity_detection(fname)
    fs, signal = wavfile.read(sound_after_vad)
    if len(signal.shape) != 1:  # to mono
        signal = signal[:, 0]
    os.remove(sound_after_vad)
    return fs, signal

# for comparison


def get_normal_form(word):
    """
    normal form of one word
    :param word:
    :return:
    """
    morph = pymorphy2.MorphAnalyzer()
    return morph.normal_forms(word)[0]


def normalize_text(text):
    return ' '.join([get_normal_form(one) for one in re.findall(r'\w+', text)])


def compare_vectors(vec1, vec2):
    count = 0
    for i, one in enumerate(vec1):
        if one == vec2[i]:
            count += 1
    return count/len(vec1)


# other


def load_json(path):
    with open(path, "r") as file:
        text = file.read()
        out = json.loads(text)
        if out:
            return out
        else:
            sys.stdout.write("Error in reading transriptions from file.")
            return None
