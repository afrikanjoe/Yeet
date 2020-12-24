/*

https://leetcode.com/problems/search-insert-position/
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

*/

public class SearchInsert {



    public static int searchInsertBS (int[] nums, int target){

        int lo = 0;
        int hi = nums.length - 1;

        while(lo <= hi){
            int mid = hi + lo >>> 1;
            if(nums[mid] == target) return mid;
            if(nums[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }


        return lo;


    }



    public static void main(String[] args){


        System.out.println("Problem: Search Insert");
        int[] arrA = {1,3,5,6};
        int target = 7;
        System.out.println(searchInsertBS(arrA, target));


    }
    
}
