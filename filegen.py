import os, sys

def training():
    fw = open(sys.argv[2], "w")
    filenames = []
    for filename in os.listdir(sys.argv[1]):
        filenames.append(filename)
    filenames.sort()
    for filename in filenames:
        fr = open(sys.argv[1]+"/"+filename, "r", errors='ignore')
        s = fr.read()
        file_data = s.split("\n")
        class_name = filename.split('.')
        line = class_name[0]
        for l in file_data:
            line = line+" "+l
        fw.write(line+"\n")
        fr.close()
    fw.close()

training()
