"""
Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax and the built-in sum function.
"""

def sum_of_square_odd_num(n):
    return sum([i*i for i in range(1, n, 2)])

def main():
	res = sum_of_square_odd_num(6)
	print(res)

if __name__=="__main__":
	main()
