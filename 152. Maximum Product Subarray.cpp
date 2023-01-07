class Solution:
    def isSubsequence(self, s: str, t: str) -> bool: 
        for i in range(len(s)):
            # print(s[i])
            # print(t)
            # index = t.find(s[i])
            if s[i] in t:
                t = t[t.find(s[i]) + 1 :]
            else: 
                # print("False")
                return False
    
        return True
    # print("True")