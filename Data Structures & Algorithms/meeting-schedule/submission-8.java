/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {
        int i = 1;
        Collections.sort(intervals, (a,b) -> a.start - b.start); 
        while(i < intervals.size()){
            if(intervals.get(i).start < intervals.get(i - 1).end){
                return false; 
            }
            i += 1; 
        }
        return true; 
    }
}
