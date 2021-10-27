"""
An integer array original is transformed into a doubled array changed by appending twice 
the value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. 
If changed is not a doubled array, return an empty array. 
The elements in original may be returned in any order.
"""



class Solution:
    def findOriginalArray(self, changed):
        changed =sorted(changed)
        if(len(changed)%2==1):
            return []
        output = []
        count_dict = {}
        for i in range(len(changed)):    
            count_dict[changed[i]] = count_dict.get(changed[i],0)+1
            
        for i in changed:
            if(i==0):
                val = count_dict.get(i/2,0)
                if(val>1):
                    output.append(i)
                    count_dict[i] = val -2
            elif(i%2==0):
                val = count_dict.get(i/2,0)
                val2 = count_dict.get(i,0)
                if(val<=0 or val2<=0):
                    continue
                else:
                    output.append(int(i/2))
                    count_dict[i/2] = val -1
                    count_dict[i] = count_dict.get(i,0)-1
            else:
                val = count_dict.get(i*2,0)
                val2 = count_dict.get(i,0)
                if(val<=0 or val2<=0):
                    continue
                else:
                    output.append(int(i))
                    count_dict[i*2] = val -1
                    count_dict[i] = count_dict.get(i,0)-1
        if(len(output)==int(len(changed)/2)):
            return output
        else: 
            return []


if __name__=="__main__":
    changed = [1,3,4,2,6,8]
    print(Solution().findOriginalArray(changed))
    changed = [6,3,0,1]
    print(Solution().findOriginalArray(changed))
    changed = [1]
    print(Solution().findOriginalArray(changed))