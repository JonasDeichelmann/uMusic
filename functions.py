#Autor: Jonas Deichelmann
#File: root.py
#Class: CST205
#Created by: Jonas Deichelmann
#Description: This is the function Source file for the final project. The File get the Input String from the user and works with this
#Created on: 11/21/2017
#Last change: 12/08/2017

import random
import math

#This function adds all the Steps between the main notes
def makeMelody(randInput):
    melody = []
    for i in range(len(randInput)-1):
        #Checks if the distance between the two notes is bigger then 2, if so then generate the numbers between
        if abs(int(randInput[i])-int(randInput[i+1])) > 2:
            k=0
            #As many steps as the two notes are away from each other, divided by 2
            for j in range(int(abs(int(randInput[i])-int(randInput[i+1]))/2)):
                #check wich way it have to go
                if randInput[i]> randInput[i+1]:
                    melody.append(randInput[i]-k)
                else:
                    melody.append(randInput[i]+k)
                k += 2
        else:
            melody.append(randInput[i])
    return melody

#This function creates an random number between 20 and 100, with the user input and then returns the randomNumber
def createRondom(myInput):
    #create a randomNumber between 50 and 90
    randomNumber = int(random.uniform(50,90))
    #Divide the randomNumber by the ASII input
    randomNumber1 = randomNumber/myInput
    #Multiply the randomNumber with the new divided randomNumber
    randomNumber = randomNumber*randomNumber1
    #if the randomNumber is to big, then create a new one
    if int(randomNumber) > 100:
        createRondom(int(randomNumber))
    #if the randomNumber is to small, then creat a new one
    if int(randomNumber) < 20:
        createRondom(int(randomNumber))
    # return the randomNumber, since it is okay
    return int(randomNumber)

def handleInput(myInput):
    out = []
    inp = myInput
    #Converting each character from the input into an ASCII Number and add these to the list
    for i in inp:
        out.append(ord(i))
    for j in range(len(out)):
        #Call the random function with the ASCII Letter
        temp = createRondom(int(out[j]))
        out[j]=temp
    #Create the steps between the numbers
    out = makeMelody(out)
    return(out)
