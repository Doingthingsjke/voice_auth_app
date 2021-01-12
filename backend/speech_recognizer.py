import os
import sys
import json
import wave
from vosk import Model, KaldiRecognizer, SetLogLevel


class Recognizer(object):
    def __init__(self):
        self.model_path = "./model"
        self.set_up()
        self.model = Model(self.model_path)

    def set_up(self):
        """
        set up vosk
        :return:
        """
        if not os.path.exists(self.model_path):
            print("Please download the model from "
                  "https://github.com/alphacep/vosk-api/blob/master/doc/models.md "
                  "and unpack as 'model' in the current folder.")
            exit(1)
        SetLogLevel(level=0)

    def recognize(self, path):
        try:
            wf = wave.open(path, "rb")
            if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
                sys.stdout.write("Audio file must be WAV format mono PCM. \n")
                exit(1)
            rec = KaldiRecognizer(self.model, wf.getframerate())
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if rec.AcceptWaveform(data):
                    pass
                else:
                    pass
            text = rec.FinalResult()
            return json.loads(text)['text']
        except:
            return ""
