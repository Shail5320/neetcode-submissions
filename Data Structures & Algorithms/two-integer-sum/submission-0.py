class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set()
        n = len(nums)
        for i in range(n):
            rem = target - nums[i]
            if rem in s:
                return [min(i, nums.index(rem)), max(i, nums.index(rem))]
            else:
                s.add(nums[i])