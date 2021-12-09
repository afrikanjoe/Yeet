"""

You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.
"""

class Solution:
    def reorderLogFiles(self, logs):
        
        word_logs = []
        digit_logs = []
        
        for log in logs:
            if(self.check_if_digit_log(log.split(" "))):
                digit_logs.append(log)
            else:
                val = " ".join(log.split(" ")[1:] + [""])
                word_log = tuple([val,log.split(" ")[0]])
                word_logs.append(word_log)
        
        word_logs = sorted(word_logs)
        
        word_logs = [ [i[-1]] + list(i[0:-1]) for i in word_logs]
        word_logs = [(" ".join(list(tup))).strip() for tup in word_logs]
        return word_logs + digit_logs
        
        
        
        
    def check_if_digit_log(self,log):
        
        for word in log[1:]:
            if not (word.isnumeric()):
                return False
        return True


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    print(Solution().reorderLogFiles(logs))