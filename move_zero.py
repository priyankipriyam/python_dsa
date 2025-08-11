class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lp = 0
        rp = 1
        
        for rp in range(len(nums)):
            if (nums[lp] == 0 and nums[rp] != 0):
                nums[lp],nums[rp] = nums[rp], nums[lp]
                lp += 1
            elif (nums[lp] != 0 and nums[rp] != 0):
                lp += 1
            rp += 1
        return nums
        

# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         lp = 0
#         rp = 0
        
#         while rp < len(nums) and lp < len(nums):
#             if nums[rp] != 0:
#                 nums[lp] = nums[rp]
#                 lp += 1
#             rp += 1

#         while lp < len(nums):
#             nums[lp] = 0
#             lp += 1

#         return nums
    
sol = Solution()
print(sol.moveZeroes([0,1, 0, 3, 12, 0]))  # Output: [1, 3, 12, 0, 0]