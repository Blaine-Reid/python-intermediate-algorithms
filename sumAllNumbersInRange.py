# Intermediate Algorithm Scripting: Sum All Numbers in a Range
# We'll pass you an array of two numbers. Return the sum of those two numbers plus the sum of all the numbers 
# between them. The lowest number will not always come first.

# import functools

def sumAll(arr):
  '''Sum all the numbers in a range given as a list.'''
  arr.sort()
  print(sum(range(arr[0],arr[1]+1)))
  # arr.sort()
  # arr = [x for x in range(arr[0],arr[1]+1)]
  # return print(functools.reduce(lambda x,y:x+y,arr,0))

# For example, sumAll([4,1]) should return 10 because sum of all the numbers between 1 and 4 (both inclusive) is 10.
sumAll([1, 4]) #should return 10.
sumAll([4, 1]) #should return 10.
sumAll([5, 10]) #should return 45.
sumAll([10, 5]) #should return 45.