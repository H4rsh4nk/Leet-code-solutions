class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        pointer = 0
        while pointer <= len(s) - 1:
            temp = []
            t_pointer = pointer
            while t_pointer <= len(s) - 1:
                st = s[t_pointer]
                if st in temp:
                    ans = max(ans, len(temp))
                    pointer = pointer + temp.index(st)  
                    break
                else:
                    temp.append(st)
                t_pointer += 1
                ans = max(ans, len(temp))
            pointer += 1
                

        return ans