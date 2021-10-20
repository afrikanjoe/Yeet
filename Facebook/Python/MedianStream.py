import heapq
# Add any extra import statements you may need here


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


def findMedian(arr):
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
  




def median_stream(a) -> list:
    res = []
    from queue import PriorityQueue
    mins = PriorityQueue()                  # larger element
    maxs = PriorityQueue()                  # smaller elements
    for i in range(len(a)):
        maxs.put(-a[i])
        x = -maxs.get()
        mins.put(x)
        if maxs.qsize() < mins.qsize():
            x = mins.get()
            maxs.put(x)
        
        if maxs.qsize() > mins.qsize():
            res.append(-maxs.get())
        else:
            res.append( int((-maxs.queue[0] + mins.queue[0])/2 + 0.499999) )
    return res



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
  