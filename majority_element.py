class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = len(nums)/2
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        
            if hashmap[nums[i]] > majority:
                    return nums[i]
            
        return -1

        
        # mp = {}
        # for i in range(len(nums)):
        #     ##hashmap code
        #     if nums[i] in mp:
        #         mp[nums[i]] += 1
        #     else:
        #         mp[nums[i]] = 1
        #     if mp[nums[i]] * 2 > len(nums):
        #         return nums[i]

        # return -1
    

#Boyer-Moore Algorithm

        # count = 0
        # candidate = None

        # for num in nums:
        #     if count == 0:
        #         candidate = num

        #     if num == candidate:
        #         count += 1
        #     else:
        #         count -= 1
        # return candidate
    
# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
# this solution is not optimal as it has O(nlogn) time complexity due to sorting, and O(n) space complexity while the Boyer-Moore algorithm has O(n) time complexity and O(1) space complexity.
#         nums.sort()
#         return nums[len(nums) // 2]
    

sol = Solution()
print(sol.majorityElement([3, 2, 3]))  # Output: 3
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
print(sol.majorityElement([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: -1 (Boyer-Moore fails here as this array does not have a majority element)
