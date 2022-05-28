class Solution {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        
        int e = 0;
        for (int i : nums) {
            if (e != i) {
                return e;
            }
            
            e++;
        }
        
        return e;
    }
}