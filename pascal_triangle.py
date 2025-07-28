class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr = [[1], [1,1]]
        if numRows == 1:
            return [[1]]
        
        for i in range(2, numRows):
            newArr = []
            for j in range(i+1):
                if j == 0 or j == i:
                    newArr.append(1)
                else:
                    el = arr[i-1][j-1] + arr[i-1][j]
                    newArr.append(el)
            arr.append(newArr)

        return arr
        

# Example usage:
sol = Solution()        
#print(sol.generate(5))  # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
tree = sol.generate(5)
for row in tree:
    print(row)  # Output each row of Pascal's Triangle  