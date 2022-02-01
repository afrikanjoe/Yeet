"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        
        new_list = []
        while list1 and list2:
            
            node_a = list1
            node_b = list2
            if(node_a.val<=node_b.val):
                new_list.append(node_a)
                list1 = list1.next
            else:
                new_list.append(node_b)
                list2 = list2.next
                
        while list1:
            new_list.append(list1)
            list1 = list1.next
        while list2:
            new_list.append(list2)
            list2 = list2.next
            
        for i in range(len(new_list)-1):
            node_a = new_list[i]
            node_b = new_list[i+1]
            node_a.next = node_b
        if(new_list):
            new_list[-1].next = None
            return new_list[0]

# if __name__ == "__main__":
#     list1 = [1,2,4]
#     list2 = [1,1,4,5,6,7]
#     print(Solution().mergeTwoLists(list1,list2))
