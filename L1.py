class Solution(object):
    def twoSum(self, nums, target):
        nums=[2,7,11,15]
        target=9
        for i in range(3):
            if nums[i]+nums[i+1]==target:
                print([i,i+1])
solution=Solution()
solution.twoSum([2,7,11,15], 9)