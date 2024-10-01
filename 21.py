"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


def convert_list_to_list_node(list_items):
    i = len(list_items)
    first_node = None
    while i > 0:
        first_node = ListNode(list_items[i - 1], first_node)
        #print(first_node.val, first_node.next)
        i -= 1
    return first_node

def convert_list_node_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == '__main__':
    solution = Solution()

    list1 = convert_list_to_list_node([1, 2, 4])
    list2 = convert_list_to_list_node([1, 3, 4])
    merged = solution.mergeTwoLists(list1, list2)
    print(convert_list_node_to_list(merged))

    list1 = convert_list_to_list_node([])
    list2 = convert_list_to_list_node([])
    merged = solution.mergeTwoLists(list1, list2)
    print(convert_list_node_to_list(merged))

    list1 = convert_list_to_list_node([])
    list2 = convert_list_to_list_node([0])
    merged = solution.mergeTwoLists(list1, list2)
    print(convert_list_node_to_list(merged))