class Solution {
    public int removeDuplicates(int[] nums) {
        int write = 1;
        for(int i = 1; i < nums.length; i++) {
            if(nums[i] != nums[i-1]) {
                nums[write] = nums[i];
                write += 1;
            }
        }
        return write;
    }
}