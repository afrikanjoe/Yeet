# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
 

class Solution:
    @staticmethod
    def addTwoNumbers(l1, l2):
        if(l1 and l2):
            d1 = [str(l1.val)]
            d2 = [str(l2.val)]
            while(l1.next):
                l1 = l1.next
                d1.append(str(l1.val))
            while(l2.next):
                l2 = l2.next
                d2.append(str(l2.val))
            d1 = d1[::-1]
            d2 = d2[::-1]
            num = str(int("".join(d1))+int("".join(d2)))[::-1]
            start = ListNode(int(num[0]),None)
            temp = start
            for i in num[1:]:
                n3 = ListNode(int(i),None)
                temp.next = n3
                temp = n3
        else:
            return ListNode(0,None)
        return start

def createList(lista):
    start = ListNode(lista[0])
    temp = start
    for i in lista[1:]:
        n3= ListNode(i,None)
        temp.next = n3
        temp = n3 
    return start 

def getList(node):
    vals = []
    while(node):
        vals.append(node.val)
        node = node.next
    return vals

if __name__=="__main__":
    l1 = createList([2,4,9])
    l2 = createList([5,6,4,9])
    answer = Solution.addTwoNumbers(l1,l2)
    print(getList(l1))
    print(getList(l2))
    print(getList(answer))

            
            
    