from random import choice
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def random():
    with open('data.json', mode='r') as lyrics:
        response = json.load(lyrics)
        return choice(response)

@app.route('/add')
def add():
    return render_template('add.html')