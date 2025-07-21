class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        last = len(digits) - 1
        while(last >= 0):
            if digits[last] != 9:
                digits[last] += 1
                break
            elif digits[last] == 9 and last == 0:
                digits[last] = 0
                digits.insert(0,1)
                break
            else:
                digits[last] = 0
            last -= 1

        return digits 

sol = Solution()
print(sol.plusOne([1,2,3]))     # Output: [1, 2, 4]
print(sol.plusOne([9,9,9]))     # Output: [1, 0, 0, 0]