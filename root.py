#Autor: Jonas Deichelmann
#File: root.py
#Class: CST205
#Description: This is the root Source file for the final project
#Date: 11/16/2017

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import random

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
@app.route('/index')
def template_func():
    randomNumber = int(random.uniform(0,10))
    print(randomNumber)
    #create randomNumber for the next Step, when we want to create random music
    return render_template('template.html')
