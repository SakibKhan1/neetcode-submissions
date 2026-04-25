class Solution {
public boolean isAlphaNum(char letter) {
    return ('A' <= letter && letter <= 'Z') ||
           ('a' <= letter && letter <= 'z') ||
           ('0' <= letter && letter <= '9');
}
    public boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right){
            if (isAlphaNum(s.charAt(left)) == false) left += 1; 
            else if (isAlphaNum(s.charAt(right)) == false) right -= 1; 
            else{
                if (Character.toLowerCase(s.charAt(left)) == Character.toLowerCase(s.charAt(right))){
                    left += 1;
                    right -= 1;
                }
                else{
                    return false; 
                }
            }
        }
        return true; 
    }
}
