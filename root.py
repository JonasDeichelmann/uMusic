#Autor: Jonas Deichelmann
#File: root.py
#Class: CST205
#Created by: Jonas Deichelmann
#Description: This is the root Source file for the final project
#Created on: 11/16/2017
#Last change: 11/21/2017

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
@app.route('/index')
def template_func():

    #create randomNumber for the next Step, when we want to create random music
    return render_template('template.html')
