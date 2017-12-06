import os
import glob

#pitch_class = user_choice

# Generates a midi file with the given parameters
first = "performance_rnn_generate --config=pitch_conditioned_performance_with_dynamics --bundle_file=pitch_conditioned_performance_with_dynamics.mag --output_dir=generated --num_outputs=1"
pitch = "--pitch_class_histogram=\"[2, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]\""
steps = "--num_steps=1280"

# melody is the starting sequence of notes given to the network
primer = "--primer_melody=\"" + str(melody) + "\""


os.system(command)

files = glob.glob("generated/*.mid")

# Converting the midi file to a wav file using pySynth, the .wav is placed in the current directory
os.system("python .\PySynth-2.3\\readmidi.py " + files[0])

# Remove the midi file
os.system("del " + files[0])