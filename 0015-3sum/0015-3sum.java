class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        mergeSort(nums, 0, nums.length - 1);
        
        List<List<Integer>> ans = new ArrayList<>();
        for(int i = 0; i < nums.length - 2; i++) {
            if(i > 0 && nums[i] == nums[i-1]) continue;
            if(nums[i] > 0) {
                return ans;
            }
            int left = i + 1;
            int right = nums.length - 1;

            while(left < right) {
                if(nums[left] + nums[right] == -nums[i]) {
                    ans.add(new ArrayList<>(Arrays.asList(nums[left], nums[right], nums[i])));
                    right -= 1;
                    left += 1;
                    while(left < right && nums[left] == nums[left-1]) left += 1;
                } else if(nums[left] + nums[right] > - nums[i]) {
                    right -= 1;
                } else {
                    left += 1;
                }
            }

            
        }
        return ans;
        
    }
    public void mergeSort(int[] nums, int left, int right) {
    if (left < right) {
        int mid = (left + right) / 2;
        mergeSort(nums, left, mid);
        mergeSort(nums, mid + 1, right);
        merge(nums, left, mid, right);
    }
}

    public void merge(int[] nums, int left, int mid, int right) {
        int[] temp = new int[right - left + 1];

        int i = left;
        int j = mid + 1;
        int k = 0;

        while(i <= mid && j <= right) {
            if(nums[i] < nums[j]) {
                temp[k++] = nums[i++];
            } else {
                temp[k++] = nums[j++];
            }
        }
        while(i <= mid) temp[k++] = nums[i++];
        while(j <= right) temp[k++] = nums[j++];

        for(int l = 0; l < temp.length; l++) {
            nums[left + l] = temp[l];
        }
    }
}