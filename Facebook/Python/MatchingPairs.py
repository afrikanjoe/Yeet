"""
Given two strings s and t of length N, find the maximum number of possible matching pairs in strings s and t after swapping exactly two characters within s.
A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that is present at the ith and jth index of s, respectively. 
The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i] are equal.
Note: This means you must swap two characters at different indices.
Signature
int matchingPairs(String s, String t)
Input
s and t are strings of length N
N is between 2 and 1,000,000
Output
Return an integer denoting the maximum number of matching pairs
Example 1
s = "abcd"
t = "adcb"
output = 4
Explanation:
Using 0-based indexing, and with i = 1 and j = 3, s[1] and s[3] can be swapped, making it  "adcb".
Therefore, the number of matching pairs of s and t will be 4.
Example 2
s = "mno"
t = "mno"
output = 1



"""


# Add any helper functions you may need here

def check_len3_string(s,t):
  for i in t:
    if i not in s:
      return False
  return True
def matching_pairs(s, t):
  # Write your code here
  if(s==t):
    # edge case 1 
    if(len(set(s))==len(s)):
      return len(s)-2
    else:
      return len(s)
  else: 
    count = 0 
    for i in range(len(s)):
      if(s[i]==t[i]):
        count+=1
    
    # edge case for length 2 strings
    if(len(s)==2 and count==0):
      if(s[0]==t[1]):
        return 1
      
    # edge case for length 3
    if(len(s)==3 and count==2 and len(set(s))<3):
      return count 
    elif(len(s)==3 and count==2 and check_len3_string(s,t)):
      return count
    if(count==len(s)-1):
      return count -1
    return count+2
  
  
# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)
  # Add your own test cases here
  s_2, t_2 = "mna", "mno"
  expected_2 = 1
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)
  
  s_2, t_2 = "abca", "abcf"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)
  
  s_2, t_2 = "aba", "axa"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)
  
  s_2, t_2 = "abx", "abb"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)
  
  s_2, t_2 = "abb", "axb"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)
  
  s_2, t_2 = "ax", "ya"
  expected_2 = 1
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)
  
  s_2, t_2 = "aabb", "aabb"
  expected_2 = 4
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)
  
  s_2, t_2 = "bb", "bb"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)
  
  