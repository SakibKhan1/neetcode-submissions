import java.util.*;

class Solution {
    public int lastStoneWeight(int[] stones) {

        // Create a max heap
        PriorityQueue<Integer> maxHeap =
                new PriorityQueue<>(Collections.reverseOrder());

        // Add all stones
        for (int stone : stones) {
            maxHeap.offer(stone);
        }

        // While more than one stone remains
        while (maxHeap.size() > 1) {

            int a = maxHeap.poll();   // largest
            int b = maxHeap.poll();   // second largest

            if (a != b) {
                maxHeap.offer(a - b);
            }
        }

        return maxHeap.isEmpty() ? 0 : maxHeap.peek();
    }
}
