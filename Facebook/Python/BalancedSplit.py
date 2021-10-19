"""
Given an array of integers (which may include repeated integers), determine if there's a way to split the array into two subsequences 
A and B such that the sum of the integers in both arrays is the same, and all of the integers in A are strictly smaller than all of the integers in B.
Note: Strictly smaller denotes that every integer in A must be less than, and not equal to, every integer in B.

arr = [1, 5, 7, 1]
output = true
We can split the array into A = [1, 1, 5] and B = [7].

"""

def balancedSplitExists(arr):
  # Write your code here
  arr = sorted(arr)
  index1 = 0 
  index2 = len(arr)-1
  while index1 < index2:
    arr1_sum = sum(arr[0:index1+1])
    arr2_sum = sum(arr[index2:])
    if(arr1_sum<=arr2_sum):
      index1+=1
    else:
      index2-=1
  
  # check for decreasing requirement
  if(arr[index1-1]>=arr[index2]):
    return False
  else:
    return sum(arr[0:index1]) ==  sum(arr[index2:])
  
# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [2, 1, 2, 5]
  expected_1 = True
  output_1 = balancedSplitExists(arr_1)
  check(expected_1, output_1)

  arr_2 = [3, 6, 3, 4, 4]
  expected_2 = False
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  arr_2 = [4, 4, 4,12]
  expected_2 = True
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)
  
  arr_2 = [4, 4, 4,4,4,12]
  expected_2 = False
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)
  
  arr_2 = [3, 3, 4,5,6]
  expected_2 = False
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)
  
  