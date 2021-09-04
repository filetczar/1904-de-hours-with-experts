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

    def _find_bigger(n, i, x, next_largest_val =[]) -> list: 

        if i <= 0:
            return next_largest_val
        elif x < 0: 
           return _find_bigger(n, i-1, i-2, next_largest_val) 
        elif n[i] > n[x]: 
            n_ = n.copy()
            n_[i], n_[x] = n_[x], n_[i]
            shrink_n = n_[x+1:len(n_)]
            shrink_n.sort()
            n_[x+1:len(n_)] = shrink_n
            int_n = int("".join(n_))
            try: 
                if int_n < min(next_largest_val):
                    next_largest_val.clear()
                    next_largest_val.append(int_n)
            except ValueError:
                next_largest_val.append(int_n) 
            return _find_bigger(n, i, x - 1, next_largest_val) 
        else:
            return _find_bigger(n, i, x - 1, next_largest_val)


    # make object mutable  
    n_list = list(str(number))
    # starting end index: i 
    i_ = len(n_list) -1 
    # iterate through each next index
    x_ = i_ -1 

    new_number = _find_bigger(n_list, i_, x_, next_largest_val=[])
    if len(new_number) == 0:
        return -1 
    else: 
        min_new_number = min(new_number)
        return min_new_number

if __name__ == "__main__":
    next_number = next_biggest_number(sys.argv[1])
    print(next_number)