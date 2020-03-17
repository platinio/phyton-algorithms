# Uses python3
import sys
import math

def binary_search(a, x):
    low = 0;
    high = len( a ) - 1;
    return binary_search_recursive( a , low , high , x );

def binary_search_recursive( a , low , high , value ):

    mid = low + math.ceil((high - low) / 2);
       

    if( a[mid] == value  ):
        return mid;
    if( a[mid] > value ):
        high = mid - 1;
    if( a[mid] < value ):
        low = mid + 1;    

    if(low > high):
        return -1; 

    return binary_search_recursive( a , low , high , value );

array = [0 , 1 , 2 , 3 , 4 , 5];
index = binary_search( array , 6 );

print(index);