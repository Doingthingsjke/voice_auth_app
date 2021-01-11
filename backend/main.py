import hashlib
import flask
from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory, jsonify
from flask_cors import CORS
from voice_authentication import Authenticator

app = Flask(__name__)
a = Authenticator('./data/legitim_user')

CORS(app)

@app.route('/signin', methods=['GET','POST'])
def get_os_name():
    print(a.authenticate('./data/test/m09.wav'))


# TO DO: брать true_text не из транскрипции

# Брать звук из POST-запроса

# при прохождении проверки что-то вроде личного кабинета, реферрер

if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)
