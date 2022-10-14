#!/usr/bin/env python 

from subprocess import Popen, DEVNULL
import shlex, os, errno, time, glob

#Constants for later use
of2_verbose = False
temp_output = "of2_out"
temp_output_file = temp_output + '.csv'
landmark_count = 68

#This line finds the openface software
#If you're getting an error here, make sure this file is in the same folder as your openface installation
exe = ([exe for exe in glob.glob("./**/FeatureExtraction", recursive=True) if os.path.isfile(exe)]+[exe for exe in glob.glob(".\\**\\FeatureExtraction.exe", recursive=True)])[0]

#Clean up the temp file from a previous run, if it exists
try:
	os.remove(temp_output_file)
except OSError as e: 
	if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
		raise # re-raise exception if a different error occurred

#These lines write the command to run openface with the correct options
command = shlex.split(" -device 0 -out_dir . -pose -2Dfp -of "+temp_output)
command.insert(0, exe)

#This line starts openface
of2 = Popen(command, stdin=DEVNULL, stdout=(None if of2_verbose else DEVNULL), stderr=DEVNULL)

#This loop waits until openface has actually started, as it can take some time to start producing output
while not os.path.exists(temp_output_file):
	time.sleep(.5)

#Openface saves info to a file, and we open that file here
data = open(temp_output_file,'r')

#This loop repeats while openface is still running
#Inside the loop, we read from the file that openface outputs to and check to see if there's anything new
#We handle the data if there is any, and wait otherwise
while(of2.poll() == None):
	line = data.readline().strip()
	
	if(line != ""):
		try:
			#Parse the line and save the useful values
			of_values = [float(v) for v in line.split(', ')]
			timestamp, confidence, success = of_values[2:5]
			pitch, yaw, roll = of_values[8:11]
			landmarks = []
			for i in range(11,11+landmark_count):
				landmarks.append((of_values[i],of_values[i+landmark_count]))
		except ValueError:
			#This exception handles the header line
			continue
			
		#********************************************
		# Most, maybe all, of your code will go here
		#********************************************
		
		#Replace this line
		print("time:", timestamp, "\tpitch:", pitch, "\tyaw:", yaw, "\troll:", roll)
		
	else:
		time.sleep(.01)
	
#Reminder: press 'q' to exit openface

print("Program ended")

data.close()