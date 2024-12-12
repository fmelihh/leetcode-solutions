# Problem Url: https://leetcode.com/problems/palindrome-linked-list/?envType=problem-list-v2&envId=recursion, Easy

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left = [head]

        def check_palindrome(left: list[Optional[ListNode]], right: Optional[ListNode]) -> bool:
            if right is None:
                return True

            res = check_palindrome(left, right.next)
            if res is False:
                return False

            cmp = left[0].val == right.val
            left[0] = left[0].next
            return cmp

        return check_palindrome(left, head)


if __name__ == "__main__":
    pass
