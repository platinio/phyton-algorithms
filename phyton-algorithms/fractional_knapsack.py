# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    
    value = 0;
    while( capacity > 0 and len(weights) > 0):
        bestIndex = getBestValueItemIndex( weights , values );
        weight = min( weights[bestIndex] , capacity );
        capacity -= weight;
        valuePerUnit = values[bestIndex] / weights[bestIndex];
        value += (valuePerUnit * weight);        
        weights.pop(bestIndex);
        values.pop(bestIndex);  
        

    return value

def getBestValueItemIndex( weights , values ):
    bestValueIndex = 0;
    bestValue = -1;
    for n in range( len(weights) ):
        value = values[n] / weights[n];        
        if(value > bestValue):            
            bestValue = value;
            bestValueIndex = n;
    return bestValueIndex;


values = list(map(int, input().split()))
weights = list(map(int, input().split()))
cap = int(input())

value = get_optimal_value( cap , weights , values );
print("best value is " + str(value));

