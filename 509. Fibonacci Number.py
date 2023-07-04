class Solution:
    def fib(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n - 2):
            temp = a
            a += b
            b = temp

        return a
