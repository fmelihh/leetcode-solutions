# Problem Url: https://leetcode.com/problems/remove-linked-list-elements/?envType=problem-list-v2&envId=recursion, Easy

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        def delete_nodes(node: Optional[ListNode]) -> Optional[ListNode]:
            if node is None:
                return None

            if node.val == val: # next
                return delete_nodes(node.next)

            node.next = delete_nodes(node.next)
            return node

        head = delete_nodes(head)
        return head


if __name__ == '__main__':
    pass
