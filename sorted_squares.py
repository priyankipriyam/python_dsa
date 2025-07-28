#O(nlogn) T.C/ O(1) S.C
# class Solution(object):
#     def sortedSquares(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         for i in range(len(nums)):
#             nums[i] = nums[i] * nums[i]

#         nums.sort()
#         return nums

#O(n) Time complexity. O(n) Space complexity           
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lp = 0
        rp = len(nums) - 1
        sorted_sq = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[lp]) > abs(nums[rp]):
                sorted_sq[i] = nums[lp] * nums[lp]
                lp += 1
            else:
                sorted_sq[i] = nums[rp] * nums[rp]
                rp -= 1
        return sorted_sq

            
sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))  # Output: [0, 1, 9, 16, 100]
