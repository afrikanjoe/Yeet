import math
# Add any extra import statements you may need here


# Add any helper functions you may need here




# Bubble sort type of thing is waaaay more efficient but ok 
def minOperationsBubble(arr):
  # Write your code here
  decreasing = False
  count = 0
  while not decreasing:
    decreasing=True
    for i in range(len(arr)-1,0,-1):
      if(arr[i]>arr[i-1]):
        decreasing=False
        swap(arr,i,i-1)
    count+=1
  return count
        
  
  
  
def swap(arr,i,j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
  
  

def minOperations(arr):
    solutions = []
    sol = sorted(arr)
    queue = [[arr]]
    while queue:
        current_attempt_list = queue.pop(0)
        if current_attempt_list[-1] == sol:
            solutions.append(current_attempt_list)
            break
        else:
            #add all the permuations to the queue.
            for i in range(2,len(arr)+1):
                for j in range(0,len(arr)-i+1):
                    new_list = current_attempt_list[:]
                    perm = current_attempt_list[-1][0:j] + current_attempt_list[-1][j:j+i][::-1] + current_attempt_list[-1][j+i:]
                    if(perm not in new_list):
                        new_list.append(perm)
                        queue.append(new_list)
            #print(queue)
            #print("")
    
    return len(solutions[0])-1
      

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
  n_1 = 5
  arr_1 = [1, 2, 5, 4, 3]
  expected_1 = 1
  output_1 = minOperations(arr_1)
  check(expected_1, output_1)

  n_2 = 3
  arr_2 = [3, 1, 2]
  expected_2 = 2
  output_2 = minOperations(arr_2)
  check(expected_2, output_2)
  
  