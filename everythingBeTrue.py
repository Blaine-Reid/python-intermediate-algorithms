# Intermediate Algorithm Scripting: Everything Be True
# Check if the predicate (second argument) is truthy on all elements of a collection (first argument). 
# In other words, you are given an array collection of objects. The predicate pre will be an object property 
# and you need to return true if its value is truthy. Otherwise, return false. In JavaScript, truthy values 
# are values that translate to true when evaluated in a Boolean context. Remember, you can access object 
# properties through either dot notation or [] notation.

def truthCheck(arr,pre):    
  count = 0                                 # count elems
  for obj in arr:                           # get obj in arr
    if pre in obj:                          # if obj has the desired key
      if obj[pre]:count += 1                # check if value is truthy, add one to count if truthy
  # if count equals length of array, then all items were truthy
  print(True) if count == len(arr) else print(False)
      

truthCheck([{"user": "Tinky-Winky", "sex": "male"}, {"user": "Dipsy", "sex": "male"}, 
{"user": "Laa-Laa", "sex": "female"}, {"user": "Po", "sex": "female"}], "sex") #should return true.

truthCheck([{"user": "Tinky-Winky", "sex": "male"}, {"user": "Dipsy"}, {"user": "Laa-Laa", "sex": "female"}, 
{"user": "Po", "sex": "female"}], "sex") #should return false.

truthCheck([{"user": "Tinky-Winky", "sex": "male", "age": 0}, {"user": "Dipsy", "sex": "male", "age": 3}, 
{"user": "Laa-Laa", "sex": "female", "age": 5}, {"user": "Po", "sex": "female", "age": 4}], "age") #should return false.

truthCheck([{"name": "Pete", "onBoat": True}, {"name": "Repeat", "onBoat": True}, 
{"name": "FastFoward", "onBoat": 0}], "onBoat") #should return false

truthCheck([{"name": "Pete", "onBoat": True}, {"name": "Repeat", "onBoat": True, "alias": "Repete"}, 
{"name": "FastFoward", "onBoat": True}], "onBoat") #should return True

truthCheck([{"single": "yes"}], "single") #should return True

truthCheck([{"single": ""}, {"single": "double"}], "single") #should return false

truthCheck([{"single": "double"}, {"single": ''}], "single") #should return false

