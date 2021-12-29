# Intermediate Algorithm Scripting: Drop it
# Given the array arr, iterate through and remove each element starting from the first element (the 0 index) 
# until the function func returns true when the iterated element is passed through it. Then return the rest 
# of the array once the condition is satisfied, otherwise, arr should be returned as an empty array.

def dropElements(arr,func):
  for x in range(len(arr)):
    if func(arr[x]):
      return print(arr[x:])
  return print([])

dropElements([1, 2, 3, 4], lambda n: n >= 3) #should return [3, 4].
dropElements([0, 1, 0, 1], lambda n: n == 1) #should return [1, 0, 1].
dropElements([1, 2, 3], lambda n: n > 0) #should return [1, 2, 3].
dropElements([1, 2, 3, 4], lambda n: n > 5) #should return [].
dropElements([1, 2, 3, 7, 4], lambda n: n > 3) #should return [7, 4].
dropElements([1, 2, 3, 9, 2], lambda n: n > 2) #should return [3, 9, 2].