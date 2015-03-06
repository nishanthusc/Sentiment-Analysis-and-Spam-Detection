import sys,glob,json,math
from decimal import *


modelFilePath = sys.argv[1]
testingFile = sys.argv[2]

modelRead = open(modelFilePath,'r')
testingFile = open(testingFile,'r')

mainDict= json.load(modelRead)
childDict1 = mainDict['priorProbDict']
wordsInDict = mainDict['wordsLogValDict']
totalVocabDict = mainDict['totalVocab']
countsPerClassDict = mainDict['countOfWordsPerClass']
totalUniqueWords = len(totalVocabDict)#mainDict['uniqueWords']

ClassDict={}
##CorrectedDict={'POS':0,'NEG':0}

className=""
outF=""
correctCount=0

    
for line in testingFile:
    #print(line)
    words = line.split()
    finalProb = -sys.maxsize
    for classes in wordsInDict.keys():
        
        if classes not in ClassDict.keys():
            ClassDict[classes]=0
        
        listVal=[]
        correctWord = words[0]
        for word in range(1,len(words)):
            if len(words[word].strip())>0:
                if words[word] in totalVocabDict:
                    if words[word] in wordsInDict[classes]:
                        w = words[word]
                        listVal.append(wordsInDict[classes][w])
                    else:
                        plusOneSmoothDenom = countsPerClassDict[classes] + totalUniqueWords
                        listVal.append(math.log(1/plusOneSmoothDenom))
        wordsProb = sum(listVal)
        currentProb = childDict1[classes]+wordsProb
        #print(currentProb,finalProb,classes)
        if(currentProb>finalProb):
            #print("true")
            finalProb = currentProb
            predictedClass = classes
        #print(correctWord,predictedClass)
        
    #outputFile.write(predictedClass+"\n")
    print(predictedClass)
    
##    if(correctWord==predictedClass):
##        correctCount+=1
##        CorrectedDict[correctWord]+=1
##    ClassDict[predictedClass]+=1
#outputFile.close()
#print(ClassDict)
#print(CorrectedDict)
#print(correctCount)
modelRead.close()
testingFile.close()

