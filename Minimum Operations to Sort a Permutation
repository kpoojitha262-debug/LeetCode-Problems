class Solution {
    public int minOperations(int[] nums) {
        int n = nums.length;
        if (n == 1) return 0;
        int idx = -1;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                idx = i;
                break;
            }
        }
        boolean isInc = true;
        for (int k = 0; k < n; k++) {
            if (nums[(idx + k) % n] != k) {
                isInc = false;
                break;
            }
        }
        boolean isDec = true;
        for (int k = 0; k < n; k++) {
            if (nums[(idx - k + n) % n] != k) {
                isDec = false;
                break;
            }
        }     
        int ans = Integer.MAX_VALUE;
        if (isInc) {
            ans = Math.min(ans, idx); 
            if (idx > 0) {
                ans = Math.min(ans, n - idx + 2);
            }
        }
        if (isDec) {
            ans = Math.min(ans, n - idx); 
            ans = Math.min(ans, idx + 2); 
        }
        
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}
