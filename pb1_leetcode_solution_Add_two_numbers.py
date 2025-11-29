# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):

    def get_sum_carry(self, n1, n2, prev_c):
        tot_sum = int(n1+n2+prev_c)
        if tot_sum >= 10:
            c = int(tot_sum/10)
            tot_sum = tot_sum % 10
        else:
            c = 0

        return tot_sum, c

    def find_len(self, listnode):
        leng = 0
        while listnode:
            listnode = listnode.next
            leng +=1
        return leng

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        l3 = None
        nodes_list = []
        cur_val1 = l1.val if l1 else 0
        cur_val2 = l2.val if l2 else 0
        c = 0
        while(l1 or l2):
            
            if not l3:
                s, c = self.get_sum_carry(cur_val1,cur_val2, c)
                l3 = ListNode(s)
                
                print("adding", cur_val1, cur_val2, "=" ,s, "carry ",c)
            else:
                cur_val1 = l1.val if l1 else 0
                cur_val2 = l2.val if l2 else 0
                s, c = self.get_sum_carry(cur_val1,cur_val2, c)
                print("adding", cur_val1, cur_val2, "=" ,s, "carry ",c)
                l3.next = ListNode(s)
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        print([self.find_len(node) for node in nodes_list])
        return l3