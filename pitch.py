#Author: Brandon Ginn
#File: pitch.py
#Class: CST 205
#Description: A dictionary consisting of possible 'pitch classes' that can be fed to Magenta when training 
#Created: 12/01/2017
#Changed: 12/01/2017

mood = {
	"Happy" : "C Major",
	"Sad" : "C Minor",
	"Mad" : "F Major",
	"Chill" : "B Minor"
}

pitch_classes = { 	
	"C Major"	:	"[2, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]",
	"C Minor" 	:	"[2, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]",
	"Db Major" 	:	"[1, 2, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0]",
	"D Major" 	: 	"[0, 1, 2, 0, 1, 0, 1, 1, 0, 1, 0, 1]",
	"D Minor" 	: 	"[1, 0, 2, 0, 1, 1, 0, 1, 0, 1, 1, 0]",
	"D# Minor" 	: 	"[0, 1, 0, 2, 0, 1, 1, 0, 1, 0, 1, 1]",
	"Eb Major" 	: 	"[1, 0, 1, 2, 0, 1, 0, 1, 1, 0, 1, 0]",
	"E Major" 	: 	"[0, 1, 0, 1, 2, 0, 1, 0, 1, 1, 0, 1]",
	"E Minor" 	: 	"[1, 0, 1, 0, 2, 0, 1, 1, 0, 1, 0, 1]",
	"F Major" 	: 	"[1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 1, 0]",
	"F Minor" 	: 	"[1, 1, 0, 1, 0, 2, 0, 1, 1, 0, 1, 0]",
	"F# Major" 	: 	"[0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 1]",
	"F# Minor" 	: 	"[0, 1, 1, 0, 1, 0, 2, 0, 1, 1, 0, 1]",	
	"G Major" 	: 	"[1, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1]",
	"G Minor" 	: 	"[1, 0, 1, 1, 0, 1, 0, 2, 0, 1, 1, 0]",
	"Ab Major" 	: 	"[1, 1, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0]",
	"Ab Minor" 	: 	"[0, 1, 0, 1, 1, 0, 1, 0, 2, 0, 1, 0]",
	"A Major" 	: 	"[0, 1, 1, 0, 1, 0, 1, 0, 1, 2, 0, 1]",
	"A Minor" 	: 	"[1, 0, 1, 0, 1, 1, 0, 1, 0, 2, 0, 1]",
	"Bb Major" 	: 	"[1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 2, 0]",
	"Bb Minor" 	: 	"[1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 2, 0]",
	"B Major" 	: 	"[0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 2]",
	"B Minor" 	: 	"[0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 2]"
	}