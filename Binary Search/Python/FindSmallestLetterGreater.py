class Solution:
    @staticmethod
    def nextGreatestLetter(letters,target):
        mina = 100
        best = None
        for  i in letters:
            diff = (ord(i)+1)-(ord(target)+1)
            diff = diff % 26
            if(diff>0 and diff<mina):
                best = i
                mina=diff
        return best
    @staticmethod
    def nextGreatestLetterBinary(letters,target):
        if target >= letters[-1]:
            return letters[0]
        low = 0 
        high = len(letters)-1
        while (low<high):
            mid = low +high >>1
            if(letters[mid]<=target):
                low = mid +1
            else:
                high = mid
        return letters[low]




if __name__=="__main__":
    inp = ["c","f","j"]
    target = "c"
    print(Solution.nextGreatestLetter(inp,target))
    print(Solution.nextGreatestLetterBinary(inp,target))
