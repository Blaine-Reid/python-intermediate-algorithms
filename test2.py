


def test():
  str=r"C:\test" #use the 'r' to ignore escape characters
  print(str)

# test()


def glueString(str):
  '''Strings can be multiplied together then concated with others'''
  print('strings' ' split' ' will concate') # strings will automatically concatenate
  print(3 * str + ' tasty')  #multiply string together then add end part

# glueString('nom')


def fibanacci():
  a, b = 0, 1         # set values to a ,b
  while a < 1000:  
     print(b, end=',')
     a, b = b, a+b    # set a to b and b to a+B

# fibanacci()

def deepIterate():
  arr = [['a'],['b']]

  for item in arr.copy():
    print(item)

# deepIterate()


def objIterate(users):
  active_users = {}
  for user , status in users.items(): # user = key, status = object used unpacking
    print(user)
    print(status)
  
    if users[user]['status'] == 'active':
        active_users[user] = status

  print(active_users)

# objIterate({
#     "Kevin":{"status":"active"},
#     "Sarah":{"status":"inactive"},
#     "Tiffany":{"status":"active"},
#     "Robert":{"status":"inactive"},
#     "Jack":{"status":"active"},
#   })

def iterateList(arr):
  '''iterates through arr and assigns extra values to y'''
  for x, *y in arr:        # use * to capture if extra values in unpacking
    print(x)
    print(y)

iterateList([['a','b'],'a'])


# we can set range with start, finish and an increment value
def incrementIterate(start,finish,increment):
  '''Prints the list of numbers from start to finish and increments those values'''
  print(list(range(start,finish,increment)))

incrementIterate(10,1000,20)



def usingSum(val):
  '''Prints the sum of all numbers in a range to val'''
  print(sum(range(val)))

usingSum(10)


def defaultParam(str='Default'):
  '''Use of default parameters'''
  print(str)

defaultParam()
defaultParam('Test')

'''The default values are evaluated at the point of function definition in the defining scope'''
i = 5
def f(arg=i):
    print(arg)

i = 6
f()



def keywordArg(require, typeVal="Int", case="Upper"):
  '''We can call defaulted parameters by name!!!'''
  print(require, ' was required but ', typeVal, " and ", case," aren't" )

keywordArg(1000, case="Lower")


def dictOfArgs(*tup,**dic):
  '''
  By using *before arg returns a tuple of the args without default/named .

     **before arg returns a dictionary of the key values for all named/keyword params
  '''
  for arg in tup: 
    print(arg)

  for key in dic:
    print(key, dic[key])

dictOfArgs(1,2,3,name='Jack',age=25)

'''
Parameters before / are positional only
Parameters after / are either positional or keyword
Parameters after * are keyword ONLY
'''
def f(pos1, pos2, /, pos_or_kwd, *, kwd1='test', kwd2='keyword'):
  print(pos1)
  print(pos2)
  print(pos_or_kwd)
  print(kwd1)
  print(kwd2)
f(1,2,pos_or_kwd='success',kwd1='help',kwd2='me')



# Finally, consider this function definition which has a potential collision between the positional 
# argument name and **kwds which has name as a key:


def foo1(name, **kwds):
   return print('name' in kwds)


# There is no possible call that will make it return True as the keyword 'name' will always 
# bind to the first parameter. For example:

# foo1(1, **{'name': 2})

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: foo() got multiple values for argument 'name'
# >>>


# But using / (positional only arguments), it is possible since it allows name as a positional argument 
# and 'name' as a key in the keyword arguments:


def foo2(name, /, **kwds):
    return print('name' in kwds)
foo2(1, **{'name': 2})
# True
  

#Annotating the values of parameters
def f(ham: str = 'ham', eggs: str = 'eggs') -> str:
  '''
  Colon after keyword denotes casting.

  then -> after parameters denotes value returned by function
  '''
     print("Annotations:", f.__annotations__)
     print("Arguments:", ham, eggs)
     return ham + ' and ' + eggs
    
f('spam')