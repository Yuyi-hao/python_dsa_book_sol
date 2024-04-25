"""
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution
"""

def minmax(data):
    largest = data[0]
    smallest = data[0]
    for i in data:
        if largest < i:
            largest = i 
        if smallest > i:
            smallest = i
    return smallest, largest 


def main():
	res = minmax([1, 2, -9, 4, 5, 6, 12])
	print(res)

if __name__=="__main__":
	main()
