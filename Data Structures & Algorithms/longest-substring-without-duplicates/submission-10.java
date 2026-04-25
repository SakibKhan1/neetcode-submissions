class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0, right = 0;
        int res = Integer.MIN_VALUE; 
        HashSet<Character> visited = new HashSet<>(); 
        while (right < s.length()){
            while (visited.contains(s.charAt(right))){
                visited.remove(s.charAt(left));
                left += 1; 
            }
            visited.add(s.charAt(right));
            res = Math.max(res, right - left + 1); 
            right += 1; 
        }
        

        if(s.length() == 0){
            return 0;
        }else{
        return res;
        } 
    }
 
}
