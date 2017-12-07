#Autor: Jonas Deichelmann
#File: root.py
#Class: CST205
#Created by: Jonas Deichelmann
#Description: This is the function Source file for the final project. The File get the Input String from the user and works with this
#Created on: 11/21/2017
#Last change: 12/07/2017

import random
import math

def createRondom(myInput):
    randomNumber = int(random.uniform(60,90))
    randomNumber1 = randomNumber/myInput
    randomNumber = randomNumber*randomNumber1
    if int(randomNumber) > 100:
        createRondom(int(randomNumber))
    if int(randomNumber) < 20:
        createRondom(int(randomNumber))
    return int(randomNumber)

out = []
inp = input()
for i in inp:
    out.append(ord(i))
for j in range(len(out)):
    print(out[j])
    temp = createRondom(int(out[j]))
    out[j]=temp
print(out)
#return out
