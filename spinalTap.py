# Intermediate Algorithm Scripting: Spinal Tap Case
# Convert a string to spinal case. Spinal case is all-lowercase-words-joined-by-dashes.

import re # import regex module

def spinalCase(str):
  split = re.split("[_\s-]|(?=[A-Z])",str)  # split string at space and - or _ along with at Capital letters
  combined = []                             
  for word in split:                        # if element in array isn't empty, then push to new array
    if bool(word): combined.append(word)
    
  print('-'.join(combined).lower())         #print the words joined by '-' character




spinalCase("This Is Spinal Tap") #should return "this-is-spinal-tap".
spinalCase("thisIsSpinalTap") #should return "this-is-spinal-tap".
spinalCase("The_Andy_Griffith_Show") #should return "the-andy-griffith-show".
spinalCase("Teletubbies say Eh-oh") #should return "teletubbies-say-eh-oh".
spinalCase("AllThe-small Things") #should return "all-the-small-things".