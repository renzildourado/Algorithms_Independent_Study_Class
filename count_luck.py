#!/bin/python3

import os
import sys

# Complete the countLuck function below.
def countLuck(matrix, k):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            pass



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input())

        result = countLuck(matrix, k)

        print(result)
        # fptr.write(result + '\n')

    # fptr.close()