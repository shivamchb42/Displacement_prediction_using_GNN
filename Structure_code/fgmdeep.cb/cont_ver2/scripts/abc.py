import os
import pandas as pd
import numpy as np

iterations = input("Enter the number of iterations:")

#Making the combined data files
os.system("python3 ab.py")

#input for prop.dat file creation
types_of_materials = 1
number_of_constants  = 101 #100 elements + 1 poisson ratio
info = ["           "+str(types_of_materials)+"          "+str(number_of_constants)]

for i in range(int(iterations)):
	#create the new prop.dat file for the new iteration
	
	#generate the new parameters
	stiff = 7 + 1.5 * np.random.randn(number_of_constants-1)  #generate random values of stiffness for each node
	poisson  = 0.45  #poisson ratio
	# open prop.dat file in write mode
	path = os.getcwd()
	path = (os.path.dirname(path)+'/'+'prop.dat')
	with open(path, 'w') as fp:
		for item in info:
		    # write each item on a new line
		    fp.write("%s\n" % item)
		for item in stiff:
		    # write each item on a new line
		    fp.write("   %s\n" % item)
		fp.write("  %s\n" % poisson)
		fp.write("           0           0           0           0           0           0           0           0           0           0           0           0           0")
	
	#run the FEM code on the generated prop.dat file
	os.system("cd ..\n./main.e > shape")
