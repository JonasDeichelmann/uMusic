#Autor: Jonas Deichelmann
#File: root.py
#Class: CST205
#Created by: Jonas Deichelmann
#Description: This is the function Source file for the final project. The File get the Input String from the user and works with this
#Created on: 11/21/2017
#Last change: 11/21/2017
import random
import math

out = []
inp=input()
for i in inp:
    out.append(int(math.sqrt(math.pow(ord(i), 3))))
for j in range(len(out)-1):
    randomNumber = int(random.uniform(out[j],out[j-1]))
    print(randomNumber)
print(out)
#return out
