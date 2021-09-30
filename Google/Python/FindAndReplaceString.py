""""
You are given a 0-indexed string s that you must perform k replacement operations on. 
The replacement operations are given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.

To complete the ith replacement operation:

Check if the substring sources[i] occurs at index indices[i] in the original string s.
If it does not occur, do nothing.
Otherwise if it does occur, replace that substring with targets[i].
For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this replacement will be "eeecd".

All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will not overlap.

For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not be generated because the "ab" and "bc" replacements overlap.
Return the resulting string after performing all replacement operations on s.

A substring is a contiguous sequence of characters in a string.


"""




class Solution:
    def findReplaceStringWrong(self, s, indices, sources, targets):
        
        sources.sort(key=dict(zip(sources, indices)).get)
        targets.sort(key=dict(zip(targets, indices)).get)
        indices.sort()

        print(indices)
        print(sources)
        print(targets)
        replacements =[]
        for i in range(len(indices)-1):
            index1 = indices[i]
            index1_end = index1 + len(sources[i]) -1
            index2 = indices[i+1]
            index2_end = index2 + len(sources[i+1]) -1
            
            if(index1_end < index2):
                if(sources[i] == s[index1:index1_end+1]):
                    replacements.append(i)
                if(sources[i+1]==s[index2:index2_end+1]):
                    replacements.append(i+1)
            else:
                print("Collision")
                if(sources[i] == s[index1:index1_end+1] and sources[i+1]!=s[index2:index2_end+1]):
                    replacements.append(i)
                elif(sources[i] != s[index1:index1_end+1] and sources[i+1]==s[index2:index2_end+1]):
                    replacements.append(i+1)
                
        replacements = list(set(replacements))
        index_counter=0
        for i in range(len(replacements)):
            index = indices[replacements[i]]+index_counter
            s = s[0:index] + targets[replacements[i]] + s[index+len(sources[replacements[i]]):]
            index_counter=index_counter +(len(targets[replacements[i]])-len(sources[replacements[i]]))
        return s

    def findReplaceString(self, s, indices, sources, targets):
        new_s = {}
        for idx in range(len(indices)):
            start_idx = indices[idx]
            end_idx = start_idx + len(sources[idx])
            if s[start_idx:end_idx] == sources[idx]:
                new_s[indices[idx]] = (end_idx, targets[idx])
        print(new_s)
        idx = 0
        answer = ""
        while idx < len(s):
            if idx in new_s:
                answer += new_s[idx][1]
                idx = new_s[idx][0]
                continue
            else:
                answer += s[idx]
                idx += 1
        return answer


if __name__ == "__main__":
    s = "emgzpmdoogscklvhtgmethuiscljkdoqewgvbulemuxgtrkgxy"
    indices = [33,42,9,16,40,2,5,22,0,37,29,11,18,7,47,44]
    sources=["wg","xg","gs","tg","mu","gzp","md","uisc","em","ule","doqe","cklvh","meth","oo","gxy","tr"]
    targets =["v","g","vh","b","o","anjn","npm","fro","vqu","nuv","qam","kdfldd","ilak","wy","pn","kl"]
    print(Solution().findReplaceString(s,indices,sources,targets))
    s = "imidcxiiqjwpvvcocjtskshvmqjnlhsqtezqttmoxuskbmujej"
    indices = [35,6,22,40,17,19,12,2,42,4,8,45,14,29,47,24]
    sources = ["qtt","ii","hv","xu","jt","sk","vv","id","skb","cx","qjw","mu","co","hsqtez","jej","mqjnl"]
    targets = ["idl","vo","yl","pg","efp","vqi","s","wb","mw","gmt","rkqc","kdx","o","vamwgpn","pl","xyvz"]
    print(Solution().findReplaceString(s,indices,sources,targets))

    s= "mhnbzxkwzxtaanmhtoirxheyanoplbvjrovzudznmetkkxrdmr"
    indices = [46,29,2,44,31,26,42,9,38,23,36,12,16,7,33,18]
    sources = ["rym","kv","nbzxu","vx","js","tp","tc","jta","zqm","ya","uz","avm","tz","wn","yv","ird"]
    targets = ["gfhc","uq","dntkw","wql","s","dmp","jqi","fp","hs","aqz","ix","jag","n","l","y","zww"]
    print(Solution().findReplaceString(s,indices,sources,targets))