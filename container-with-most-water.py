# Problem Url: https://leetcode.com/problems/container-with-most-water/description/?envType=problem-list-v2&envId=array, Medium
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) in (0, 1):
            return 0

        max_area = 0
        start, end = 0, len(height) - 1
        while start < end:
            max_area = max(max_area, (min(height[start], height[end]) * (end - start)))

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area


if __name__ == "__main__":
    s = Solution()
    s.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])  # 49
