# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head):
        self.ll = []
        while head:
            self.ll.append(head.val)
            head = head.next

    def getRandom(self):
        
        return self.ll[random.randint(0,len(self.ll)-1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


# Resevoir Sampling is a family of algorithms which includes several variants over the time. Here we present a simple albeit slow one
# Also known as Algorithm R by Alan Waterman


 # S has items to sample, R will contain the result, k is the number of samples
    def ResevoirSample(S,R,k):

        # fill the resevoir array 
        for i in range(k):
            R[i] = S[i]
        

        # repalce the elements with a gradually decreasing probability
        for i in range(k+1,n)

            # randomInteger(a,b) generates a uniform integer
            # from the inclusive range {a,..,b}
            j = random.randin(0,i)
            if(j<k):
                R[j] = S[i]


class OptimalSolution:

     def __init__(self, head):
        self.head  = head

    def getRandom(self) -> int:
        
        k = 1
        chosen_value =0 
        curr=self.head
        while curr:
            # this will always be true for k =1
            if(random.random()<1/k):
                chosen_value = curr.val
                
            # move on to the next node
            curr = curr.next 
            k +=1
            
        return chosen_value

   
