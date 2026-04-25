class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 0; 
        int best = 0; 
        while(right < prices.length){
            int profit = prices[right] - prices[left];
            if(profit < 0) left = right;
            best = Math.max(best, profit); 
            right += 1;  
        }
        return best; 
    }
}
