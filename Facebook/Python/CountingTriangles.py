"""
Given a list of N triangles with integer side lengths, determine how many different triangles there are. 
Two triangles are considered to be the same if they can both be placed on the plane such that their 
vertices occupy exactly the same three points.

arr = [[2, 2, 3], [3, 2, 2], [2, 5, 6]]
output = 2
The first two triangles are the same, so there are only 2 distinct triangles.
"""


def countDistinctTriangles(arr):
  # Write your code here
  count = 0
  triangle_list =[]
  for triangle in arr:
    tr = sorted(triangle)
    if(tr not in triangle_list):
      count+=1
      triangle_list.append(tr)
  return count

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
  arr_1 = [(7, 6, 5), (5, 7, 6), (8, 2, 9), (2, 3, 4), (2, 4, 3)]
  expected_1 = 3
  output_1 = countDistinctTriangles(arr_1)
  check(expected_1, output_1)

  arr_2 = [(3, 4, 5), (8, 8, 9), (7, 7, 7)]
  expected_2 = 3
  output_2 = countDistinctTriangles(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  arr = [[2, 2, 3], [3, 2, 2], [2, 5, 6]]
  expected_2 = 2
  output_2 = countDistinctTriangles(arr)
  check(expected_2, output_2)
  
  arr =  [[8, 4, 6], [100, 101, 102], [84, 93, 173]]
  expected_2 = 3
  output_2 = countDistinctTriangles(arr)
  check(expected_2, output_2)
  
  
  arr =  [[5, 8, 9], [5, 9, 8], [9, 5, 8], [9, 8, 5], [8, 9, 5], [8, 5, 9]]
  expected_2 = 1
  output_2 = countDistinctTriangles(arr)
  check(expected_2, output_2)
  
  