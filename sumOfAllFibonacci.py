# Intermediate Algorithm Scripting: Sum All Odd Fibonacci Numbers
# Given a positive integer num, return the sum of all odd Fibonacci numbers that are less than or equal to num. 
# The first two numbers in the Fibonacci sequence are 1 and 1. Every additional number in the sequence is the 
# sum of the two previous numbers. The first six numbers of the Fibonacci sequence are 1, 1, 2, 3, 5 and 8.
#  For example, sumFibs(10) should return 10 because all odd Fibonacci numbers less than or equal to 10 are 1, 1, 3, 
#  and 5.

def sumFibs(num):
  '''Sum up the odd numbers in a Fibonacci sequence up to num'''
  fibs = [1,1]              # initial fib numbers
  sum = 0                           # sum to return
  fib = fibs[-1]+fibs[-2]         # set new fib to be added to list
  while fib <= num:               # as long as fib is less than number
    fibs.append(fib)              # add it to list
    fib = fibs[-1]+fibs[-2]       # create next value
  for x in fibs:                  #total sum of odd fib numbers
    if x % 2 != 0 :
      sum+=x
  return print(sum)



sumFibs(1) #should return a number.
sumFibs(1000) #should return 1785.
sumFibs(4000000) #should return 4613732.
sumFibs(4) #should return 5.
sumFibs(75024) #should return 60696.
sumFibs(75025) #should return 135721.