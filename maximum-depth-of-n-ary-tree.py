"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    @staticmethod
    def findMax(heights: list[int]):
        if not heights:
            return 0

        heights.sort()
        return heights[-1]

    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        return 1 + self.findMax([self.maxDepth(children) for children in root.children])
        
