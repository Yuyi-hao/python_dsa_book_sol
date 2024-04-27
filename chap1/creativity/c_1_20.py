"""
Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possible order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
"""

"""
swap each number with one of the number from list 
"""

from random import randint

def shuffle_list(data) -> None:
    n = len(data)
    for i in range(n):
        c = randint(0, n-1)
        data[i], data[c] = data[c], data[i]
    print(data)
    return 

def main():
    res = shuffle_list( [1, 2, 4, 34, 546, 6546])
    if res != None:
        print(res)

if __name__=="__main__":
	main()
