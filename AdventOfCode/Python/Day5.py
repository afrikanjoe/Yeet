
import numpy as np
class Solution:

    def read_input(self,file_h):
        lines = []
        x_max = -100
        y_max = -100
        intervals = []
        lines = []
        for line in file_h:
            curr_line = line.replace(" -> ", ",")
            x1,y1,x2,y2 = curr_line.split(",")
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
            
            if(x1==x2 or y1==y2):

                interval = [[min(x1,x2),max(x1,x2)],[min(y1,y2),max(y1,y2)]]
                intervals.append(interval)
                x_max = max(x1,x2,x_max)
                y_max = max(y1,y2,y_max)
        board = np.zeros((x_max+1,y_max+1))
        for interval in intervals:

            for i in range(interval[0][0],interval[0][1]+1):
                for j in range(interval[1][0],interval[1][1]+1):
                    board[i][j] +=1

        indices = np.where(board>=2)[0]

        return len(indices)
            # print(line_split)
            # #lines.append()

    def read_input_part_two(self,file_h):
        lines = []
        x_max = -100
        y_max = -100
        intervals = []
        lines = []
        for line in file_h:
            curr_line = line.replace(" -> ", ",")
            x1,y1,x2,y2 = curr_line.split(",")
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
            
            if(x1==x2 or y1==y2):

                interval = [[min(x1,x2),max(x1,x2)],[min(y1,y2),max(y1,y2)]]
                intervals.append(interval)
                x_max = max(x1,x2,x_max)
                y_max = max(y1,y2,y_max)

            else:
                lines.append([x1,y1,x2,y2])
                #print(x1,y1,x2,y2)
        board = np.zeros((x_max+1,y_max+1))
        for interval in intervals:

            for i in range(interval[0][0],interval[0][1]+1):
                for j in range(interval[1][0],interval[1][1]+1):
                    board[i][j] +=1

        #indices = np.where(board>=2)[0]
        for line in lines:
            x_start = (line[0],line[1])
            x_end = (line[2],line[3])
            x_incr = 1
            y_incr = 1
            if(line[0]>line[2]):
                x_incr = -1
            if(line[1]>line[3]):
                y_incr = -1

            curr_point = x_start 
            while curr_point!=x_end:
                board[curr_point[0]][curr_point[1]]+=1
                curr_point = (curr_point[0]+x_incr,curr_point[1]+y_incr)
            board[curr_point[0]][curr_point[1]]+=1

        indices = np.where(board>=2)[0]
        return len(indices)





if __name__ == "__main__":
    with open("inputs/Day5.txt") as f:
        file_h =f.read().split("\n")
        print(Solution().read_input(file_h))
    with open("inputs/Day5.txt") as f:
        file_h =f.read().split("\n")
        print(Solution().read_input_part_two(file_h))