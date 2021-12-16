"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
 
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
"""





class Solution:
    def compress(self, chars):
        
        output = []
        
        prev = chars[0] 
        count = 0
        
        for i in chars:
            if(i==prev):
                count+=1
            else:
                if(count==1):
                    output.append(prev)
                else:
                    output.append(prev)
                    num_str = list(str(count))
                    output+=num_str
                count=1
            prev = i 
        if(count==1):
            output.append(prev)
        else:
            output.append(prev)
            num_str = list(str(count))
            output+=num_str
        
        while chars:
            chars.pop()
            
        for i in output:
            chars.append(i)

if __name__ == "__main__":
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(chars)
    Solution().compress(chars)
    print(chars)