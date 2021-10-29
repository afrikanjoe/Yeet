"""
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
"""

class SnapshotArray:

    def __init__(self, length: int):
        
        self.arr = {}
        self.snap_id = 0 
        self.snap_arr = []
        

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val
        

    def snap(self) -> int:
        self.snap_id+=1
        self.snap_arr.append(dict(self.arr))
        return self.snap_id-1
        

    def get(self, index: int, snap_id: int) -> int:
        if(len(self.snap_arr[snap_id])>0 and index in self.snap_arr[snap_id].keys()):
            return self.snap_arr[snap_id][index]
        else:
            return 0 


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


if __name__ == "__main__":
    inp  = ["SnapshotArray","set","snap","snap","get","get","snap","snap"]
    vals = [[2],[0,12],[],[],[1,0],[1,0],[],[]]
    ss = None
    output = []
    for i in range(len(inp)):
        if(inp[i]=="SnapshotArray"):
            ss = SnapshotArray(vals[i][0])
            output.append(None)
        elif(inp[i]=="set"):
            ss.set(vals[i][0],vals[i][1])
            output.append(None)
        elif(inp[i]=="snap"):
            output.append(ss.snap())
        else:
            output.append(ss.get(vals[i][0],vals[i][1]))
    print(output)