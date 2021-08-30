"""
Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds 
(i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).
All messages will come in chronological order. Several messages may arrive at the same timestamp.
Implement the Logger class:
Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.
"""

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buffer = {}
        

    def shouldPrintMessage(self, timestamp, message) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        prev_stamp = self.buffer.get(message)
        if(not prev_stamp):
            self.buffer[message] = str(timestamp)
            return True
        else:
            if(timestamp-int(prev_stamp)>=10):
                self.buffer[message] = str(timestamp)
                return True
            else:
                return False

if __name__=="__main__":

    """Expected Answer: [null,true,true,true,false,false,false,false,false,false,false]"""
    test_case = [[],[0,"A"],[0,"B"],[0,"C"],[0,"A"],[0,"B"],[0,"C"],[0,"A"],[0,"B"],[0,"C"],[0,"A"]]
    ans_dict = []
    lg = Logger()
    for item in test_case:
        if(item):
            ans_dict.append(lg.shouldPrintMessage(item[0],item[1]))
        else:
            ans_dict.append(None)
    print(ans_dict)