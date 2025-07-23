class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        crs = 0
        numsRs = []
        for i in range(len(nums)):
            crs = crs + nums[i]
            numsRs.append(crs)
        return numsRs

        # for i in range(1, len(nums)):
        #     nums[i] += nums[i-1]
        # return nums

sol = Solution()
print(sol.runningSum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]