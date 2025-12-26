'''
1. Generate a random integer between 1 and 100.
'''

import random
from typing import Tuple

def random_a_and_b(a: int, b: int)->int:
    '''
    Generate a random number between a and b (eg. 1 and 100)
    '''
    if a>b:
        raise ValueError("a must be less than or equal to b")
    return random.randint(a, b)
    
def get_user_input() -> Tuple[int, int]:
    '''
    Read user inputs
    '''
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        return a,b
    except ValueError as err:
        raise ValueError("Input must be valid integers") from err
        
def main() -> None:
    try:
        a, b = get_user_input()
        result = random_a_and_b(a, b)
        print(f"Random Number between {a} and {b} : {result}")
    except ValueError as err:
        print(f"Error: {err}")
        
if __name__ == "__main__":
    main()
    
# Enter a: 1
# Enter b: 100
# Random Number between 1 and 100 : 71
