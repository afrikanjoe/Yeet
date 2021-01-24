/*
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, 
try coding another solution of which the time complexity is O(n log n). 

https://leetcode.com/problems/minimum-size-subarray-sum/


*/


public class MinSizeSubArraySum {

    public static int minSubArrayLen(int s, int[] nums){

        int sum = 0;
        int end = 0;
        int beg = 0;
        int minWindowLen = Integer.MAX_VALUE;

        while (end < nums.length){
            sum += nums[end];

            while(sum >= s){
                minWindowLen = Math.min(minWindowLen, end - beg + 1);
                sum -= nums[beg];
                beg++;
            }
            end++;
        }


        return minWindowLen == Integer.MAX_VALUE ? 0 : minWindowLen;

    }

    public static void main (String[] args){


        int s = 7;
        int[] nums = {2,3,1,2,4,3};
        int result = minSubArrayLen(s,nums);

        System.out.println(result);






    }



    
}
