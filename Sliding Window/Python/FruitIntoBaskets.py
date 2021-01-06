"""In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

    Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
    Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?"""

class Solution:
    @staticmethod
    def totalFruit(tree):
        maxi = 0
        vals = Solution.getindices(tree)
        for i in vals.keys():
            for index in vals[i]:
                val = Solution.collect(index,tree)
                if(len(val)>maxi):
                    maxi = len(val)
        return maxi 
    @staticmethod
    def getindices(tree):
        dicta= {}
        for i in range(len(tree)):
            val = dicta.get(tree[i],0)
            if val ==0:
                dicta[tree[i]] = [i]
            else:
                newls = val+[i]
                dicta[tree[i]] = newls
        return dicta

    @staticmethod
    def collect(index,tree):
        fruit= [tree[index]]
        for i in range(index+1,len(tree)):
            fruit2 = tree[i]
            if(len(list(set(fruit)))==1):
                fruit.append(fruit2)
            elif(fruit2 in fruit):
                fruit.append(fruit2)
            else:
                break
        return fruit



        
if __name__=='__main__':
    tree = [3,3,3,1,2,1,1,2,3,3,4]
    tree2 = [0,1,2,2]
    tree3 = [1,2,3,2,2]
    print(Solution.totalFruit(tree))
    print(Solution.totalFruit(tree2))
    print(Solution.totalFruit(tree3))