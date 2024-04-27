"""
Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
"""

"""
ctrl+d raise EOFError check for that
"""

def print_line_reverse() -> None:
    data = []
    try:
        while True:
            c = input()
            data.append(c)
    except EOFError as e:
        n = len(data)
        for i in range(n-1, -1, -1):
            print(data[i])
        return 
    
def main():
    res = print_line_reverse()
    if res != None:
        print(res)

if __name__=="__main__":
	main()


