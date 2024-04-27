"""
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""

"""
only product of two odd number can result in odd number 
find two different odd number 
"""

def is_odd_product(data) -> None:
    curr = 0 
    for i in data:
        if i&1 and not curr:
            curr = i
        elif i&1 and curr and curr != i:
            return True
    return False

def main():
    res = is_odd_product([5, 2, 3])
    if res != None:
        print(res)

if __name__=="__main__":
	main()
