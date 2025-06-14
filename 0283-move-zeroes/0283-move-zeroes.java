class Solution {
    public void moveZeroes(int[] nums) {
        int write = 0;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] != 0) {
                nums[write] = nums[i];
                write += 1;
            }
        }
        for(int j = write; j < nums.length; j++) {
            nums[j] = 0;
        }
    }
}