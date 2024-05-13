class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        first = ListNode()
        current = first
        carry = 0
        
        while l1 or l2 or carry:
            # Calculate sum of current digits and carry
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            
            # Update carry and create new node for sum
            carry = sum_val // 10
            current.next = ListNode(sum_val % 10)
            current = current.next
        
        return first.next
