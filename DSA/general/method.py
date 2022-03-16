from general.data_type import Integer 

"""
METHOD2
- for find the sum and negative of numbers in the array should be zero
"""
# number of element if even in continue order
# even length divisible by 2 remain 0
# it should be a sequence of 
def even_continous(arr=None):
    assert type(arr)==list 

    if len(arr)%2!=0:
        raise RuntimeError("Required a even and continue array")
    assert len(arr)%2==0
    arr=Integer.ascending(arr)
    
    alen=len(arr)
    half=alen//2
    first=arr[:half]
    second=arr[half:]

    print(arr,first,second)