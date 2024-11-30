# Problem Url: https://leetcode.com/problems/sort-list/?envType=problem-list-v2&envId=merge-sort, Medium
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        while head:
            array.append(head.val)
            head = head.next

        if len(array) == 0:
            return None

        def merge(array: list[int], left: int, mid: int, right: int):
            n1 = mid - left + 1
            n2 = right - mid

            L = [0] * n1
            R = [0] * n2

            for i in range(n1):
                L[i] = array[left + i]

            for j in range(n2):
                R[j] = array[mid + 1 + j]

            i = 0
            j = 0
            k = left
            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = R[j]
                    j += 1
                k += 1

            while i < n1:
                array[k] = L[i]
                i += 1
                k += 1

            while j < n2:
                array[k] = R[j]
                j += 1
                k += 1

        def merge_sort(array: list[int], left: int, right: int):
            if left < right:
                mid = (left + right) // 2
                merge_sort(array, left, mid)
                merge_sort(array, mid + 1, right)
                merge(array, left, mid, right)

        merge_sort(array=array, left=0, right=len(array) - 1)
        root = ListNode(val=array[0])
        temp = root

        for i in range(1, len(array)):
            temp.next = ListNode(val=array[i])
            temp = temp.next

        return root


if __name__ == "__main__":
    pass
