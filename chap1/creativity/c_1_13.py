"""
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""

"""
Pseduo code:
Algorithm:
n -> list.length 
for i from n-1 to 0
    print list[i]
endfor 
"""

from random import randrange

def print_in_reverse(data) -> None:
    n = len(data)
    print("Algorithm")
    for i in range(n-1, -1, -1):
        print(data[i], end=" ")
    print()
    print("Python builtin")
    for i in reversed(data):
        print(i, end=" ")
    print()

def main():
    res = print_in_reverse([1, 2, 4, 53, 66, 5 ,24, 2, 5, 6, 3, 2, 4, 2, 54, 65, 4])
    if res != None:
        print(res)

if __name__=="__main__":
	main()
