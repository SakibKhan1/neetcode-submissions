import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count how many of each task we have
        count = Counter(tasks)
        
        # We use a max heap, so store negative counts
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque()  # to keep track of tasks in cooldown: (ready_time, count)
        
        # While there are tasks still in heap or waiting to cool down
        while maxHeap or q:
            time += 1

            if maxHeap:
                # Pop the most frequent task
                cnt = 1 + heapq.heappop(maxHeap)  # add 1 since stored as negative
                if cnt != 0:
                    # Push to cooldown queue: (ready_time, remaining count)
                    q.append((time + n, cnt))
            
            # If cooldown has expired for a task, push back to heap
            if q and q[0][0] == time:
                heapq.heappush(maxHeap, q.popleft()[1])
        
        return time
