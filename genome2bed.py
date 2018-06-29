#script to convert fasta/ genome files
#to the BED file format.
#author: Noah A. Legall
#created: June 27th 2018
##########

#An extra tool I ended up making, but turned out to not be necessary to research
#alas, I also realized there was no way to take a genome file and convert it to a BED file
#here, I present an attempt.

#Take in arguements and save to variable filename
import sys # use to access arguments
import os # use in order to call commands from terminal script is called in
import re # regular expressions used to 


# python genome2bed.py [genome fasta file] [output file name]

#read in file name i want to change
filename = sys.argv[1] 

#name of the output file we wish to create, then activly create it
output = sys.argv[2] 
os.system('touch '+output) 

file = open(filename, "r")
out = open(output, "w")



length_of_sequence = 0 # a variable to ultimately hold the length of the sequence
iteration = 0 #a counter that keeps certain logical things on track
name = '' # initialize the name variable to hold the chromosome name


#loop through every line in the genome fasta
for line in file:
    #record the name variableon the first line
    if line[0] == '>' and iteration == 0:
        name = line[1:].rstrip()
    #everytime we encounter a new label, write out to output file
    #reset length of sequence
    elif line[0] == '>' and iteration > 0:
        out.write(name+'\t0\t'+str(length_of_sequence)+'\n')
        #remove any trailing white spaces from the line.
        name = line[1:].rstrip()
        length_of_sequence = 0
    #keep adding the length of each line otherwise    
    else:
        length_of_sequence = len(line) + length_of_sequence
    #increment iteration by 1    
    iteration += 1
