class Solution:
    def hammingWeight(self,n):
        n = "{0:b}".format(n)
        count = 0
        for i in n:
            if (i=='1'):
                count+=1
        return count
