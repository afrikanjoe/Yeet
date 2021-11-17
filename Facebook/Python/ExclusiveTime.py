"""

On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.
Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, 
its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. 
Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.
You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". 
For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" 
means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.
A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, 
one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.
Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i
"""

class Solution:
    def exclusiveTime(self, n, logs):
        
        stack = [] 
        value_dict = {}
        curr_time=0 
        for log in logs:
            log_list = log.split(":")
            if(log_list[1]=="start"):
                stack.append((int(log_list[0]),int(log_list[2])))
                if(len(stack)>1):
                    prev = stack[-2]
                    value_dict[prev[0]] = value_dict.get(prev[0],0) + (int(log_list[2]) - prev[1])
                    
            else:
                top_val = stack.pop()
                value_dict[top_val[0]] = value_dict.get(top_val[0],0) + (int(log_list[2]) - top_val[1])+1
                if(len(stack)>0):
                    pre_val = stack.pop()
                    new_val = (pre_val[0],int(log_list[2])+1)
                    stack.append(new_val)
                
                
        output = []
        for i in sorted(list(value_dict.keys())):
            output.append(value_dict[i])
        return output

if __name__ == "__main__":
    n = 2
    logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
    print(Solution().exclusiveTime(n,logs))