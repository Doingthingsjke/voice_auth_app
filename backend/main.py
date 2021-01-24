import os
import flask
import time
import shutil
import random
import subprocess
from hashlib import sha256
from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory, jsonify
from flask_cors import CORS
from voice_authentication import Authenticator
from utils import load_json

#initial values
INIT_DATA = load_json('./data/signin_transcription.json')
TRUE_TEXT = INIT_DATA["0"]

app = Flask(__name__)
a = Authenticator()
CORS(app)


@app.route('/phrase', methods=['GET'])
def get_phrase():
    global TRUE_TEXT
    if request.method == "GET":
        data = load_json('./data/signin_transcription.json')
        num = random.randint(0,35)
        TRUE_TEXT = data[str(num)]
        return TRUE_TEXT

@app.route('/register_phrase', methods=['GET'])
def get_reg_phrase():
    transcriptions = load_json('./data/reg_transcriptions.json')
    if request.method == "GET":
        return transcriptions

@app.route('/signup', methods=['POST'])
def get_files_from_signup():
    # parse request
    first_name = request.form['first_name']
    second_name = request.form['second_name']
    email = request.form['email']
    leg_dir = './data/' + str(sha256(bytes(email, "utf-8")).hexdigest())
    if os.path.exists(leg_dir):
        return "1"
    else:
        os.mkdir(leg_dir)
        try:
            for i in range(1,10):
                file = request.files['audio'+str(i)]
                # save file from user
                file_name_1 = leg_dir + '/audio' + str(i) + '.opus'
                file.save(file_name_1)
                file_name_2 = file_name_1.replace("opus","wav")
                command = ['ffmpeg', '-i', file_name_1, file_name_2]
                subprocess.run(command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
                os.remove(file_name_1)
            return "Ok"
        except:
            return "0"
        


@app.route('/signin', methods=['POST'])
def get_file():
    # parse request
    email = request.form['email']
    leg_dir = './data/' + str(sha256(bytes(email, "utf-8")).hexdigest())
    if os.path.exists(leg_dir):
        file = request.files['audio']
        # save file from user
        file_name_1 = './data/test/attempt.opus'
        file.save(file_name_1)
        file_name_2 = file_name_1.replace("opus","wav")
        command = ['ffmpeg', '-i', file_name_1, file_name_2]
        subprocess.run(command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
        result = a.authenticate(leg_dir, file_name_2, TRUE_TEXT)
        os.remove(file_name_1)
        os.remove(file_name_2)
        print(result)
        return str(result)
    else:
        return "False"

# TO DO: брать true_text не из транскрипции

# при прохождении проверки что-то вроде личного кабинета, реферрер

if __name__ == "__main__":
    context = ('../frontend/server.crt', '../frontend/server.key')
    app.run('0.0.0.0', 5000, debug=True, ssl_context=context)