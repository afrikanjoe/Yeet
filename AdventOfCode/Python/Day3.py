"""
The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. 
The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). 
The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. 
For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.
The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. 
So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.
"""

class Solution:

    def binary_diagnostic(self,file):
        return self.decode_string(file.split("\n"))



    def count_bits(self,arr):
        iter_length = len(list(arr[0]))
        count_dicts = []
        for i in range(iter_length):
            count_dicts.append({})

        for item in arr:
            item = list(item)
            for i in range(iter_length):
                val = int(item[i])
                index_count_dict = count_dicts[i]
                index_count_dict[val] = index_count_dict.get(val,0)+1
        return count_dicts



    def decode_string(self,arr):

        iter_length = len(list(arr[0]))
        count_dicts = []
        for i in range(iter_length):
            count_dicts.append({})

        for item in arr:
            item = list(item)
            for i in range(iter_length):
                val = int(item[i])
                index_count_dict = count_dicts[i]
                index_count_dict[val] = index_count_dict.get(val,0)+1
        
        gamma = ""
        epsilon = ""
        for i in range(iter_length):
            zero_count = count_dicts[i][0]
            one_count = count_dicts[i][1]
            if(zero_count>one_count):
                gamma = gamma + "0"
                epsilon = epsilon + "1"
            else:
                gamma = gamma + "1"
                epsilon = epsilon + "0"



        numbers = arr[:]
        temp = []
        index = 0 
        while len(numbers)>1 and index<iter_length:
            curr_dict = count_dicts[index]
            for item in numbers: 
                curr_item = list(item)
                if(curr_dict[1]>=curr_dict[0]):
                    if(curr_item[index]=="1"):
                        temp.append(item)
                else:
                    if(curr_item[index]=="0"):
                        temp.append(item)
            numbers = temp[:]
            count_dicts = self.count_bits(numbers)
            temp = []
            index+=1
        
        oxy = int(numbers[0],2)


        numbers = arr[:]
        count_dicts = self.count_bits(numbers)
        temp = []
        index = 0
        while len(numbers)>1 and index<iter_length:
            curr_dict = count_dicts[index]
            for item in numbers: 
                curr_item = list(item)
                if(curr_dict[1]>=curr_dict[0]):
                    if(curr_item[index]=="0"):
                        temp.append(item)
                else:
                    if(curr_item[index]=="1"):
                        temp.append(item)
            numbers = temp[:]
            count_dicts = self.count_bits(numbers)
            temp = []
            index+=1
        
        co2 = int(numbers[0],2)


        return int(gamma,2)* int(epsilon,2), oxy*co2



        




    #def decode_epsilon(self,arr):


if __name__ == "__main__":
    with open("inputs/Day3.txt") as f:
        content = f.read()
        print(Solution().binary_diagnostic(content))
