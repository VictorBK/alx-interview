#!/usr/bin/python3
""" makeChange function """

def makeChange(coins, total):
    if total == 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while total - coin >= 0:
            total -= coin
            count += 1
        if total == 0:
            return count
    return -1
