# Intermediate Algorithm Scripting: Seek and Destroy
# You will be provided with an initial array (the first argument in the destroyer function), followed by one or 
# more arguments. Remove all elements from the initial array that are of the same value as these arguments. Note
# You have to use the arguments object.

def destroyer(arr,*args):
  for destroy in args:                      #get value to destroy
    for count in range(arr.count(destroy)): #iterate up to the count of the destroys in an array
      arr.remove(destroy)                   #remove the item to destroy
  return print(arr)                         #print whats left


destroyer([1, 2, 3, 1, 2, 3], 2, 3) #should return [1, 1].
destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3) #should return [1, 5, 1].
destroyer([3, 5, 1, 2, 2], 2, 3, 5) #should return [1].
destroyer([2, 3, 2, 3], 2, 3) #should return [].
destroyer(["tree", "hamburger", 53], "tree", 53) #should return ["hamburger"].
destroyer(["possum", "trollo", 12, "safari", "hotdog", 92, 65, "grandma", "bugati", "trojan", "yacht"],
 "yacht", "possum", "trollo", "safari", "hotdog", "grandma", "bugati", "trojan") #should return [12,92,65].