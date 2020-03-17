#Uses python3

import sys

def max_dot_product(a, b):
    
    result = 0;
    findMax = True;
    while( len(a) > 0 ):
        indexA = getMaxNumberIndex(a) if findMax else getMinNumberIndex(a);
        indexB = getMaxNumberIndex(b) if findMax else getMinNumberIndex(b);
        
        if( (findMax and (a[indexA] > 0 and b[indexB] > 0)) or (not findMax) ):
            result += a[indexA] * b[indexB];
            a.pop(indexA);
            b.pop(indexB);
        else:
            findMax = False;
    
    return result;

def getMaxNumberIndex(a):

    max = a[0];
    index = 0;

    for n in range( len(a) ):        
        if( max < a[n]):
            max = a[n];
            index = n;

    return index;

def getMinNumberIndex(a):

    min = a[0];
    index = 0;

    for n in range( len(a) ):        
        if( min > a[n]):
            min = a[n];
            index = n;

    return index;



a = list(map(int, input().split()))
b = list(map(int, input().split()))

print( max_dot_product( a , b ) );
    
