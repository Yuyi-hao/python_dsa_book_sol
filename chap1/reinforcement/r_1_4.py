"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""

def sum_of_square(n):
    sum_of_square_number = 0
    for i in range(n):
        sum_of_square_number += i*i
    return sum_of_square_number


def main():
	res = sum_of_square(3)
	print(res)

if __name__=="__main__":
	main()
