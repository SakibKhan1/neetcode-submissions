class Solution {
    public int maxProfit(int[] prices) {
        int left = 0, right = 0; 
        int res = 0; 
        while(right < prices.length){
            int profit = prices[right] - prices[left];
            if(profit < 0){
                left = right; 
            }
            res = Math.max(res, profit);
            right += 1; 
        }

        return res; 
    }
}
