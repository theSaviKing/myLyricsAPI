from random import choices, choice
from flask import Flask, render_template, redirect, url_for, request
from waitress import serve
import json
import logging

logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

app = Flask(__name__)

@app.route('/')
@app.route('/<int:number>')
def random(number=1):
    with open('data.json', mode='r') as lyrics:
        response = json.load(lyrics)
        if number > 1:
            return choices(response, k=number)
        else:
            return choice(response)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/submit', methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        lyrics = open('data.json', mode='r')
        lyric = json.load(lyrics)
        lyrics.close();
        lyric.append({
            "album": request.form['album'],
            "artist": request.form['artist'],
            "features": request.form['features'],
            "name": request.form['songname'],
            "lyrics": request.form['lyrics']
        })
        json.dump(lyric, open('data.json', mode="w"), indent=4)
        return json.load(open('data.json'))
    else:
        return redirect(url_for('add'))

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8080)