# File: 		keyphrase_extractor.py 	v1.0 	09/07/2021
# Author:		German Garcia Garcia	gggsman@gmail.com
# Description:	The following script is an automatic terminology or keyphrase extractor that given a text
#				input returns the text itself with the keywords on it highlighted and a list of them,
#				the model has been trained using the system provided in the following github repository.
# Github:		https://github.com/3Gsman/DeepTerminologyExtraction

import sys
import os

try:
	from flair.models import SequenceTagger
	from flair.data import Sentence
except:
	print("ERROR: 'FLAIR' libray not found, please write the command 'pip3 install flair'. ")

# Files loading
if not os.path.isfile('model.pt'):
	print("ERROR: 'model.pt' does not exist, please follow the instructions in README.txt to download the model.")
	sys.exit()

try:
	with open('input.txt') as f:
		lines = f.readlines()
except IOError:
	print("ERROR: 'input.txt' file does not exist. Please create the file in this directory.")
	sys.exit()

model = SequenceTagger.load('model.pt')	

try:
	sentence = Sentence(lines[0])
except:
	print("ERROR: 'input.txt' file empty. Please intruduce the text in 'input.txt'.")
	sys.exit()

# Tag preddiction
model.predict(sentence)

labeled = sentence.to_tagged_string()

# Output processing
wordList = labeled.split()

it2 = -1
keywords = []
for i in range(len(wordList)):
	if wordList[i] == "<B-KEY>":
		temp = []
		temp.append(wordList[i-1])
		keywords.append(temp)

	elif wordList[i] == "<I-KEY>":
		temp.append(wordList[i-1])
		keywords.append(temp)

str_keyword = []
for item in keywords:
	str_keyword.append(' '.join(item))

str_keyword = list(set(str_keyword))

temp2 = ["ORIGINAL TEXT",lines[0],"","TEXT WITH TAGS",labeled,"","KEYWORDS"]

totxt = temp2 + str_keyword

with open('output.txt', 'w') as f:
    for item in totxt:
        f.write("%s\n" % item)
