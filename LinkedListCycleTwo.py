# 連結リストのheadを受け取る
# サイクルの初めのノードを返す
# もしサイクルでなければ null を返す

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        else: return None
        while head != slow:
            head, slow = head.next, slow.next
        return head

Node1 = ListNode(5)
Node2 = ListNode(6)
Node3 = ListNode(7)
Node4 = ListNode(8)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node2

head = Node1
solution = Solution()
print(solution.detectCycle(head))
