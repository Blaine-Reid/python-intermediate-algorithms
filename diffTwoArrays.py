# Intermediate Algorithm Scripting: Diff Two Arrays
# Compare two arrays and return a new array with any items only found in one of the two given arrays, but not both. 
# In other words, return the symmetric difference of the two arrays. Note
# You can return the array with its elements in any order.

# VERSION 1
def diffArray(arr1,arr2):
  newArr = []
  for elem in arr2 :               # loop through arr2 and see if elem is NOT in arr1
    if elem not in arr1: newArr.append(elem) 
  for elem in arr1 :               # loop through arr1 and see if elem is NOT in arr2
    if elem not in arr2: newArr.append(elem)
  return print(newArr)

# VERSION 2
def diffArray(arr1,arr2):
  arr3 = arr1 + arr2        # combine arrays
  newArr = []
  for elem in arr3 :        #check to see if dublicates are in array
    if arr3.count(elem)==1:
     newArr.append(elem)
  return print(newArr)


diffArray(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], 
["diorite", "andesite", "grass", "dirt", "dead shrub"]) #should return ["pink wool"].


diffArray(["andesite", "grass", "dirt", "pink wool", "dead shrub"], 
["diorite", "andesite", "grass", "dirt", "dead shrub"]) #should return ["diorite", "pink wool"].

diffArray(["andesite", "grass", "dirt", "dead shrub"], ["andesite", "grass", "dirt", "dead shrub"]) #should return [].

diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]) #should return [4].

diffArray([1, "calf", 3, "piglet"], [1, "calf", 3, 4]) #should return ["piglet", 4].

diffArray([], ["snuffleupagus", "cookie monster", "elmo"]) #should return ["snuffleupagus", "cookie monster", "elmo"].

diffArray([1, "calf", 3, "piglet"], [7, "filly"]) #should return [1, "calf", 3, "piglet", 7, "filly"].
