# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        self.ft_sorted(head)
        current = head
        while current and current.next:
            if current.val == current.next.val:
                self.remove_next_node(current)
                continue
            current = current.next
        return head

    def remove_next_node(self, head):
        if head.next and head.next.next:
            head.next = head.next.next
        else:
            head.next = None

    def ft_sorted(self, head):
        sorted = False
        while not sorted:
            sorted = True
            current = head
            while current and current.next:
                if current.val > current.next.val:
                    current.val, current.next.val = current.next.val, current.val
                    sorted = False
                current = current.next
        return head

    def print_linked_list(self, head):
        while head is not None:
            print(head.val)
            head = head.next

    def create_linked_list(self, elements):
        if not elements:
            return None
        head = ListNode(elements[0])
        current = head
        for val in elements[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

elements = [-50,-49,-48,-47,-46,-45,-43,-42,-41,-40,-39,-38,-37,-36,-35,-34,-33,-32,-31,-30,-28,-27,-26,-25,-24,-22,-21,-20,-19,-18,
            -17,-16,-15,-14,-13,-12,-10,-9,-8,-7,-6,-5,-4,-3,-1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,25,26,28,
            29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]


solution = Solution()
head = solution.create_linked_list(elements)
solution.deleteDuplicates(head)
