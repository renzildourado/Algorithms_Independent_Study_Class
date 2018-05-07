class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        final_sum = 0
        i = 0
        current = -1
        current_index = 0

        while i < len(height):
            if height[i] != 0:
                current = height[i]
                current_index = i
                i += 1
                sum = 0
                while i < len(height) and height[i] < current:
                    sum += current - height[i]
                    i += 1

                if i != len(height):
                    final_sum += sum

            else:
                i += 1

        i = len(height) - 1

        current = -1
        while i >= current_index:
            if height[i] != 0:
                current = height[i]
                i -= 1
                sum = 0
                while i >= current_index and height[i] < current:
                    sum += current - height[i]
                    i -= 1

                if i != -1:
                    final_sum += sum

            else:
                i -= 1

        return final_sum

obj = Solution()

print(obj.trap(height=[4,2,3]))


