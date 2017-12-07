"""
Author: David Wong
File: page.py
Class: CST 205
Description: The background Flask code for our project. This is an early prototype for the webpage.
Date: 12/6/2017
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from pprint import pprint

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		mood = request.form['mood']
		sentence = request.form['sentence']
		return redirect(url_for('test', test_mood=mood, test_text=sentence))
	return render_template('index.html')
	
@app.route('/test')
def test():
	return render_template('test.html')