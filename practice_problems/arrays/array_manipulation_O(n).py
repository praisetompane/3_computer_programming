#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
'''
    for all a, b, k:
        set instruction to increment by k:
            from index a to index n: HOW? 
                    mark where the increase by k must start with k(i.e. array[a] = 100)
                BUT since we actually ONLY want to increment by until index b
                    set instruction to decrement by k from {b + 1 to n} HOW?
                        mark where the decrease by k must start with -k(i.e. array[b+1] = -k)
                    
    NB: Since we are not actually goin from a to b<=n
        the cost of setting the instruction to:
            increment by k
            decrement by k
            is O(1)
    
'''

'''
    array = [n]

    queries = [
                x,y,z
                x,y,z
              ]
'''

def arrayManipulation(n, queries):
    sums = [0] * n
    for query in queries:
        k = query[2]
        sums[query[0]] += k     #set start index from where all indices are incremented by k
        sums[query[1]] += -k    #set start index from where all indices are decremented by k
    max_consective_inrease = 0
    for i in range(len(sums)):
        if max_consective_inrease < max_consective_inrease + sums[i]:
            max_consective_inrease = max_consective_inrease + sums[i]
                    
    return max_consective_inrease

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
