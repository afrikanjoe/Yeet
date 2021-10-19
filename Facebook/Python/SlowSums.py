"""
Suppose we have a list of N numbers, and repeat the following operation until we're left with only a single number: Choose any two numbers and replace them with their sum. 
Moreover, we associate a penalty with each operation equal to the value of the new number, and call the penalty for the entire list as the sum of the penalties of each operation.
For example, given the list [1, 2, 3, 4, 5], we could choose 2 and 3 for the first operation, which would transform the list into [1, 5, 4, 5] and incur a penalty of 5. 
The goal in this problem is to find the highest possible penalty for a given input.

Example:
    - arr = [4, 2, 1, 3]
    - output = 26

    - First, add 4 + 3 for a penalty of 7. Now the array is [7, 2, 1]
    - Add 7 + 2 for a penalty of 9. Now the array is [9, 1]
    - Add 9 + 1 for a penalty of 10. The penalties sum to 26.
"""


# O(n^2)
def getTotalTime(arr):
  # Write your code here
  penalty = 0 
  while len(arr)>1:
    max1_index=arr.index(max(arr))
    val1 = arr.pop(max1_index)
    max2_index=arr.index(max(arr))
    val2 = arr.pop(max2_index)
    penalty+= (val1+val2)
    arr.append(val1+val2)
  return penalty
  


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
  arr_1 = [4, 2, 1, 3]
  expected_1 = 26
  output_1 = getTotalTime(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 3, 9, 8, 4]
  expected_2 = 88
  output_2 = getTotalTime(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  