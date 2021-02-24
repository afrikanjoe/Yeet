import java.util.*;
/*
Given an unsorted integer array nums, find the smallest missing positive integer.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space?

solution explanation: 

solution must be in range 1... n or the result is n + 1

1- Ignore all numbers <=0 and >n since they are outside the range of possible answers 
(which we proved was [1..n]). We do this by replacing them with the value n+1.
2- For all other integers <n+1, 
mark their bucket (cell) to indicate the integer exists. (*see below)
3- Find the first cell not marked, that is the first missing integer. 
If you did not find an unmarked cell, there was no missing integer, so return n+1.




*/

public class FirstMissingPositive {

    // O(N) very similar to find disappeared numbers
    public static int firstMissingPos(int[] nums) {

        int n = nums.length;

        // mark numbers < 0 and num > n with mark number in this case n + 1
        for (int i = 0; i < n; i++) {
            if (nums[i] <= 0 || nums[i] > n) {
                nums[i] = n + 1;
            }
        }

        // mark all cells in array convert idx to negative
        for (int i = 0; i < n; i++) {
            int idxNum = Math.abs(nums[i]);
            if (idxNum > n) {
                continue;
            }
            idxNum--;

            if (nums[idxNum] > 0) {
                nums[idxNum] = -nums[idxNum];
            }
        }

        // find FIRST non negative cell
        for (int i = 0; i < n; i++) {
            if (nums[i] >= 0) {
                return i + 1;
            }
        }

        // no pos numbers found this means it was in range 1... n so return n + 1
        return n + 1;

    }

    public static void main(String[] args) {

        int[] nums = { 3, 4, -1, 1 };
        System.out.println(firstMissingPos(nums));

    }

}
