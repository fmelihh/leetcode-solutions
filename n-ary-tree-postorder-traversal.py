"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        vals = []

        def _postortder_traversal(node: 'Node'):
            if not node:
                return
            
            for child in node.children:
                _postortder_traversal(child)
            
            vals.append(node.val)
        
        _postortder_traversal(root)
        return vals

        
