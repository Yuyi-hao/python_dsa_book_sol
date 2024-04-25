"""
Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""

def is_even(k):
	return not k&1

def main():
	res = is_even(3)
	print(res)

if __name__=="__main__":
	main()
