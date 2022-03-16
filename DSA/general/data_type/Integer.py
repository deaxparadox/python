import random 

"""
Sort the given array of integer in ascending order
"""
def ascending(arr=None):
    assert type(arr)==list
    alen=len(arr)
    for i in range(alen):
        for j in range(alen):
            if arr[i]<arr[j]:
                hold=arr[i]
                arr[i]=arr[j]
                arr[j]=hold
    return arr

"""
Sort the given array of integer in descending order
"""
def descending(arr=None):
    assert type(arr)==list
    alen=len(arr)
    for i in range(alen):
        for j in range(alen):
            if arr[i]>arr[j]:
                hold=arr[i]
                arr[i]=arr[j]
                arr[j]=hold
    return arr


"""
return the largest form the given array
1. the array in ascending order
2. then the last number
"""
def largest(arr=None):
    # sort array in ascending order 
    # and return the largest number 
    return ascending(arr)[-1]

"""
# check if every number is greator than zero
# return True is for all non-zero
# return False for any zero
"""
def greator_than_zero(args):        
    dup=[]
    for n in args:
        if n>0:
            if n in dup:
                return False
            else:
                dup.append(n)
    else:
        return True

"""
# generate random numbers
"""
def generate_random(start=None,stop=None,count=None):
    return [random.randint(start,stop) for x in range(count)]
