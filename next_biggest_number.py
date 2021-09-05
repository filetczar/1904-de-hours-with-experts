#!/usr/bin/python3*

import sys

def next_biggest_number(number: int) -> int: 
    """
    This method finds the next largest value given an integer by rearranging that number's digits.
    If a larger number cannot be created, the function returns -1.

    Methodology: 
        This function recursively iterates from the last digit (i) until the first digit (x). 
        If switching these digits creates a larger number (number[i] > number[x]), they are switched. 
        Then that number is "shrunk" by sorting the trailing digits from least to greatest to ensure the next highest value. 
        All possible greater numbers are exhaustively searched in order to ensure we find the next largest sequential value. 
    Pre Processing:
        To make an integer mutable, it is transformed into a list object 
    Args:
        number (int): A non-negative integer 
    Returns:
        int: The next largest integer or -1 if a larger value can not be created 
    """

    def _find_bigger(n: list, i: int, x: int, next_largest_val: int = None) -> int: 

        if i <= 0:
            return next_largest_val
        elif x < 0: 
           return _find_bigger(n, i-1, i-2, next_largest_val) 
        elif n[i] > n[x]: 
            n_ = n.copy()
            n_[i], n_[x] = n_[x], n_[i]
            sorted_n = n_[0:x+1] + sorted(n_[x+1:len(n_)])
            int_n = int("".join(sorted_n))
            if next_largest_val:
                if int_n < next_largest_val:
                    next_largest_val = int_n 
            else:
                next_largest_val = int_n
            return _find_bigger(n, i, x - 1, next_largest_val) 
        else:
            return _find_bigger(n, i, x - 1, next_largest_val)

    # make object mutable and start iteration from nth digit (i)  
    n_list = list(str(number))
    i_ = len(n_list) -1 
    x_ = i_ -1 

    next_value = _find_bigger(n_list, i_, x_, next_largest_val=None)
    if next_value:
        return next_value
    else:
        return -1 

if __name__ == "__main__":
    next_number = next_biggest_number(sys.argv[1])
    print(next_number)