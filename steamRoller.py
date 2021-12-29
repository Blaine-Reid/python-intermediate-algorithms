# Intermediate Algorithm Scripting: Steamroller
# Flatten a nested array. You must account for varying levels of nesting.


def steamrollArray(arr, L=None):
    '''Reduce a multi-dimensional list to its elements'''
    if L == None:
        L = []

    for x in arr:
        if isinstance(x, list): steamrollArray(x, L = L)
        else: L.append(x)
    return L


print(steamrollArray([[["a"]], [["b"]]])) #should return ["a", "b"].

print(steamrollArray([1, [2], [3, [[4]]]])) #should return [1, 2, 3, 4].
print(steamrollArray([1, [], [3, [[4]]]])) #should return [1, 3, 4].
print(steamrollArray([1, {}, [3, [[4]]]])) #should return [1, {}, 3, 4].