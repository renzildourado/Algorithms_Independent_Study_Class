class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        solution = {")":"(", "]":"[", "}":"{", "(":")", "[":"]", "{":"}"}

        for bracket in s:
            if len(stack) > 0:

                if stack[-1] == solution[bracket]:
                    stack.pop()
                else:
                    stack.append(bracket)
            else:
                stack.append(bracket)

        if len(stack)== 0:
            return True
        else:
            return False

obj = Solution()
print(obj.isValid("()"))