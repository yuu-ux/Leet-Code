class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False



node1 = ListNode(3)
node2 = ListNode(4)
node3 = ListNode(5)
node4 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

head = node1

linked_list = LinkedList()
print(linked_list.is_cycle(head))
