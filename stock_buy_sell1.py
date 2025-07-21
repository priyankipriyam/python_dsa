class Solution:
    def max_profit(self, prices):
        max_profit = 0

        lp, rp = 0, 1

        while rp < len(prices):
            if prices[lp] < prices[rp]:
                max_profit = max(max_profit, prices[rp] - prices[lp])
                rp += 1
            else:
                lp = rp
                rp += 1

        return max_profit
        

sol = Solution()
print(sol.max_profit([7,1,5,3,6,4]))