# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        extra = 0
        sol = []
        while l1 is not None or l2 is not None or extra > 0:
            l1_digit = l1.val if l1 is not None else 0
            l2_digit = l2.val if l2 is not None else 0

            sol_sum = l1_digit + l2_digit + extra
            digit = sol_sum % 10
            extra = sol_sum // 10

            sol.append(digit)
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return toListNode(sol)


def toListNode(l: list):
    head = ListNode(l[0])
    actual = head
    for element in l[1:]:
        value = ListNode(element)
        actual.next = value
        actual = actual.next
    return head