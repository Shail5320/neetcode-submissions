class Solution:
    def hammingWeight(self, n: int) -> int:
        # Brian Kernighan’s Algorithm
        ct = 0
        while n:
            n &= (n-1)
            ct += 1
        return ct