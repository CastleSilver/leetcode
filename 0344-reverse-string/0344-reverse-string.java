class Solution {
    public void reverseString(char[] s) {
        int right = s.length - 1;
        for(int left = 0; left < s.length/2; left++) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            right -= 1;
        }
    }
}