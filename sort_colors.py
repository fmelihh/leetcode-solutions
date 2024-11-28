# Problem Url: https://leetcode.com/problems/sort-colors, Medium

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = key


if __name__ == "__main__":
    s = Solution()
    s.sortColors([2, 0, 2, 1, 1, 0])  # [0,0,1,1,2,2]
    s.sortColors([2, 0, 1])  # [0,1,2]
