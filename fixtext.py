#!/usr/bin/python3
import fileinput

for line in fileinput.input():
    sentence = line.split('"contest">')[1]
    sentence = sentence.split('<')[0]
    auth = line.split('"winnerid">')[1]
    auth = auth.split('</span>')[0]

    print(sentence+"\n"+auth)

