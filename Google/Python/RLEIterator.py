"""
We can use run-length encoding (i.e., RLE) to encode a sequence of integers. In a run-length encoded array of even length encoding (0-indexed), for all even i, 
encoding[i] tells us the number of times that the non-negative integer value encoding[i + 1] is repeated in the sequence.

For example, the sequence arr = [8,8,8,5,5] can be encoded to be encoding = [3,8,2,5]. encoding = [3,8,0,9,2,5] and encoding = [2,8,1,8,2,5] are also valid RLE of arr.
Given a run-length encoded array, design an iterator that iterates through it.

Implement the RLEIterator class:

RLEIterator(int[] encoded) Initializes the object with the encoded array encoded.
int next(int n) Exhausts the next n elements and returns the last element exhausted in this way. If there is no element left to exhaust, return -1 instead.


"""


class RLEIterator:

    def __init__(self, encoding):
        self.encoding_list = []
        self.value_list = []
        
        for i in range(0,len(encoding),2):
            if(encoding[i]>0):
                self.encoding_list.append(encoding[i])
                self.value_list.append(encoding[i+1])
            self.counter = 0 

        

    def next(self, n):
        burn = n
        while burn and self.encoding_list:
            encoding = self.encoding_list[0]
            value = self.value_list[0]
            if(encoding-burn>=0):
                self.encoding_list[0] = self.encoding_list[0]-burn
                return value
            else:
                burn = burn - self.encoding_list[0]
                self.encoding_list.pop(0)
                self.value_list.pop(0)
        return -1

if __name__ == "__main__":
    f_calls = ["RLEIterator","next","next","next","next"]
    encoding = [3,8,0,9,2,5]
    calls = [[2],[1],[1],[2]]
    answer = []
    obj = None
    count = 0 
    for s in f_calls:
        if(s == "RLEIterator"):
            obj = RLEIterator(encoding)
        else:
            answer.append(obj.next(calls[count][0]))
            count+=1
    print(answer)
