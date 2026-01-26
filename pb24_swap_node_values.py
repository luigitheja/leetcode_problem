# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        odd = True

        return_node = head

        while(head):

            if odd:
                cur_val = head.val
                if head.next:
                    head.val = head.next.val
                odd = False
            else:
                head.val = cur_val
                odd = True

            head = head.next
        
        return return_node