"""
Give a single command that computes the sum from Exercise R-1.4, relying on Python’s comprehension syntax and the built-in sum function.
"""

def sum_of_square(n):
    return sum([i*i for i in range(n)])

def main():
	res = sum_of_square(3)
	print(res)

if __name__=="__main__":
	main()
