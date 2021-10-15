"""

Change in a Foreign Currency
You likely know that different currencies have coins and bills of different denominations. In some currencies, it's actually impossible to receive change for a given amount of money. 
For example, Canada has given up the 1-cent penny. If you're owed 94 cents in Canada, a shopkeeper will graciously supply you with 95 cents instead since there exists a 5-cent coin.
Given a list of the available denominations, determine if it's possible to receive exact change for an amount of money targetMoney. 
Both the denominations and target amount will be given in generic units of that currency.
Signature
boolean canGetExactChange(int targetMoney, int[] denominations)
Input
1 ≤ |denominations| ≤ 100
1 ≤ denominations[i] ≤ 10,000
1 ≤ targetMoney ≤ 1,000,000
Output
Return true if it's possible to receive exactly targetMoney given the available denominations, and false if not.
Example 1
denominations = [5, 10, 25, 100, 200]
targetMoney = 94
output = false

"""

def canGetExactChange(targetMoney, denominations):
  # Write your code here
  if(len(denominations)==0 and targetMoney>0):
    return False
  elif(len(denominations)==0 and targetMoney==0):
    return True
  else:
    return canGetExactChange(targetMoney%denominations[-1],denominations[:-1])
  
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
  target_1 = 94
  arr_1 = [5, 10, 25, 100, 200]
  expected_1 = False
  output_1 = canGetExactChange(target_1, arr_1)
  check(expected_1, output_1)

  target_2 = 75
  arr_2 = [4, 17, 29]
  expected_2 = True
  output_2 = canGetExactChange(target_2, arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  