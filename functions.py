#Autor: Jonas Deichelmann
#File: root.py
#Class: CST205
#Created by: Jonas Deichelmann
#Description: This is the function Source file for the final project. The File get the Input String from the user and works with this
#Created on: 11/21/2017
#Last change: 12/07/2017

import random
import math

def makeMelody(randInput):
    melody = []
    for i in range(len(randInput)-1):
        if abs(int(randInput[i])-int(randInput[i+1])) > 2:
            k=0
            for j in range(int(abs(int(randInput[i])-int(randInput[i+1]))/2)):
                if randInput[i]> randInput[i+1]:
                    melody.append(randInput[i]-k)
                else:
                    melody.append(randInput[i]+k)
                k += 2
        else:
            melody.append(randInput[i])
    return melody

def createRondom(myInput):
    randomNumber = int(random.uniform(60,90))
    randomNumber1 = randomNumber/myInput
    randomNumber = randomNumber*randomNumber1
    if int(randomNumber) > 100:
        createRondom(int(randomNumber))
    if int(randomNumber) < 20:
        createRondom(int(randomNumber))
    return int(randomNumber)
