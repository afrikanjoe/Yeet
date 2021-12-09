"""
You are in charge of preparing a recently purchased lot for one of Amazon's new building. The lot is covered with trenches and has a single obstacle that needs to be taken
down before the foundation can be prepared for the building. The demolition robot must remove the obstacle before progress can be made on the building. 

Write an algorithm to determine the minimum distance required for the demolition to remove the obstacle. 
"""

class Solution: 

    # This was the implementation I did during the interview
    def distanceTraversed(self,lot):

        paths = []
        m = len(lot)
        n = len(lot[0])

        queue = [[(0,0,lot[0][0])]]
        while queue:
            curr_path = queue.pop(0)
            last_point = curr_path[-1]
            x,y,val = last_point
            if(val==9):
                paths.append(curr_path)
            else:
                dirs = [(0,1),(1,0),(-1,0),(0,-1)]
                for i in range(len(dirs)):
                    direction = dirs[i]
                    x_new = x+direction[0]
                    y_new = y+direction[1]
                    if(x_new>=0 and x_new<m and y_new>=0 and y_new<n):
                        new_val = lot[x_new][y_new]
                        new_path = curr_path[:]
                        if((x_new,y_new,new_val) not in new_path):
                            new_path = new_path + [(x_new,y_new,new_val)]
                            queue.append(new_path)
        min_len = 2**32
        for path in paths:
            min_len = min(len(path)-1,min_len)
        return min_len


if __name__ == "__main__":
    inp = [[1,0,0],[1,0,0],[1,9,1]]
    print(Solution().distanceTraversed(inp))