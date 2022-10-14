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
count = 0
x = []
y = []
for i in range(6):
	x.append(0)
	y.append(0)
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
			y_19 = of_values[104]
			y_24 = of_values[109]
			y_48 = of_values[133]
			y_51 = of_values[136]
			y_54 = of_values[139]
			x_48 = of_values[65]
			y_57 = of_values[142]
			x_54 = of_values[71]
		except ValueError:
			#This exception handles the header line
			continue
			
		#********************************************
		# Most, maybe all, of your code will go here
		#********************************************
		if(count%5 == 0):
			if(abs(pitch-x[0]) > 0.2):
				print('Yes')
			x[0] = pitch
			if(abs(roll - x[1]) > 0.2):
				print('Indian Nod')
			x[1] = roll
			if(abs(yaw-x[2]) > 0.2):
				print('No')
			x[2] = yaw
			if(x_48-x[3] > 2 and x_54-x[4] < -2 \
			and y_48 - y[4] < -2 and y_54 - y[5] < -2):
				print("Prototypical Smile")
			x[3] = x_48
			x[4] = x_54
			y[4] = y_48
			y[5] = y_54
			if(y_19-y[0] < -0.5 and y_24-y[1] < -0.5 \
			and y_51 - y[2] > 3 and y_57 - y[3] < -1):
				print("Surprise!")
			y[0] = y_19
			y[1] = y_24
			y[2] = y_51
			y[3] = y_57
	else:
		time.sleep(.01)
	count+=1
	
#Reminder: press 'q' to exit openface

print("Program ended")

data.close()