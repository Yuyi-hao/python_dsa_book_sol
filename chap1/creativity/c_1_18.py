"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
"""

"""
The pattern 
0  = 0*1 
2  = 1*2 
6  = 2*3
12 = 3*4
20 = 4*5
nth = n*(n+1)
"""

def produce_list(n) -> None:
    return [i*(i+1) for i in range(n)]

def main():
    res = produce_list(10)
    if res != None:
        print(res)

if __name__=="__main__":
	main()
