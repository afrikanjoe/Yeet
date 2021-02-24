/*

https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.



*/

public class MaxProdSubArray {

    // the idea here is that if there are even number of negatives
    // then you can just go forward, if odd number of negatives
    // then you'll need to go forward and backwards to return
    // the correct result (this is 0(N)time O(1)space
    public static int maxProductTwoPass(int[] nums) {

        int maxProd = Integer.MIN_VALUE;
        int curProd = 1;

        for (int i = 0; i < nums.length; i++) {

            curProd *= nums[i];
            maxProd = Math.max(maxProd, curProd);

            // reset if it's zero to avoid all zero max prod
            // i.e [0,2,3,4,-3]
            if (nums[i] == 0)
                curProd = 1;

        }

        curProd = 1;

        // reverse the array
        for (int i = nums.length - 1; i >= 0; i--) {

            curProd *= nums[i];
            maxProd = Math.max(maxProd, curProd);

            // reset if it's zero to avoid all zero max prod
            // i.e [0,2,3,4,-3]
            if (nums[i] == 0)
                curProd = 1;

        }
        return maxProd;

    }

    // O(N)time O(1)space
    public static int maxProductKadanes(int[] nums) {

        int prevMax = nums[0]; // max from previous iteration
        int prevMin = nums[0]; // min from previous iteration
        int max = nums[0]; // max from this iteration
        int min = nums[0]; // min this iteration

        int maxProd = nums[0];

        for (int i = 1; i < nums.length; i++) {

            // subproblem: use previous max/min * num[i] or restart from i.
            // the absolute value of the min could be larger so it should be stored in// in
            // case the
            // next value is negative.

            int val = nums[i];

            max = Math.max(Math.max(prevMax * val, prevMin * val), val);
            min = Math.min(Math.min(prevMax * val, prevMin * val), val);

            prevMax = max;
            prevMin = min;

            maxProd = Math.max(maxProd, max);

        }

        return maxProd;

    }

    public static void main(String[] args) {

        int[] A = { 2, 3, -2, 4 };

        System.out.println(maxProductTwoPass(A));
        System.out.println(maxProductKadanes(A));

    }
}