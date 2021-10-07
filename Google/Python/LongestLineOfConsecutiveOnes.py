class Solution:
    def longestLine(self, mat):
        
        m=len(mat)
        n = len(mat[0])
        queue = []
        max_len = 0 
        for i in range(m):
            for j in range(n):
                if(mat[i][j]):
                    queue.append([(i,j)])
                    
        while queue:
            item_list = queue.pop(0)
            max_len = max(max_len,len(item_list))
            if(len(item_list)==1):
                self.consider_neighbors(item_list,m,n,queue,mat)
            else:
                self.add_neighbor(item_list,m,n,queue,mat)
        return max_len

        
    def consider_neighbors(self,item,m,n,queue,mat):
        item_tup = item[0]
        i,j = item_tup[0],item_tup[1]
        
        if(i-1>=0): # above
            if(mat[i-1][j]):
                item_list  = item[:]
                item_list.append((i-1,j))
                queue.append(item_list)
                
        if(i+1<m):  # below
            if(mat[i+1][j]):
                item_list  = item[:]
                item_list.append((i+1,j))
                queue.append(item_list)
                
        if(i-1>=0 and j-1>=0): # top left
            if(mat[i-1][j-1]):
                item_list  = item[:]
                item_list.append((i-1,j-1))
                queue.append(item_list)
                
        if(i-1>=0 and j+1<n): # top right
            if(mat[i-1][j+1]):
                item_list  = item[:]
                item_list.append((i-1,j+1))
                queue.append(item_list)
                
        if(j-1>=0): # to the left
            if(mat[i][j-1]):
                item_list  = item[:]
                item_list.append((i,j-1))
                queue.append(item_list)
                
        if(j+1<n): # to the right
            if(mat[i][j+1]):
                item_list  = item[:]
                item_list.append((i,j+1))
                queue.append(item_list)
                
        if(j+1<n and i+1<m): # botom right
            if(mat[i+1][j+1]):
                item_list  = item[:]
                item_list.append((i+1,j+1))
                queue.append(item_list)
                
        if(j-1>=0 and i+1<m): # botom left
            if(mat[i+1][j-1]):
                item_list  = item[:]
                item_list.append((i+1,j-1))
                queue.append(item_list)

    def add_neighbor(self,item,m,n,queue,mat):
        item_tup = item[-2]
        item_tup2 = item[-1]
        i,j = item_tup[0],item_tup[1]
        i2, j2 = item_tup2[0],item_tup2[1]

        if(i==i2 and j2>j): # right
            if(j2+1<n): # to the right
                if(mat[i2][j2+1]):
                    item_list  = item[:]
                    if((i2,j2+1) not in item_list):
                        item_list.append((i2,j2+1))
                        queue.append(item_list)
        elif(i==i2 and j2<j): # left
            if(j2-1>=0):
                if(mat[i2][j2-1]):
                    item_list  = item[:]
                    if((i2,j2-1) not in item_list):
                        item_list.append((i2,j2-1))
                        queue.append(item_list)
        elif(i<i2 and j==j2): # below
            if(i2+1<m):
                if(mat[i2+1][j2]):
                    item_list  = item[:]
                    if((i2+1,j2) not in item_list):
                        item_list.append((i2+1,j2))
                        queue.append(item_list)
        elif(i>i2 and j==j2): # above
            if(i2-1>=0):
                if(mat[i2-1][j2]):
                    item_list  = item[:]
                    if((i2-1,j2) not in item_list):
                        item_list.append((i2-1,j2))
                        queue.append(item_list)

        elif(i<i2 and j<j2):  # bottom right
            if(i2+1<m and j2+1<n):
                if(mat[i2+1][j2+1]):
                    item_list  = item[:]
                    if((i2+1,j2+1) not in item_list):
                        item_list.append((i2+1,j2+1))
                        queue.append(item_list)
        elif(i>i2 and j>j2):  # top left
            if(i2-1>=0 and j2-1>=0): # top left
                if(mat[i2-1][j2-1]):
                    item_list  = item[:]
                    if((i2-1,j2-1) not in item_list):
                        item_list.append((i2-1,j2-1))
                        queue.append(item_list)
        elif(i<i2 and j<j2):  # top right
            if(i2-1>=0 and j2+1<n): 
                if(mat[i2-1][j2+1]):
                    item_list  = item[:]
                    if((i2-1,j2+1) not in item_list):
                        item_list.append((i2-1,j2+1))
                        queue.append(item_list)
        elif(i>i2 and j2<j):  # bottom left
            if(j2-1>=0 and i2+1<m): # botom left
                if(mat[i2+1][j2-1]):
                    item_list  = item[:]
                    if((i2+1,j2-1) not in item_list):
                        item_list.append((i2+1,j2-1))
                        queue.append(item_list)





        

            
if __name__== "__main__":
    mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
    print(Solution().longestLine(mat))

    mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
    print(Solution().longestLine(mat))

                
        