import os
import glob
from shutil import move

def file_cleaner(path):
    files = glob.glob(path)  # теперь dirs-массив директорий
    for one in files:
        basename = os.path.basename(one)
        cv = "common_voice_ru_"
        if basename.startswith(cv):
            new = one.replace(cv, "a")
            move(one, new)
        else:
            new = one
        file_size = os.stat(new).st_size / 1024
        print(file_size)
        if file_size < 600:
            os.remove(new)



file_cleaner('/home/anna/Загрузки/voice-auth/data/телка/*')
