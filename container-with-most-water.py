# Not finish yet
# Problem Url: https://leetcode.com/problems/container-with-most-water/description/?envType=problem-list-v2&envId=array, Medium
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        first, second = 0, 0
        area = 0
        areas = []
        for i in range(1, len(height)):
            if height[i] < height[first]:
                if first > second:
                    continue

                new_area = (i - first) * (i - 1)
                if new_area > area:
                    area = new_area
                    first = i
            else:
                first = i
                second = 0

        return area


if __name__ == "__main__":
    s = Solution()
    s.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])  # 49
