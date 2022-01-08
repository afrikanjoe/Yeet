
class Solution:
    def cherryPickup(self, grid):
        maxa = -2**32
        if(not grid):
            return 0 
        queue1 = [  [ [[0,0,grid[0][0]]],[[0,len(grid[0])-1,grid[0][-1]]]] ]
        m = len(grid)
        n = len(grid[0])
        
        while queue1:
            
            paths = queue1.pop()
            rob1_path  = paths[0]
            rob2_path  = paths[1]
            
            # rob1
            
            added = False
            for i in range(-1,2):
                last_point= [rob1_path[-1][0]+1,rob1_path[-1][1]+i]
                for j in range(-1,2):
                    last_point2 = [rob2_path[-1][0]+1,rob2_path[-1][1]+j]
                    
                    if(last_point[0]<m and last_point[1]>=0 and last_point[1]<n  and last_point2[0]<m and last_point2[1]>=0 and last_point2[1]<n ):
                        added = True
                        if(last_point==last_point2):

                            new_path = rob1_path[:] + [last_point+[rob1_path[-1][2]+grid[last_point[0]][last_point[1]]]]
                            new_path1 = rob1_path[:] + [last_point+[rob1_path[-1][2]+0]]

                            new_path2 = rob2_path[:] + [last_point2+[rob2_path[-1][2]+grid[last_point2[0]][last_point2[1]]]]
                            new_path3 = rob2_path[:] + [last_point2+[rob2_path[-1][2]+0]]
                            
                            
                            p1 = [new_path,new_path3]
                            p2 = [new_path1,new_path2]
                            queue1.append(p1)
                            queue1.append(p2)
                        else:
                            
                            new_path = rob1_path[:] + [last_point+[rob1_path[-1][2]+grid[last_point[0]][last_point[1]]]]
                            new_path2 = rob2_path[:] + [last_point2+[rob2_path[-1][2]+grid[last_point2[0]][last_point2[1]]]]
                            queue1.append([new_path,new_path2])
            if(not added):
                maxa = max(maxa,paths[1][-1][2]+paths[0][-1][2])
        return maxa
