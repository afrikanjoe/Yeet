"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

"""

class Solution:
    def oddEvenList(self, head):
        
        even_list = []
        odd_list  = []
        count = 0 
        
        while head: 
            if(count%2==0):
                even_list.append(head)
            else:
                odd_list.append(head)
                
            head = head.next 
            count+=1
        
        all_nodes = even_list+odd_list
        
        for i in range(len(all_nodes)-1):
            all_nodes[i].next = all_nodes[i+1]
            
        if(len(all_nodes)>0):
            all_nodes[-1].next = None
            return all_nodes[0]
        else:
            return 