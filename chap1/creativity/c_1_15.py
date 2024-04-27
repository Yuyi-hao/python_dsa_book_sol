"""
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""

"""
Algorithm:
for every number in list check if it exist second time in list if it does return False else True 

Algorithm:
use hashmap to find the distinct number if the number of distinct number is same as number of element in list return True else false.
"""

def is_distinct(data) -> None:
    n = len(data)
    flag = True
    print("using o^2 approach")
    for i in range(n):
        for j in range(i+1, n):
            if data[i] == data[j]:
                flag = False
                print("False")
                break
    if flag:
        print(True)
    print("Using set")
    print(len(data) == len(set(data)))
    return

def main():
    res = is_distinct([5, 2, 3])
    if res != None:
        print(res)

if __name__=="__main__":
	main()
