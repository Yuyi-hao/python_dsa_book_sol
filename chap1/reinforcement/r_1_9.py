"""
What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
"""

def range_list(start, end, gap) -> None:
    for i in range(start, end, gap):
        print(i, end=" ")
    print()

def main():
    res = range_list(50, 90, 10)
    if res != None:
        print(res)

if __name__=="__main__":
	main()
