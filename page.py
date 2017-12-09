"""
Author: David Wong
File: page.py
Class: CST 205
Description: The background Flask code for our project. This is an early prototype for the webpage.
Date: 12/6/2017
"""

from generate_music import GenerateMusic
import functions
import pitch
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from pprint import pprint

app = Flask(__name__)
Bootstrap(app)

pitch_dict = pitch.mood
pitch_classes = pitch.pitch_classes

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		mood = request.form['mood']
		sentence = request.form['sentence']
		speed = request.form['speed']
		per_second = 5
		
		pitch = pitch_classes[pitch_dict[mood]]

		if (speed == "Fast"):
			per_second = 7
		
		elif (speed == "Slow"):
			per_second = 3
		
		note_list = functions.handleInput(sentence)
		GenerateMusic(notes_per_second=per_second, input_melody=note_list, pitch_class=pitch)
		return render_template('sound.html')
	return render_template('index.html')
	
@app.route('/test')
def test():
	return render_template('test.html')