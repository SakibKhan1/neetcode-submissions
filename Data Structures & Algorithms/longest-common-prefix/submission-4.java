class Solution {
    public String longestCommonPrefix(String[] strs) {
        String shortest = strs[0];
        StringBuilder res = new StringBuilder("");
        for(String word: strs){
            if(word.length() < shortest.length()) shortest = word;
        }
        for(int i = 0; i < shortest.length(); i++){
            for(String word: strs){
                if(word.charAt(i) != shortest.charAt(i)) return res.toString(); 
            }
            res.append(shortest.charAt(i));
        }
        return res.toString();
    }
}