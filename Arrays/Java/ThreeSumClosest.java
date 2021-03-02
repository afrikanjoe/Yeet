
/*

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.


Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4


*/
import java.util.*;

public class ThreeSumClosest {

    // O(n^2) best time solution sorting is O(nlogn)
    // ourter loop and inner loops going through n elemennts
    // Space complexity ( O(logn)) to O(n) depends on sorting algo

    //ALGO: sort check for closest difference and use the two pointer 
    // method to find the closest difference faster.
    public static int threeSumClosest(int[] nums, int target) {

        int diff = Integer.MAX_VALUE;
        int n = nums.length;

        Arrays.sort(nums);

        for (int i = 0; i < n && diff != 0; i++) {
            int lo = i + 1;
            int hi = n - 1;

            while (lo < hi) {
                int sum = nums[i] + nums[lo] + nums[hi];

                if (Math.abs(target - sum) < Math.abs(diff)) {
                    diff = target - sum;

                }
                if (sum < target)
                    lo++;
                else
                    hi--;

            }
        }

        return target - diff;

    }

    public static void main(String[] args) {

        int[] A = { -1, 2, 1, -4 };
        int target = 1;

        System.out.println(threeSumClosest(A, target));

    }

}
