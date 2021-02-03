import java.util.*;
/*

Subarray Sum Equals K

https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, 
return the total number of continuous subarrays whose sum equals to k.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107


https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/prefix_sum
Prefix sum.


The tricky part is, how to find the sum of a subarray fast? For example, you're given an array nums, 
and asked to implement API sum(i, j) which returns the sum of nums[i..j]. 
Furthermore, the API will be very frequently used. How do you plan to implement this API?
Due to the high frequency, it is very inefficient to traverse through nums[i..j] each time. 
Is there a quick method which find the sum in time complexity of O(1)? 


*/





public class subarraySum{


    //the idea behind this is prefix sum


    public static int subarraySumPrefix(int[] nums, int k){

        //edge cases

        if(nums.length == 0) return 0;

        int count= 0;
        int sum = 0;

        //we need to count the frequency
        //map: prefix sum -> frequency
        HashMap <Integer, Integer> preSum = new HashMap<>();

        //base case
        preSum.put(0,1);

    
        for (int num: nums){

            sum += num;

            //prefix sum we want to find nums[0....j]
            int sum_j = sum - k;

            // update result if it exists
            if(preSum.containsKey(sum_j)){
                count += preSum.get(sum_j);
            }

            // record the prefix sum nums[0...i] and its frequency
            preSum.put(sum, preSum.getOrDefault(sum, 0) + 1);

        }

        return count;

    }

    public static void main(String[] args){

        int[] arrA = {1,1,1,-1};
        int k = 2;

        int sum = subarraySumPrefix(arrA, k);

        System.out.println(sum);


    }





}