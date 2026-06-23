class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l = i+1
            r = len(numbers)-1
            mains = target - numbers[i]
            while l<=r:
                mid = (l+r)//2
                if numbers[mid]==mains:
                    return [i+1, mid+1]
                elif numbers[mid]>mains:
                    r = mid-1
                else:
                    l = mid+1


    