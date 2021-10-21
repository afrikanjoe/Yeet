import heapq
# Add any extra import statements you may need here


"""
heapq methods 

heapq.nlargest return a list with the n largest elements
heapq.nsmallest return a list with n smallest elements

A heap or binary heap has O(log n) push, O(log n) pop 
"""

# Add any helper functions you may need here

# O(N^2 Log N)
def findMedianBF(arr):
  # Write your code here
  pq = []
  median_list = []
  for i in range(len(arr)):
    temp_arr = sorted(arr[0:i+1])
    if(len(temp_arr)%2==0):
      mid = int((len(temp_arr)-1)/2.0)
      mid1 = mid+1
      try:
        median = (temp_arr[mid] + temp_arr[mid1])/2
        median_list.append(int(median))
      except:
        print(temp_arr,mid,mid1) 
    else:
      mid = int((len(temp_arr)-1)/2.0)
      try:
        median_list.append(int(temp_arr[mid]))
      except:
        print(temp_arr,mid)
  return median_list


def findMedianTwoHeaps(arr):
  output = []
  minq = []
  maxq = []
  for i in range(len(arr)):
    heapq.heappush(maxq,-arr[i])
    val = - heapq.heappop(maxq)
    heapq.heappush(minq,val)
    
    while(len(minq)> len(maxq)+1):
      heapq.heappush(maxq,-heapq.heappop(minq))
      
    if(len(minq)==len(maxq)):
      output.append(int((minq[0]-maxq[0])/2.0))
    else:
      output.append(minq[0])
    
    
  return output


def findMedian(arr):

  output = []
  for i in range(1,len(arr)+1):

    # get the smallest elements from the subarray arr[0:i] this takes log(n) time 
    temp = heapq.nsmallest(i,arr[0:i])
    mid = (0 + len(temp)-1) >> 1
    if(len(temp)%2==0):
      mid1 = mid+1 
      val = (temp[mid] + temp[mid1]) >> 1
      output.append(val)
    else:
      output.append(temp[mid])
  return output

  


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [5, 15, 1, 3]
  expected_1 = [5, 10, 5, 4]
  output_1 = findMedian(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [2, 3, 4, 3, 4, 3]
  output_2 = findMedian(arr_2)
  check(expected_2, output_2)


  # Add your own test cases here
  