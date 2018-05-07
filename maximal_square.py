def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """

    dynamic = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    max = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if j - 1 < 0:
                left = 0
            else:
                left = dynamic[i][j - 1]

            if i - 1 < 0:
                up = 0
            else:
                up = dynamic[i - 1][j]

            if left != 0 and up != 0:
                diagonal = dynamic[i - 1][j - 1]
            else:
                diagonal = 0

            if matrix[i][j] == "1":
                dynamic[i][j] = min(int(left), int(up), int(diagonal)) + 1
                if dynamic[i][j] > max:
                    max = dynamic[i][j]

            else:
                dynamic[i][j] = 0

    return max * max


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

#matrix = [["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]

print(maximalSquare(matrix))
