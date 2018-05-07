class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    final_answer = []

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        answer = []
        self.final_answer = []

        self.path_helper(self, root, sum, answer)
        print(self.final_answer)

    def path_helper(self, root, sum, answer):

        if root == None:
            return

        if sum - root.val == 0 and root.left is None and root.right is None:
            self.final_answer.append(answer)

        answer.append(root.val)
        self.path_helper(self, root.left, sum - root.val, answer[:])
        self.path_helper(self, root.right, sum - root.val, answer[:])

tree = TreeNode(5)
tree.left = TreeNode(4)
tree.right = TreeNode(8)
tree.left.left = TreeNode(11)
tree.left.left.left = TreeNode(7)
tree.left.left.right = TreeNode(2)
tree.right.left = TreeNode(13)
tree.right.right = TreeNode(4)
tree.right.right.left = TreeNode(5)
tree.right.right.right = TreeNode(1)

obj = Solution
obj.pathSum(obj, root= tree, sum = 22)
