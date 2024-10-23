# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        next = head.next

        if next.val == head.val:
            while next and next.val == head.val:
                next = next.next
            return self.deleteDuplicates(next)
        else:
            head.next = self.deleteDuplicates(next)
            return head


    def create_linked_list(self, elements):
        if not elements:
            return None
        head = ListNode(elements[0])
        current = head
        for val in elements[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def print_linked_list(self, head):
        while head is not None:
            print(head.val)
            head = head.next

array = [1, 1, 1, 2, 3]
solution = Solution()
head = solution.create_linked_list(array)
res = solution.deleteDuplicates(head)
solution.print_linked_list(res)
