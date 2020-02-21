# Uses python3
import sys


def calc_fib_faster(n):

    if n in hashTable:
        return hashTable[n];

    if (n <= 1):
        return n
    fibA = hashTable[n - 1] if (n - 1) in hashTable else   calc_fib_faster(n - 1)
    hashTable[n - 1] = fibA
    fibB = hashTable[n - 2] if (n - 2) in hashTable else   calc_fib_faster(n - 2)   
    hashTable[n - 2] = fibB;

    return fibA + fibB

def calc_fib_module(fib , m):
    return ( calc_fib_faster( fib  ) ) % m;



hashTable = {0 : 0 , 1 : 1 }

fib = int(input())
result = calc_fib_faster(fib)

print( "fibonacci of " + str( fib ) + " is " + str( result ) )
    

