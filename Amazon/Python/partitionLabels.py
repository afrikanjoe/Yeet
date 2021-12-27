class Solution:
    def partitionLabels(self, s):
        
        # find the last occurence of each letter
        last = {c: i for i, c in enumerate(s)}
        
        # anchor is used to compute the length
        j = anchor = 0 
        ans = []
        
        # for each character and index in s
        for i, c in enumerate(s): 
            
            # find the farthest right char for the current character
            # and the original letter
            j = max(j, last[c])
            
            # if i==j then we need a new partition
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans

if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"
    print(Solution().partitionLabels(s))