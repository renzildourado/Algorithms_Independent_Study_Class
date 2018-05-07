#!/bin/python3

import sys

s = input().strip()
# your code goes here

n = 6
previous_column = {}
previous_column[int(s[0]) % n] = 1
result = 0

if 0 in previous_column:
    result += previous_column[0]

for i in range(1, len(s)):
    number = int(s[i])
    current_column = {}

    for key in previous_column:
        current_column[int(key * 10 + number) % n] = previous_column[key]

    if int(number) % n in current_column:
        current_column[int(number) % n] += 1
    else:
        current_column[int(number) % n] = 1


    if int(s[i - 1]) == 0:
        current_column[int(number) % n] -= 1

    if 0 in current_column:
        result += current_column[0]
        
    previous_column = current_column

print(result)