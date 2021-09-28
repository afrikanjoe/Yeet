"""
You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] 
means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.

"""
import heapq
class Solution:
    def getOrder(self, tasks):
        for i,c in enumerate(tasks):
            c.append(i)

        # this sorts them with respect to their enqueue time descending
        tasks.sort(reverse=True)
        available = []
        res = []

        print(tasks)

        # get the first task and the current time is the enque time
        currTime=tasks[-1][0]
        while tasks or available:
            if(tasks):
                print("main_loop",currTime,tasks[-1],available)
            # if the list of tasks is not empty and the current tasks start time is greater than 
            # the current time, and nothing is is in the available heap 
            # set the current time to this task 
            if tasks and tasks[-1][0]>currTime and not available:
                currTime=tasks[-1][0]

            # if the list of tasks is not empty and the most recent task is less than the current tasks
            if tasks and tasks[-1][0]<=currTime:
                # add the the index and task length to the avalable list
                while tasks and tasks[-1][0]<=currTime:
                    print("adding childs",currTime,tasks[-1],available)
                    heapq.heappush(available,(tasks[-1][1],tasks[-1][2]))
                    tasks.pop()

            # for all the tasks in the list 
            # get the most recent task append it to the results list 
            # increment the time and do that for all the available tasks
            if available:
                time,index=heapq.heappop(available)
                print("result adding",time,index)
                currTime+=time
                res.append(index)
            # print(currTime)
        return res


if __name__ == "__main__":
    inp = [[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]
    print(Solution().getOrder(inp))

    inp = [[1,2],[2,4],[3,2],[4,1]]
    print(Solution().getOrder(inp))
