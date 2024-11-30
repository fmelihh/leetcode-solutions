# Problem Url: https://leetcode.com/problems/reverse-linked-list, Easy
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_count = self.maxDepth(root.left)
        right_count = self.maxDepth(root.right)

        return max(left_count, right_count) + 1

if __name__ == "__main__":
    pass
