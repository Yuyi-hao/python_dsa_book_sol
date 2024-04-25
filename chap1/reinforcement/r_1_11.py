"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""

def range_list() -> None:
    lst = [2**i for i in range(9)]
    return lst

def main():
    res = range_list()
    if res != None:
        print(res)

if __name__=="__main__":
	main()
