# Intermediate Algorithm Scripting: Make a Person
# Fill in the object constructor with the following methods below:

# getFirstName()
# getLastName()
# getFullName()
# setFirstName(first)
# setLastName(last)
# setFullName(firstAndLast)

# Run the tests to see the expected output for each method. The methods that take an argument must accept 
# only one argument and it has to be a string. These methods must be the only available means of interacting
#  with the object.

class Person: 
  # Complete the method below and implement the others similarly
  '''A class to create a Person that returns name(s)'''
  def __init__(self,firstAndLast):      # define initiation function
    self.name = firstAndLast.split()    # set self name to argument
    self.firstName = None
    self.lastName = None

  def getFullName(self):                # define full name function
    print(' '.join(self.name))

  def getFirstName(self):               # define first name function
    if self.firstName: print(self.firstName) 
    print(self.name[0])

  def getLastName(self):                # define last name function
    if self.lastName: print(self.firstName) 
    print(self.name[1])

  def setFullName(self, fullName):      # define set full name function
    self.name = fullName.split()

  def setFirstName(self, firstName):    # define set first name function
    self.name[0] = firstName
    self.firstName = firstName

  def setLastName(self, lastName):      # define set last name function
    self.name[1] = lastName
    self.lastName = lastName


bob = Person('Bob Ross')


# print(bob) #should return 6.
print(isinstance(bob, Person)) #should return true.
print(bob.firstName,' = None') #should return undefined.
print(bob.lastName,' = None') #should return undefined.
print(bob.getFirstName(),' = Bob') #should return "Bob".
print(bob.getLastName(),' = Ross') #should return "Ross".
print(bob.getFullName(),' = Bob Ross') #should return "Bob Ross".
bob.setFirstName("Haskell")
print(bob.getFullName(),' = Haskell Ross') #should return "Haskell Ross" after bob.setFirstName("Haskell").
bob.setLastName("Curry")
print(bob.getFullName(),' = Haskell Curry') #should return "Haskell Curry" after bob.setLastName("Curry").
bob.setFullName("Haskell Curry")
print(bob.getFullName(),' = Haskell Curry') #should return "Haskell Curry" after bob.setFullName("Haskell Curry").
bob.setFullName("Haskell Curry")
print(bob.getFirstName(),' = Haskell') #should return "Haskell" after bob.setFullName("Haskell Curry").
bob.setFullName("Haskell Curry")
print(bob.getLastName(),' = Curry') #should return "Curry" after bob.setFullName("Haskell Curry").