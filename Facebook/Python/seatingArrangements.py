"""

There are n guests attending a dinner party, numbered from 1 to n. The ith guest has a height of arr[i-1] inches.
The guests will sit down at a circular table which has n seats, numbered from 1 to n in clockwise order around the table. 
As the host, you will choose how to arrange the guests, one per seat. Note that there are n! possible permutations of seat assignments.
Once the guests have sat down, the awkwardness between a pair of guests sitting in adjacent seats is defined as the absolute difference 
between their two heights. 
Note that, because the table is circular, seats 1 and n are considered to be adjacent to one another, and that there are therefore n pairs of adjacent guests.
The overall awkwardness of the seating arrangement is then defined as the maximum awkwardness of any pair of adjacent guests. 
Determine the minimum possible overall awkwardness of any seating arrangement.

Difficult if you don't notice the pattern... if you are minimizing height differences, imagine an unsorted list [a,b,c,d,e] 
you will be limited by the MAX difference occurring among 3 items when trying to minimize that difference. Can someone help me with a better way to word it?

Example: [2,4,6,20,40]... no matter what, 40 has to be next to 2 numbers. So we aren't limited by the neighbors [20,40] but instead by [6,40]
Example: [2,4,7,7,7]... it's harder to see, but 2,4,7 will be the limiting set and 5 would be the max height difference.

So we will always be limited by the skip-an-item pairs in the sorted list. Sorting helps us minimize the differences, and then we want to find the max.

Code below. Time complexity = O(nlogn) because it's capped by the sorting process.


"""


# Add any helper functions you may need here


def minOverallAwkwardness(arr):
  # Write your code here
  val = 0 
  arr = sorted(arr)
  for i in range(len(arr)-2):
    item1 = arr[i]
    item2 = arr[i+1]
    item3 = arr[i+2]
    new_val = max(abs(item1-item2),abs(item3-item2), abs(item3-item1))
    val = max(val,new_val)
  return val
    

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
  arr_1 = [5, 10, 6, 8]
  expected_1 = 4
  output_1 = minOverallAwkwardness(arr_1)
  check(expected_1, output_1)

  arr_2 = [1, 2, 5, 3, 7]
  expected_2 = 4
  output_2 = minOverallAwkwardness(arr_2)
  check(expected_2, output_2)
  