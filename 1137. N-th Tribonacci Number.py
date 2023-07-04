class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        a, b, c = 0, 1, 1

        for i in range(n-2):
            print(a, b, c)
            temp = a + b + c
            a = b
            b = c
            c = temp
        return c    
