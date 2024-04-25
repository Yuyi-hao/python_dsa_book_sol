"""
What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, -2, -4, -6, -8?
"""

def range_list(start, end, gap) -> None:
    for i in range(start, end, gap):
        print(i, end=" ")
    print()

def main():
    res = range_list(8, -9, -2)
    if res != None:
        print(res)

if __name__=="__main__":
	main()
