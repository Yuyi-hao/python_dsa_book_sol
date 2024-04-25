"""
Write a short python function, is_multiple(n, m), that takes two integer value
and returns True if n is a multiple of m, that is n = mi for some integer i, and False otherwise.
"""
def is_multiple(n, m):
	return not bool(n%m)

def main():
	res = is_multiple(2, 3)
	print(res)

if __name__=="__main__":
	main()
