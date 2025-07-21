# class Solution:
#     def two_sum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []

class Solution:
    def two_sum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            potentialMatch = target - nums[i]
            if potentialMatch in hashmap and hashmap[potentialMatch] != i:
                return [i, hashmap[potentialMatch]]
        return []

sol = Solution()
print(sol.two_sum([2, 7, 11, 15], 9))