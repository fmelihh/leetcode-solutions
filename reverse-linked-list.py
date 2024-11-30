# Problem Url: https://leetcode.com/problems/reverse-linked-list, Easy
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        values = values[::-1]
        if len(values) == 0:
            return None

        root = ListNode(val=values[0])
        temp = root
        for i in range(1, len(values)):
            temp.next = ListNode(val=values[i])
            temp = temp.next

        return root


if __name__ == '__main__':
    pass

