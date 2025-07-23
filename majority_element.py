class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp = {}
        for i in range(len(nums)):
            ##hashmap code
            if nums[i] in mp:
                mp[nums[i]] += 1
            else:
                mp[nums[i]] = 1
            if mp[nums[i]] * 2 > len(nums):
                return nums[i]

        return -1
    
# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         return nums[len(nums) // 2]
    

sol = Solution()
print(sol.majorityElement([3, 2, 3]))  # Output: 3
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
print(sol.majorityElement([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: -1
