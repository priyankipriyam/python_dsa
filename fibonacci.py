# class Solution(object):
#     def fib(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
        
#         return self.fib(n-1) + self.fib(n-2)
        

# class Solution(object):
#     def fib(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         # [0, 1, 1, 2, 3, 5, 8]
#         arr = [0,1]
#         for i in range(2,n+1):
#             num = arr[i-1] + arr[i-2]
#             arr.append(num)
#         return arr[n]

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def helper(n):
            if n == 0 or n == 1: return n
            if n in memo: return memo[n]
            memo[n] = helper(n - 1) + helper(n - 2)
            print('memo:', memo)
            return memo[n]
        return helper(n)
    
sol = Solution()
print(sol.fib(6))  # 832040