__author__ = 'srikanth'

import glob
import sys
import os


directory = "/home/nish/NLP/Homework1/DataSets/SPAM_training"

files = os.listdir(directory)
count = 0
out = open("spam_train.txt", "w")
files.sort()


for temp in files:

    f = open("/home/nish/NLP/Homework1/DataSets/SPAM_training/"+temp, "r+",errors='ignore')
    lines = f.read().split("\n")
    if("HAM" in temp):
      out.write("HAM ")
    else:
      out.write("SPAM ")
    for line in lines :
        out.write(line)
        out.write(" ")
    out.write("\n")
    #print("\n")
    f.close()

print (len(files))


