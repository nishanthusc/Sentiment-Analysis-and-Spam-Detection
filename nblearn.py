import glob,math,sys
from decimal import *
from datetime import datetime
import json

#print(str(datetime.now())) 
uniqueWordsInTrainingSet= 0.0
totalNumberOfLines = 0.0
classesDict={}
cWrdsClasses={}
wordsDict={}
priorProbDict={}
totalVocab={}

def calcProbablity(word,classes):
    if word in wordsDict[classes]:
        count = Decimal(wordsDict[classes].get(word))+1
    else:
        #print("Inside Else")
        count=1
    return(math.log(count)-math.log(cWrdsClasses[classes]+vocabCount))



#trainingFile = open('/home/nish/NLP/Homework1/DataSets/spam_training.txt','r')
trainingFile = open(sys.argv[1],'r')
for inline in trainingFile:
    totalNumberOfLines+=1 #This will give count of sum of all classes in training file
    wordsInLine = inline.split(" ")
    classInLine = wordsInLine[0].strip()
    if classInLine in classesDict:
        classesDict[classInLine]+=1 #counting the number of words that belong to each different class
    else:
        classesDict[classInLine]=1.0
        cWrdsClasses[classInLine]=0.0
        wordsDict[classInLine]={}
    wordsInLine.remove(wordsInLine[0])
    for word in wordsInLine:
        word = word.strip()
        if word!="":
            if word not in totalVocab:
                totalVocab[word]=1
            cWrdsClasses[classInLine]+=1
            if word in wordsDict[classInLine]:
                wordsDict[classInLine][word]+=1
                
            else:
                wordsDict[classInLine][word]=1
                uniqueWordsInTrainingSet+=1
                
trainingFile.close()
#print(str(datetime.now()))
vocabCount = len(totalVocab)
#modelFile = open('/home/nish/NLP/Homework1/DataSets/spam.nb','w')
modelFile = open(sys.argv[2],'w')
for className in classesDict:
    
    priorProbability = classesDict[className]/totalNumberOfLines
    logpriorProb = math.log(priorProbability)
    priorProbDict[className]=logpriorProb

   
##over riding the counts of each word in a specific class with log of Probailbity Values in each class
for classes in classesDict:
    for words in wordsDict[classes]:
        logVal = calcProbablity(words,classes)
        wordsDict[classes][words]= logVal

        
finalDict ={'priorProbDict':priorProbDict,'wordsLogValDict':wordsDict,'countOfWordsPerClass':cWrdsClasses,'uniqueWords':uniqueWordsInTrainingSet,'totalVocab':totalVocab}

json.dump(finalDict,modelFile)
modelFile.close()
#print(uniqueWordsInTrainingSet)
#print(len(totalVocab))

