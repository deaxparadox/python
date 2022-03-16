
"""     ltof : last to first shift
# pop the element from array 
# and insert it at number index 0
# based count time
"""
def ltof(arr=None,n=1):
    # n equal to 1 represent default time 
    assert type(arr)==list

    for i in range(n):
        l=arr.pop()
        arr.insert(0,l)
    return arr

"""     srby1: shift row by 1
# shift each level 
# and its elements by 1
arr: list
n: shift distance default to 1
"""
def srby1(arr=None,n=1):
    assert type(arr)==list
    shifted=[]
    alen=len(arr)
    # we have shift element by 1 to previous row 
    for i in range(alen):
        # print(i+1)
        shifted.append(ltof(arr[i],n))
    return shifted

"""     soir: shift on increasing range
e.g. such as first row shift by 1, second by 2, third by 3 and so on
# shift the matrix 
# shift each row of matrix by 1 by previous 
"""
def soir(arr=None):
    assert type(arr)==list
    shifted=[]
    alen=len(arr)
    # we have shift element by 1 to previous row 
    for i in range(alen):
        # print(i+1)
        shifted.append(ltof(arr[i],i+1))
    return shifted
    