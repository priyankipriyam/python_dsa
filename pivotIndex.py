class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        runningSum = 0
        totalSum = 0
        for i in range(len(nums)):
            totalSum += nums[i]
        for i in range(len(nums)):
            if 2 * runningSum == (totalSum - nums[i]):
                return i
            runningSum += nums[i]
        return -1


sol = Solution()
print(sol.pivotIndex([1, 7, 3, 6, 5, 6]))  # Output: 3
print(sol.pivotIndex([1, 2, 3]))  # Output: -1
print(sol.pivotIndex([-1,-1,-1,-1,-1,-1]))