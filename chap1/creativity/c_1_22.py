"""
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1.
"""

def dot_product(a: list[int], b: list[int]) -> list[int]:
    return [x*y for x, y in zip(a, b)]

def main():
    res = dot_product([5, 2, 3], [2, 3, 5])
    if res != None:
        print(res)

if __name__=="__main__":
	main()
