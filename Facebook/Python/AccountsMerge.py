"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails 
representing emails of the account. Now, we would like to merge these accounts. 
Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, 
they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. 
The accounts themselves can be returned in any order.
"""

class Solution:
    def __init__(self):
        self.visited = []
    def accountsMerge(self, accounts):
        
        adj_dictionary = {}
        name_dictionary = {}
        return_list = []
        
        for acc in accounts:
            acc_name = acc[0]
            emails = acc[1:]
            first_email = emails[0]
            name_dictionary[first_email] = acc_name
            for email in emails[1:]:
                name_dictionary[email] = acc_name
                # connect this email to first email in the list
                connections = adj_dictionary.get(email,[])
                if(len(connections)==0):
                    adj_dictionary[email] = [first_email]
                else:
                    if(first_email not in connections):
                        connections.append(first_email)
                        adj_dictionary[email] = connections
                        
                # connect first email to this email
                connections = adj_dictionary.get(first_email,[])
                if(len(connections)==0):
                    adj_dictionary[first_email] = [email]
                else:
                    if(email not in connections):
                        connections.append(email)
                        adj_dictionary[first_email] = connections
                        
        email_candidates = list(name_dictionary.keys())
        
        for email_c in email_candidates: 
            merged = self.dfs(email_c, adj_dictionary)
            if(len(merged)>0):
                return_list.append([name_dictionary[email_c]] + merged)
        return return_list
        
       
    def dfs(self,email,adj_matrix):
        if(email in self.visited):
            return []
        else:
            visited = []
            queue = [email]
            while queue: 
                em = queue.pop()
                if(em in visited):
                    continue
                visited.append(em)
                neighbors = adj_matrix.get(em,[])
                for i in neighbors: 
                    if(i not in visited):
                        queue.append(i)
            self.visited = self.visited + visited
            return sorted(visited)
                            
if __name__ == "__main__":
    inp = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
    print(Solution().accountsMerge(inp))