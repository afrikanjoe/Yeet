"""
Implementation of LCS as an introduction to Dynamic Programming 
"""

class Solution: 
    def findLCS(self,s,t):
        m = len(s)
        n = len(t)
        arr = []
        for i in range(m):
            arr.append([0]*n)
        for i in range(m):
            for j in range(n):
                if(S[i]!=T[j]):
                    val1 =0
                    val2 =0 
                    if(i-1>=0):
                        val1 = arr[i-1][j]
                    if(j-1>=0):
                        val2 = arr[i][j-1]
                    arr[i][j] = max(val1,val2)
                else:
                    val = 0 
                    if(i-1>=0 and j-1>=0):
                        val = arr[i-1][j-1]
                    arr[i][j] = 1 +val 
        return self.getSubSequence(arr,S,T)




    def getSubSequence(self,arr,S,T):
        LCS = []
        m = len(arr)
        n = len(arr[0])
        mi = m-1
        ni = n-1
        while mi>=0 and ni>=0:
            val = 0 
            val2 = 0 
            char = S[mi]
            #print(mi,ni,char)
            # value of right character
            if (ni+1<n):
                val = arr[mi][ni+1]
            # value of character above
            if(mi-1>=0):
                val2 = arr[mi-1][ni]

            if(arr[mi][ni]>val  and arr[mi][ni]>val2):
                LCS.append(char)
                mi-=1
                ni-=1
            elif(arr[mi][ni]==val):
                ni+=1
            elif(arr[mi][ni]==val2):
                mi-=1
        return "".join(LCS[::-1])



            


if __name__=="__main__":
    S = "ABAZDC"
    T = "BACBAD"
    print(Solution().findLCS(S,T))