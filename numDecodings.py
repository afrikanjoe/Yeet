"""

lru_cache() is one such function in functools module which helps in reducing the execution time of the function by using memoization technique.

This is kind of sick

"""





from functools import lru_cache



class Solution:
    def numDecodingsExponential(self, s):
        if(not s):
            return
        count = 0 
        answers = []
        queue = [([],s)]
        while queue:
            curr_list, curr_s = queue.pop()
            if(len(curr_s)==0):
                if(curr_list not in answers):
                    answers.append(curr_list)
                    count+=1
            else:
                one_digit = int(curr_s[0:1])
                if(one_digit>0):
                    new_list = curr_list[:]+[one_digit]
                    queue.append((new_list,curr_s[1:]))
                if(len(s)>1):
                    two_digit = int(curr_s[0:2])
                    if(two_digit<27 and two_digit>9):
                        new_list = curr_list[:]+[two_digit]
                        queue.append((new_list,curr_s[2:]))                   
        return count

    @lru_cache(maxsize=None)
    def recursiveWithMemo(self, index, s):
        # If you reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1

        # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0

        if index == len(s)-1:
            return 1
        
        answer = self.recursiveWithMemo(index + 1, s)
        if int(s[index : index + 2]) <= 26:
            answer += self.recursiveWithMemo(index + 2, s)

        return answer

    def numDecodings(self, s):
        return self.recursiveWithMemo(0, s)
        

if __name__ == "__main__":
    s = "226"
    print(Solution().numDecodings(s))
    s = "11106"
    print(Solution().numDecodings(s))
