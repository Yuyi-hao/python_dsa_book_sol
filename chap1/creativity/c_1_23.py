"""
Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don’t try buffer overflow attacks in Python!”
"""

"""
IndexError exception raised when try to access out of bound index 
"""

def out_of_bound(data) -> None:
    n = len(data)
    try:
        print(data[n])
    except IndexError as e:
        print("Don’t try buffer overflow attacks in Python!")

def main():
    res = out_of_bound([5, 2, 3])
    if res != None:
        print(res)

if __name__=="__main__":
	main()
