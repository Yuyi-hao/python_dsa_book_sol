"""
Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
"""
from random import randrange

def get_random_element_from_list(data) -> None:
    n = len(data)
    res = data[randrange(0, n)]
    return res 

def main():
    res = get_random_element_from_list([1, 2, 4, 53, 66, 5 ,24, 2, 5, 6, 3, 2, 4, 2, 54, 65, 4])
    if res != None:
        print(res)

if __name__=="__main__":
	main()
