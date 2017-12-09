#Autor: Jonas Deichelmann
#File: root.py
#Class: CST205
#Created by: Jonas Deichelmann
#Description: This is the root Source file for the final project
#Created on: 11/16/2017
#Last change: 12/08/2017

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from functions import createRondom
from functions import makeMelody
from functions import handleInput

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
@app.route('/index')
def template_func():
    inp="test"
    noteList=handleInput(inp)
    print(noteList)
    return render_template('template.html')
