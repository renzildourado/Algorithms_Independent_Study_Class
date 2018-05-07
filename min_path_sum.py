class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dynamic_program_array = []

        for i in range(len(grid)):
            dynamic_program_array.append([])
            for j in range(len(grid[0])):
                dynamic_program_array[i].append(0)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i-1>= 0 and j-1 >=0:
                    dynamic_program_array[i][j] = min(dynamic_program_array[i-1][j], dynamic_program_array[i][j-1]) + grid[i][j]

                elif i-1 >= 0:
                    dynamic_program_array[i][j] = dynamic_program_array[i - 1][j] + grid[i][j]

                elif j-1 >=0:
                    dynamic_program_array[i][j] = dynamic_program_array[i][j-1] + grid[i][j]

                else:
                    dynamic_program_array[i][j] = grid[i][j]

        return dynamic_program_array[-1][-1]


obj = Solution()
print(obj.minPathSum([[1,2],[1,1]]))