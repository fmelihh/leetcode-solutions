from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        state = [None]

        def preorderTraversal(node: Optional[TreeNode], _target):
            if node:
                if isinstance(_target, int):
                    if _target == node.val:
                        state[0] = node
                else:
                    if _target == node:
                        state[0] = node.val

                preorderTraversal(node.left, _target)
                preorderTraversal(node.right, _target)

        preorderTraversal(original, target)
        preorderTraversal(cloned, state[0])
        return state[0]
        
