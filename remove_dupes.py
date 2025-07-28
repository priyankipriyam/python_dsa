# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         lp = 0
#         wp = 1
#         rp = 1
#         while(lp < rp and rp < len(nums)):
#             if nums[lp] == nums[rp]:
#                 rp += 1
#             elif nums[lp] < nums[rp]:
#                 nums[wp], nums[rp] = nums[rp], nums[wp]
#                 wp += 1
#                 rp += 1
#                 lp += 1
#         return lp + 1
#         # return nums
            
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lp = 0
        rp = 1
        while rp < len(nums):
            if nums[rp] != nums[lp]:
                lp += 1
                nums[lp] = nums[rp]

            rp += 1
        return lp+1, nums[0:lp + 1]
    


# Example usage:
sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # Output: (5, [0, 1, 2, 3, 4])
