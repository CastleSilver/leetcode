class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        s = s.replaceAll(" ", "");
        s = s.replaceAll("[^a-z0-9]", "");
        int right = s.length() - 1;
        for(int left = 0; left < s.length() / 2; left++) {
            if(s.charAt(left) != s.charAt(right)) return false;
            right -= 1;
        }
        return true;
    }
}