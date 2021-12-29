# ntermediate Algorithm Scripting: Arguments Optional
# Create a function that sums two arguments together. If only one argument is provided, then return a function 
# that expects one argument and returns the sum. For example, addTogether(2, 3) should return 5, and addTogether(2) 
# should return a function. Calling this returned function with a single argument will then return the sum: var 
# sumTwoAnd = addTogether(2); sumTwoAnd(3) returns 5. If either argument isn't a valid number, return undefined.

def addTogether(*args):
    # sum total for when 2 args are passing
  x = 0               
    # loop to check if args are integers                                   
  for arg in args:                                     
    if not isinstance(arg,int):return print('undefined') 
      # if only one argument is given, check if INT and sum together
  
  if len(args) == 1:                                   
    return lambda num: print(args[0] + num) if isinstance(num,int) else print('undefined')
               # else sum arguments given 
  for val in args:                            
    x+= val
                      # return sum
  return print(x)                      

addTogether(2, 3) #should return 5.
addTogether(2)(3) #should return 5.
addTogether("http://bit.ly/IqT6zt") #should return undefined.
addTogether(2, "3") #should return undefined.
addTogether(2)([3]) #should return undefined.