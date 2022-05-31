class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<>();
        int[] values = {-1, -1};
        
        for (int i = 0; i < nums.length; i++) {
            try {
                values[0] = seen.get(target - nums[i]);
                values[1] = i;
                break;
            } catch (Exception e) {
                seen.put(nums[i], i);
            }
        }
        
        return values;
    }
}