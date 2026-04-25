class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> mapping1 = new HashMap<>(); 
        HashMap<Character, Integer> mapping2 = new HashMap<>(); 
        for(int i = 0; i < s.length(); i++) mapping1.put(s.charAt(i), mapping1.getOrDefault(s.charAt(i), 0) + 1);
        for(int i = 0; i < t.length(); i++) mapping2.put(t.charAt(i), mapping2.getOrDefault(t.charAt(i), 0) + 1);
        if(mapping1.equals(mapping2)) return true; 
        else return false; 
    }
}
