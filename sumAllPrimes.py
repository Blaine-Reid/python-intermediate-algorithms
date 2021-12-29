# Intermediate Algorithm Scripting: Sum All Primes
# Sum all the prime numbers up to and including the provided number. A prime number is defined as a number 
# greater than one and having only two divisors, one and itself. For example, 2 is a prime number because 
# it's only divisible by one and two. The provided number may not be a prime.

import functools

def sumPrimes(num):
  '''Sum the prime numbers up to num'''
  if num == 1 : return print('Not Prime')     # default 
  primes=[]                                  # starting prime list

  for n in range(2, num):
    for x in range(2, n):
      if n % x == 0:
          break
    else:
        # loop fell through without finding a factor
        primes.append(n)
  print(functools.reduce(lambda x,y: x+y, primes,0))  

sumPrimes(10) #should return 17.
sumPrimes(977) #should return 73156.