/*

https://leetcode.com/problems/subarray-product-less-than-k/

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:

Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.


*/

public class SubarrayLessThanK {

    public static int numSubarrayProductLessThanK(int[] nums, int k) {

        // sliding window in this instance only really works because the numbers remain positive.
        if (k <= 1)
            return 0;
        int prod = 1;

        int begin = 0, end = 0, result = 0;

        while (end < nums.length) {

            prod *= nums[end++];
            while (prod >= k)
                prod /= nums[begin++];
            result += end - begin;

        }

        return result;

    }

    public static void main (String[] args){

        int[] nums = {10, 5, 2, 6};
        int k = 100;

        System.out.println(numSubarrayProductLessThanK(nums, k));






    }



}