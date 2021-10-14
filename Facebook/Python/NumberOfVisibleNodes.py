"""

There is a binary tree with N nodes. You are viewing the tree from its left side and can see only the leftmost nodes at each level. Return the number of visible nodes.
Note: You can see only the leftmost nodes, but that doesn't mean they have to be left nodes. The leftmost node at a level could be a right node.

"""

class TreeNode: 
  def __init__(self,key): 
    self.left = None
    self.right = None
    self.val = key 


def visible_nodes(root):
  # Write your code here
  left_max = left_dfs(root)
  queue = [(root,1)]
  max_left = 1
  while queue:
    node_tup = queue.pop()
    node = node_tup[0]
    depth = node_tup[1]
    if(node.left):
      max_left = max(max_left,depth+1)
      queue.append((node.left,depth+1))
    if(node.right):
      queue.append((node.right,depth+1))
      max_left = max(max_left,depth+1)
  return max(left_max,max_left)
  
def left_dfs(root):
  if(not root):
    return 0
  depth = 1
  queue = [root]
  while queue:
    node = queue.pop()
    if(node.left):
      queue.append(node.left)
      depth+=1
  return depth
    

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
  root_1 = TreeNode(8)
  root_1.left = TreeNode(3)
  root_1.right = TreeNode(10)
  root_1.left.left = TreeNode(1)
  root_1.left.right = TreeNode(6)
  root_1.left.right.left = TreeNode(4)
  root_1.left.right.right = TreeNode(7)
  root_1.right.right = TreeNode(14)
  root_1.right.right.left = TreeNode(13)
  expected_1 = 4
  output_1 = visible_nodes(root_1)
  check(expected_1, output_1)

  root_2 = TreeNode(10)
  root_2.left = TreeNode(8)
  root_2.right = TreeNode(15)
  root_2.left.left = TreeNode(4)
  root_2.left.left.right = TreeNode(5)
  root_2.left.left.right.right = TreeNode(6)
  root_2.right.left =TreeNode(14)
  root_2.right.right = TreeNode(16)

  expected_2 = 5
  output_2 = visible_nodes(root_2)
  check(expected_2, output_2)
