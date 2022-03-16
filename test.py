# In[]:
"""1. Write a function that estimate that given
number is positive, negative and zero"""

def check(data: int) -> None:
    if data == 0:
        print(f"Given number {data} is zero")
    if (data % 2) == 0:
        print(f"Given number {data} is Positive")
    else:
        print(f"Given number {data} is negative.")
    

# %%
for i in range(0,100,21):
    check(i)
# %%
"""Write a Python program to find those numbers
which are divisible by 7 and multiple of 11, between 100
and 700 (both inluded)"""

def Q2():
    start = 100
    target = 700
    for i in range(start, target+1):
        if (i%11) == 0 and (i%7) == 0:
            print(i)
    
# %%
Q2()
# %%
"""Write a Python program that accepts a word from 
the user and reverse it.
"""

def reverse(data: str = None) -> None:
    rdata = data[::-1]
    print(rdata)
# %%
reverse('Nitish')
# %%
"""5. Write a Python program to find the eigenvalues and eigenvectors 
for  the matrix.
"""
from sympy.matrices import Matrix
M = Matrix(3, 3, [1, 2, 2, 2, 1, 2, 2, 2, 1])
eval = M.eigenvals()
evec = M.eigenvects()

print("Given matrix: ", M)
print("Eigenvals for given matrics is:\n", eval)
print("Eigenvects for given matrics is:\n", evec)

# %%
from sympy import Matrix
M = Matrix(3,3,[6,8,3,2,12,1,4,15,3])
M.echelon_form()
M.rank()
M.nullspace()
M.columnspace()