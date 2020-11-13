# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 00:07:16 2020

@author: VIDYA
"""
# TO identify the rosbag files and put it in a list 
# Irterate through the list, create a folder name in bagfile name and csvDIRECTORY in every bagfile folder
# make extractor.py as a module and pass each bagfile name as a pamameter
#rosbag -> csv files created
#Okay i will type and explain. Now that we have all the file names in the list we will create folder namesin
#bagfile name . for that you have a to get aseperate vaiablgetting the .bag extansion out 
#got it brooo?
#bor okay va?
import os
from os import walk
import extractor

#This is the folder name
mypath="normal"
#mypath=mypath+"/"
f = []
#wlak function is just a function that gets a triplet output of the the given foldername
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break

for bag in f:
    #This line gets the .bag extension out of our filename so that folder name looks good
    dirName=bag.strip(".bag")
    #now you create a new direcrroty for the bagfiles
    # normmal/2020... 
    dirName=mypath+"\\"+dirName
    command="mkdir  "+dirName
    os.system(command)
    #This is specifically for CSV files
    command=command+"\\CVDirectory"
    os.system(command)
    #Now lets create a path for input filename and output filename
    # normal/20202.bag
    #normal/20202/CV 
    inputFilename = mypath+"/"+bag
    outputFilename = dirName+"\\CVDirectory\\"
    print(inputFilename, outputFilename)
    #os.system("echo hi > "+outputFilename+"britto.txt")
    #now i have created a file called exctractor.py and that contains our script for extraci=ting csv
    # ihave altered the functions such that it takes input and output filenames as arguments
    # so to make use of that function i have used "import extractor in the top line cos thats the filename"
    #and in here i call that function using extractor.bagExtractor with input and outputfile name
    #And i am just getting the return command to make sure ecerything is ging fine
    # Its 2:00 in the morning and i am typing it now. By the time it ran foor one onr folder i even fin
    # doing my dishes and now i waiting for rest of the folders to complete uhm. 
    #Awesome now the battery is also running low :/
    message = extractor.bagExtractor( inputFilename, outputFilename )
    print(message)