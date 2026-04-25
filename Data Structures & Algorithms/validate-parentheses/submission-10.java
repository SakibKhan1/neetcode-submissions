class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> mapping = new HashMap<>(); 
        ArrayList<Character> stk = new ArrayList<>(); 
        mapping.put(')', '(');
        mapping.put('}', '{');
        mapping.put(']', '[');
        for(int i = 0; i < s.length(); i++){
            if(mapping.containsKey(s.charAt(i))){
                if(!stk.isEmpty() && stk.get(stk.size() - 1) == mapping.get(s.charAt(i))){
                    stk.remove(stk.size() - 1);
                }else{
                    return false;
                }
            }else{
                stk.add(s.charAt(i));
            }
        }
        if(stk.isEmpty()){
            return true;
        }else{
            return false; 
        }  
    }
}
