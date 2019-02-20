import pandas as pd
import csv
import os

folders = ['./2016/', './2017/']
files = [folder + f for folder in folders for f in os.listdir(folder)]

def getResponses():
    responses = {}
    for f in files:
        lines = list(csv.reader(open(f, 'r')))
        questions = lines.pop(0)
        for line in lines:
            for index, field in enumerate(line):
                if questions[index] not in responses:
                    responses[questions[index]] = []
                responses[questions[index]].append(field)
    return responses

def makeNewCSV():
    responses = getResponses()
    biggest = max([len(a) for a in responses.values()])
    out = ','.join(responses.keys()) + '\n'
    for i in range(biggest):
        line = ''
        for q in responses:
            if i < len(responses[q]):
                line += '"' + responses[q][i] + '"'
            line += ','
        out += line + '\n'
    f = open('combined.csv', 'w')
    f.write(out)
    f.close()

def getQuestions():
    questions = []
    for f in files:
        with open(f, 'r') as text:
            questions.extend(text.read().split('\n')[0].split(','))
    return questions

[print(q) for q in getQuestions()]

    

makeNewCSV()