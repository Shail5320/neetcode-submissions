class Solution:
    def hammingWeight(self, n: int) -> int:
        ct = 0
        for i in range(32):
            if n & 1<<i:
                ct+=1
        return ct