class Solution:
    @staticmethod
    def isAnagram(s, t):
        return sorted(list(s))==sorted(list(t))


if __name__=="__main__":
    s1 = "anagram"
    s2 = "nagaram"
    print(Solution.isAnagram(s1,s2))