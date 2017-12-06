import os
import glob
import pitch

pitch_classes = pitch.pitch_classes

pitch_class = pitch_classes["Bb Major"]

melody = [58, -1, 62, -1, 65, -1, 70, -2, 65, -2, 62, -2, 58]

performance = "multiconditioned_performance_with_dynamics"

# Generates a midi file with the given parameters
first = "performance_rnn_generate --config=" + performance + " --bundle_file=" + performance + ".mag --output_dir=generated --num_outputs=1"
steps = "--num_steps=6000"
notes_per_second = "--notes_per_second=4"

# melody is the starting sequence of notes given to the network
primer = "--primer_melody=\"" + str(melody) + "\""
chord = "--primer_pitches=\"[58, 62, 65]\""
pitch = "--pitch_class_histogram=\"" + pitch_class + "\""

command = first + " " + pitch + " " + steps + " " + notes_per_second + " " + primer + " " + chord

os.system(command)

files = glob.glob("generated/*.mid")

# Converting the midi file to a wav file using pySynth, the .wav is placed in the current directory
os.system("python .\PySynth-2.3\\readmidi.py " + files[0])

# Remove the midi file
os.system("del " + files[0])