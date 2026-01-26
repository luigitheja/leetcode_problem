# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        master_list = []

        for node_list in lists:

            cur_node = node_list

            while cur_node:
                master_list.append(cur_node.val)
                cur_node = cur_node.next
        
        master_list.sort()
        print("the master list is ", master_list)

        if not master_list:
            return ListNode().next
        else:
            dummy = ListNode(master_list[0])
            current = dummy

            for i in range(1, len(master_list)):
                dummy.next = ListNode(master_list[i])
                dummy = dummy.next

            return current

        