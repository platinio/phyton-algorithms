# Uses python3
import sys

def optimal_summands(n):

    if(n == 1 ):
        return [1];
        

    summands = []
    counter = n;
    for j in range( 1 , n):
        if( (counter - j) >= j + 1):
            summands.append(j);
            counter -= j;
        else:
            summands.append(counter);
            return summands;
    return summands

n = int(input())
summands = optimal_summands(n)
for x in summands:
    print(x, end=' ')

