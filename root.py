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

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
@app.route('/index')
def template_func():
    out = []
    inp = "test"
    for i in inp:
        out.append(ord(i))
    for j in range(len(out)):
        temp = createRondom(int(out[j]))
        out[j]=temp
    out = makeMelody(out)
    print(out)
    #create randomNumber for the next Step, when we want to create random music
    return render_template('template.html')
