import math

# O(n log n)
def are_they_equal_simple(array_a, array_b):
  # Write your code here
  return sorted(array_a)==sorted(array_b)  

# O(n)
def are_they_equal(array_a,array_b):

    array_dict_a = {}
    array_dict_b = {}

    if(len(array_a)!=len(array_b)):
        return False
    else:
        for i in range(len(array_a)):
            array_dict_a[array_a[i]] = array_dict_a.get(array_a[i],0)+1
            array_dict_b[array_b[i]] = array_dict_b.get(array_b[i],0)+1
        for item in array_a:

            item1 = array_dict_a.get(item,0)
            item2 = array_dict_b.get(item,0)
            if(item1!=item2):
                return False
    return True


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
  n_1 = 4
  a_1 = [1, 2, 3, 4]
  b_1 = [1, 4, 3, 2]
  expected_1 = True
  output_1 = are_they_equal(a_1, b_1)
  check(expected_1, output_1)

  n_2 = 4
  a_2 = [1, 2, 3, 4]
  b_2 = [1, 2, 3, 5]  
  expected_2 = False
  output_2 = are_they_equal(a_2, b_2)
  check(expected_2, output_2)

  # Add your own test cases here
  