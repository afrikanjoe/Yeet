"""
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. 
It clears up all the forward history.
string back(int steps) Move steps back in history. 
If you can only return x steps in the history and steps > x, you will return only x steps. 
Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. 
If you can only forward x steps in the history and steps > x, you will forward only x steps. 
Return the current url after forwarding in history at most steps.
"""

class BrowserHistory:

    def __init__(self, homepage):
        
        self.history = [homepage]
        self.curr_index = 0
        

    def visit(self, url):
         
        self.history = self.history[:self.curr_index+1]
            
        self.history.append(url)
        self.curr_index = len(self.history)-1
            
        

    def back(self, steps):
        self.curr_index = max(self.curr_index - steps,0)
        return self.history[self.curr_index]
        

    def forward(self, steps):
        self.curr_index = min(self.curr_index + steps,len(self.history)-1)
        return self.history[self.curr_index]
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
if __name__ == "__main__":
    function_calls = ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
    url = [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
    ans = [None]

    bh = BrowserHistory(url[0][0])
    for i in range(1,len(function_calls)):
        call = function_calls[i]
        if(call=="visit"):
            ans.append(bh.visit(url[i][0]))
        elif(call=="back"):
            ans.append(bh.back(url[i][0]))
        else:
            ans.append(bh.forward(url[i][0]))
    print(ans)
