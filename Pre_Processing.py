#!/usr/bin/python2

#---------------------------------------------------------------------
#Remove noise function

noise_list = ["is", "a", "this", "could"] 

def removeNoise(input_text):
    words = input_text.split() 
    noise_free_words = [word for word in words if word not in noise_list] 
    noise_free_text = " ".join(noise_free_words) 
    return noise_free_text

#---------------------------------------------------------------------
# Remove regular expression patterns 

import re 

regex_pattern = "#[\w]*"  

def removeRegex(input_text, regex_pattern):
    urls = re.finditer(regex_pattern, input_text) 
    for i in urls: 
        input_text = re.sub(i.group().strip(), '', input_text)
    return input_text


#removeRegex("remove this #hashtag from analytics vidhya", regex_pattern)

#---------------------------------------------------------------------
#POS tagging

from nltk import word_tokenize, pos_tag, punkt


#---------------------------------------------------------------------

#Open the file for pre-processing

fHandle = open("/home/muditha/mlresearch/corpus/originaldocuments/16122017DMBD1","r+")
fHandleW1 = open("/home/muditha/mlresearch/corpus/noiseremoved/16122017DMBD1","w+")
fHandleW2 = open("/home/muditha/mlresearch/corpus/postagged/16122017DMBD1","w+")

for line in fHandle:
	print line
	print "--------Removing Noice----------------------------"
	noNoiseLine = removeNoise(line)
	print "--------Removing Regular Expression---------------"
	fHandleW1.write(removeRegex(noNoiseLine, regex_pattern))
	print "--------------------------------------------------"
	tokens = word_tokenize(line)
	postag = pos_tag(tokens)
	print postag
	fHandleW2.write(postag[0])

#print fHandle.readlines()
fHandle.close()
fHandleW1.close()
fHandleW2.close()
