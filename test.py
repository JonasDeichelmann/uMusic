import os
import glob
import pitch

pitch_classes = pitch.pitch_classes

pitch_class = pitch_classes["C Minor"]

melody = [60, -1, 64, -1, , -1, 67, -2, 64, -2, 64, -2, 60]

#input_melody = user_input

# Generates a midi file with the given parameters

def GenerateMusic(notes_per_second=3, input_melody=[60,-1,62], input_chord=[60, 64, 67], pitch_class=pitch_classes["C Major"]):

	performance = "multiconditioned_performance_with_dynamics"

	first = "performance_rnn_generate --config=" + performance + " --bundle_file=" + performance + ".mag --output_dir=generated --num_outputs=1"

	# A step is 10 ms.  Hence, 3000 steps will generate 30 seconds of music
	steps = "--num_steps=3000"
	notes_per_second = "--notes_per_second=" + str(notes_per_second)

	# melody is the starting sequence of notes given to the network
	primer = "--primer_melody=\"" + str(input_melody) + "\""
	chord = "--primer_pitches=\"" + str(input_chord) + "\""
	pitch = "--pitch_class_histogram=\"" + pitch_class + "\""

	command = first + " " + pitch + " " + steps + " " + notes_per_second + " " + primer + " " + chord

	os.system(command)

	files = glob.glob("generated/*.mid")

	# Converting the midi file to a wav file using pySynth, the .wav is placed in the current directory
	os.system("python .\PySynth-2.3\\readmidi.py " + files[0])

	# Remove the midi file
	os.system("del " + files[0])

GenerateMusic(notes_per_second=5, input_melody=melody, pitch_class=pitch_class)