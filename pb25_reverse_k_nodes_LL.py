# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #solution courtesy : professor0akes yt

        def get_reversed_list(head1, k):
            cur_node = head1
            prev = None
            i=0
            next_node = None
            while(i<k): 

                # print("before switching ", next_node, cur_node, prev)

                #change pointer
                next_node = cur_node.next
                cur_node.next = prev
                #move to next item
                prev = cur_node
                cur_node = next_node

                # print("after switching ", next_node, cur_node, prev)

                i=i+1
            return prev

        def get_length(head1):
            dum = head1
            llen = 0
            while(dum):
                llen +=1
                dum = dum.next
            return llen
        
        def print_nodes(head1):
            while(head1):
                print(head1.val, end="->")
                head1 = head1.next
            return

        # reversed_head = get_reversed_list(head, 3)

        tot_len = get_length(head)

        #for keeping track of first overall head
        overall_head = head
        first_time = True

        #for keeping track of each sub group start and end after reversing
        group_head = head
        prev_group_tail = None

        #for keeping track of next group start after each iteration
        dummy = head


        while(tot_len >= k):

            #dummy.next will contain next group starting
            i=0
            while(i<k):
                dummy = dummy.next
                i=i+1
            
            group_head = get_reversed_list(group_head, k)


            if first_time:
                overall_head = group_head
                first_time = False

            
            
            print("\nresult after iteration ")
            print("\noverall head")
            print_nodes(overall_head)
            print("\ncurrent head")
            print_nodes(group_head)
            print("\n--------------")
            print("\ndummy")
            print_nodes(dummy)
            print("\n--------------")
            

            group_tail = group_head

            while(group_tail.next):
                group_tail = group_tail.next

            if prev_group_tail:
                prev_group_tail.next = group_head
                prev_group_tail = group_tail
            else:
                prev_group_tail = group_tail
            
            group_tail.next  = dummy
            group_head = dummy

            print("\ncurrent head1")
            print_nodes(group_head)

            print("\noverall head1")
            print_nodes(overall_head)

            tot_len -= k
        
        return overall_head