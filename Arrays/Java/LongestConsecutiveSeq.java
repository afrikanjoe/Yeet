/*

https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 104
-109 <= nums[i] <= 109


*/

import java.util.*;

public class LongestConsecutiveSeq {

    public static int longestConsecutiveSorting(int[] nums) {

        // edge cases
        if (nums.length == 0)
            return 0;

        Arrays.sort(nums);

        int longestStreak = 1;
        int currentStreak = 1;

        for (int i = 1; i < nums.length; i++) {

            // check if duplicate
            if (nums[i] != nums[i - 1]) {
                // check if the prev is nums[i -1] + 1, i.e 1,2
                if (nums[i] == nums[i - 1] + 1) {
                    currentStreak++;
                } else {
                    longestStreak = Math.max(currentStreak, longestStreak);
                    currentStreak = 1;
                }
            }
        }

        return Math.max(longestStreak, currentStreak);

    }

    public static int longestConsecutiveHashSet(int[] nums) {

        HashSet<Integer> hs = new HashSet<Integer>();

        for (int num : nums) {
            hs.add(num);
        }

        int longestStreak = 0;

        for (int num : hs) {

            // Main thing is making sure you skip the duplicates.
            if (!hs.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;

                while (hs.contains(currentNum + 1)) {
                    currentNum++;
                    currentStreak++;

                }

                longestStreak = Math.max(longestStreak, currentStreak);

            }

        }

        return longestStreak;

    }

    public static void main(String[] args) {

        int[] A = { 0, 3, 7, 2, 5, 8, 4, 6, 0, 1 };
        System.out.println(longestConsecutiveSorting(A));

        int[] B = { 0, 3, 7, 2, 5, 8, 4, 6, 0, 1 };
        System.out.println(longestConsecutiveHashSet(B));

    }

}