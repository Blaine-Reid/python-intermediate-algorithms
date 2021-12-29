# Intermediate Algorithm Scripting: Wherefore art thou
# Make a function that looks through an array of objects (first argument) and returns an array of all objects 
# that have matching name and value pairs (second argument). Each name and value pair of the source object 
# has to be present in the object from the collection if it is to be included in the returned array. For example, 
# if the first argument is [{ first: "Romeo", last: "Montague" }, { first: "Mercutio", last: null }, 
# { first: "Tybalt", last: "Capulet" }], and the second argument is { last: "Capulet" }, then you must 
# return the third object from the array (the first argument), because it contains the name and its value, 
# that was passed on as the second argument.

def whatIsInAName(collection, source):
  newCollection = []
  keys = 0
  for obj in collection:              #loop through collection
    for key in source:                # get the key in the source
      if key in obj:                  # if the key is in the object from collection
        if source[key] == obj[key]:   # compare the values
          keys+=1                     #increment counter
          continue
        else:                         #or break from loop
          break               
    if keys == len(source.keys()):    #if the increment equals the length of the keys in source object
      newCollection.append(obj)       # append the obj to newArr
      keys=0                          # reset keys increment
    else:
      keys = 0

  return print(newCollection)


whatIsInAName([{ "first": "Romeo", "last": "Montague" }, { "first": "Mercutio", "last": 0 }, { "first": "Tybalt", "last": "Capulet" }], { "last": "Capulet" }) 
#should return [{ first: "Tybalt", last: "Capulet" }].
whatIsInAName([{ "apple": 1 }, { "apple": 1 }, { "apple": 1, "bat": 2 }], { "apple": 1 }) 
#should return [{ "apple": 1 }, { "apple": 1 }, { "apple": 1, "bat": 2 }].
whatIsInAName([{ "apple": 1, "bat": 2 }, { "bat": 2 }, { "apple": 1, "bat": 2, "cookie": 2 }], { "apple": 1, "bat": 2 }) 
#should return [{ "apple": 1, "bat": 2 }, { "apple": 1, "bat": 2, "cookie": 2 }].
whatIsInAName([{ "apple": 1, "bat": 2 }, { "apple": 1 }, { "apple": 1, "bat": 2, "cookie": 2 }], { "apple": 1, "cookie": 2 }) 
#should return [{ "apple": 1, "bat": 2, "cookie": 2 }].
whatIsInAName([{ "apple": 1, "bat": 2 }, { "apple": 1 }, { "apple": 1, "bat": 2, "cookie": 2 }, { "bat":2 }], { "apple": 1, "bat": 2 }) 
#should return [{ "apple": 1, "bat": 2 }, { "apple": 1, "bat": 2, "cookie":2 }].
whatIsInAName([{"a": 1, "b": 2, "c": 3}], {"a": 1, "b": 9999, "c": 3}) 
#should return []