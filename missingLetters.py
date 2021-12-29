# Intermediate Algorithm Scripting: Missing letters
# Find the missing letter in the passed letter range and return it. If all letters are present in the range, 
# return undefined.

def fearNotLetter(str):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'   # characters to compare against
  first = alphabet.find(str[0])             # index of first character from str in alphabet
  last = alphabet.find(str[-1:])            # index of last character from str in alphabet
  clip = alphabet[first:last+1]             # clipped characters from alphabet
  for x in clip:                            # loop clipping
    if x not in str: return print(x)        # if charcter isn't in str, print the character
  return print('undefined')

    
fearNotLetter("abce") #should return "d".
fearNotLetter("abcdefghjklmno") #should return "i".
fearNotLetter("stvwx") #should return "u".
fearNotLetter("bcdf") #should return "e".
fearNotLetter("abcdefghijklmnopqrstuvwxyz") #should return undefined.