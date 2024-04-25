"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""

def sum_of_square_odd_num(n):
    res = 0 
    for i in range(1, n, 2):
        res += i*i
    return res

def main():
	res = sum_of_square_odd_num(6)
	print(res)

if __name__=="__main__":
	main()
