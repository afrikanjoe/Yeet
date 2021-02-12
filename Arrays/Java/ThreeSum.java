import java.util.*;
/*


https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105





*/

public class ThreeSum {


    //O(N * N)
    public static List<List<Integer>> threeSum(int[] nums) {

        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);

        int n = nums.length;

        for (int i = 0; i < n - 2; i++) {
            // if the first value in sorted array is greater than 0 it doesn't exist return
            // empty list
            if (nums[i] > 0)
                break;

            // skip values that have already appeared
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            int target = -nums[i];

            int lo = i + 1;
            int hi = n - 1;


            // iterate through using two pointer method
            while (lo < hi) {

                int tempSum = nums[lo] + nums[hi];
                if (tempSum == target) {
                    res.add(Arrays.asList(new Integer[] { nums[i], nums[lo], nums[hi] }));
                    lo++;
                    while (lo < hi && nums[lo] == nums[lo - 1]) {
                        lo++;
                    }
                    hi--;
                    while (lo < hi && nums[hi] == nums[hi + 1]) {
                        hi--;
                    }

                } else if (tempSum < target) {
                    lo++;

                } else {
                    hi--;
                }

            }

        }

        return res;

    }


    public static void main(String[] args){


        int[] nums = {-1,0,1,2,-1,-4};
         // Output: [[-1,-1,2],[-1,0,1]]

        System.out.println (threeSum(nums));

        

        






    }

}
