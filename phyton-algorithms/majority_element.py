# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    
    get_majority_element(a , left , right / 2);
    get_majority_element(a , left + (right / 2) , right);


    return -1
