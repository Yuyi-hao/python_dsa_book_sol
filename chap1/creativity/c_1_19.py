"""
Demonstrate how to use Pythons list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
"""

"""
we cah use ascii code of different character 
"""

def produce_letter_list() -> list[str]:
    return [chr(i) for i in range(97, 97+26)]

def main():
    res = produce_letter_list()
    if res != None:
        print(res)

if __name__=="__main__":
	main()
