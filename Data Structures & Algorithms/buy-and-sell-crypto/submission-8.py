class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 0 
        res = 0 
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right 
            res = max(res, prices[right] - prices[left])
            right += 1 
        return res 