class KthLargest {
    private int k;
    private PriorityQueue<Integer> minHeap;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.minHeap = new PriorityQueue<>();

        // Equivalent to Python heapify step
        for (int num : nums) {
            minHeap.offer(num);
        }

        // Equivalent to shrinking heap to size k
        while (minHeap.size() > k) {
            minHeap.poll();
        }
    }

    public int add(int val) {
        minHeap.offer(val);

        while (minHeap.size() > k) {
            minHeap.poll();
        }

        return minHeap.peek();
    }
}
