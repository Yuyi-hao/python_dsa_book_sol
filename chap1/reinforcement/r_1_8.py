"""
Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?
"""

def negative_index(s: str) -> None:
    n = len(s)
    for i in range(-n, 0, 1):
        print(s[i+n], end="")
    print()

def main():
    res = negative_index("Yuyi Hao")
    if res != None:
        print(res)

if __name__=="__main__":
	main()
