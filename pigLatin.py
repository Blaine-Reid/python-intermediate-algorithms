# Intermediate Algorithm Scripting: Pig Latin
# Translate the provided string to pig latin. Pig Latin takes the first consonant (or consonant cluster) of an 
# English word, moves it to the end of the word and suffixes an "ay". If a word begins with a vowel you just add 
# "way" to the end. If a word does not contain a vowel, just add "ay" to the end. Input strings are guaranteed to 
# be English words in all lowercase.

import re   #import regex module 

def translatePigLatin(str):
  vowels = re.compile('[aeiouAEIOU]')                      # compile the desired match
  if vowels.match(str): return print(str + 'way')     # return desired word
  if vowels.search(str,1):                            # word doesn't start with vowel 
    span = vowels.search(str,1).span()                # access the match object span location
    print(str[span[0]:] + str[:span[0]] + 'ay')
  else:                                               # if no vowels
    print(str + 'ay')



translatePigLatin("california") #should return "aliforniacay".
translatePigLatin("paragraphs") #should return "aragraphspay".
translatePigLatin("glove") #should return "oveglay".
translatePigLatin("algorithm") #should return "algorithmway".
translatePigLatin("eight") #should return "eightway".
#Should handle words where the first vowel comes in the middle of the word. 
translatePigLatin("schwartz") #should return "artzschway".
# Should handle words without vowels. 
translatePigLatin("rhythm") #should return "rhythmay".