#!/bin/python3

import sys


def gridlandMetro(n, m, k, track):
    # Complete this function

    track = sorted(track, key = lambda x : (x[0], x[1]))
    i = 0
    sum = 0
    while i < len(track):
        stack = []
        row = track[i][0]
        stack.append((track[i][1], track[i][2]))
        i += 1
        
        while i <len(track) and track[i][0] == row:
            current = (track[i][1], track[i][2])
            stack_top = stack.pop()

            if stack_top[0] <= current[0]<= stack_top[1] or stack_top[1] >= current[1] >= stack_top[0]:
                if current[1] > stack_top[1]:
                    new_tup = (stack_top[0], current[1])
                    stack.append(new_tup)

                else:
                    stack.append(stack_top)

            else:
                stack.append(stack_top)
                stack.append(current)

            i +=1

        for elements in stack:
            sum += elements[1] - elements[0] + 1


    result = (m*n) - sum

    return result


if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    track = []
    for track_i in range(k):
       track_t = [int(track_temp) for track_temp in input().strip().split(' ')]
       track.append(track_t)
    result = gridlandMetro(n, m, k, track)
    print(result)