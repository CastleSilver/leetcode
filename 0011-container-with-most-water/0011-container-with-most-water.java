class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int ans = 0;
        while(left < right) {
            int curAmt = (right - left) * (height[left] < height[right]? height[left] : height[right]);
            ans = ans < curAmt ? curAmt : ans;
            if(height[left] < height[right]) left += 1;
            else right -= 1;
        }
        return ans;
    }
}