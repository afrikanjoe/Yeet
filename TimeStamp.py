"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and 
retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns ""



"""





class TimeMap:
    def __init__(self):
        self.values_dict = {}
        self.time_dict ={}
        

    def set(self, key, value, timestamp):
        v_dict = self.values_dict.get(key,0)
        t_dict = self.time_dict.get(key,0)
        if(v_dict):
            v_dict.append(value)
            self.values_dict[key] = v_dict
            t_dict.append(timestamp)
            self.time_dict[key] = t_dict
        else:
            self.values_dict[key] = [value]
            self.time_dict[key] = [timestamp]
        
    def get(self, key, timestamp):
        val = ""
        v_dict = self.values_dict.get(key,0)
        t_dict = self.time_dict.get(key,0)
        if(not v_dict):
            return val
        for i in range(len(v_dict)-1,-1,-1):
            if(t_dict[i]<=timestamp):
                val = v_dict[i]
                break
        return val
                
    


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


if __name__=="__main__":
    command_list = ["TimeMap","set","set","get","get","get","get","get"]
    command_args = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
    output_val = [None]
    tm = TimeMap()
    for i in range(1,len(command_list)):
        cm = command_list[i]
        carg = command_args[i]
        if(cm=="set"):
            tm.set(carg[0],carg[1],carg[2])
            output_val.append(None)
        else:
            output_val.append(tm.get(carg[0],carg[1]))
    print(output_val)
