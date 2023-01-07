class Solution:
    def isValid(self, s: str) -> bool:
                
        dic = {")":"(", "]":"[", "}":"{"}

        stack = []
        # print(s[-2])

        for i in range(len(s)):
            
            # print(stack)
            if s[i] not in dic.keys():
                stack.append(s[i])
            else: 
                if len(stack) == 0:
                    return False
                if stack[-1] == dic[s[i]]:
                    stack.pop()
                else:
                    print("False")
                    return False
                    break

        if len(stack) == 0:
            print("True")
            return True
        else:
            print("False")
            return False