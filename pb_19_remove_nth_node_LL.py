# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        i=1
        head1 = head
        while(head1.next != None):
            i+=1
            head1 = head1.next
        
        n_from_start = i - n 

        # print("total number of items ", i)
        # print("nth from last ", n)
        # print("nth from first ", n_from_start)

        result = ListNode(head1.val)
        result1 = result

        if i == 1:
            return None


        i=0
        while(head != None):
            i+=1
            print("checking i, n_from_start", i, n_from_start)

            if i != n_from_start+1:
                result.val = head.val
                result.next = head.next
                if i+1 == n_from_start+1:
                    if head.next.next == None:
                        result.next = None
                
                result = result.next
            head = head.next

            

          
        
        return result1