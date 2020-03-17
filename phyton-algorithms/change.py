# Uses python3
import sys

#The goal in this problem is to find the minimum number of coins needed to change the input value(an integer) into coins with denominations 1, 5, and 10

def get_change(m):
    
    coins = 0;

    if m >= 10:
        coins += int(m / 10);
        m = m % 10;
    if m >= 5:
        coins += int(m / 5);
        m = m % 5;

    coins += int(m);
    return coins;

#if __name__ == '__main__':
m = int(input())
print(get_change(m))
