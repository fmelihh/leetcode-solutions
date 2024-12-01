# Problem Url: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree, Easy
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sorted_array_bst_to_recursive(
        self, nums: List[int], start: int, end: int
    ) -> Optional[TreeNode]:
        if start > end:
            return None

        mid = start + (end - start) // 2

        root = TreeNode(val=nums[mid])
        root.left = self.sorted_array_bst_to_recursive(nums, start, mid - 1)
        root.right = self.sorted_array_bst_to_recursive(nums, mid + 1, end)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sorted_array_bst_to_recursive(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    pass
