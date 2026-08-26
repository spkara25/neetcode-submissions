class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length; 
        HashMap<Integer, Integer> seen = new HashMap<>(); 
        int complement = 0; 
        for(int i = 0;i<n;i++) {
            complement = target - nums[i]; 
            if(seen.containsKey(complement))
            {
                return new int[] {seen.get(complement), i}; 
            }
            seen.put(nums[i],i); 
        }
        return new int[] {-1, -1}; 
    }
}
