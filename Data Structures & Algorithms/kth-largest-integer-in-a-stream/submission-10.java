class KthLargest {
    public PriorityQueue<Integer> minheap;
    public int k;
    
    public KthLargest(int k, int[] nums) {
        this.k = k; 
        this.minheap = new PriorityQueue<>();
        for(int i = 0; i < nums.length;i++){
            minheap.offer(nums[i]);
        }
        while(minheap.size() > k){
            minheap.poll();
        }
    }
    
    public int add(int val) {
        minheap.add(val); 
        while(minheap.size() > k){
            minheap.poll();
        } 
        return minheap.peek(); 
    }
}
