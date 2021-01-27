/*


You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104

https://leetcode.com/problems/search-in-rotated-sorted-array/





*/


public class SearchSortedArray {



    public static int search(int[] nums, int target) {
        
        int n = nums.length - 1;
        int minIdx = findMin(nums);
        int lo = (target <= nums[n] ) ? minIdx : 0;
        int hi = (target > nums[n]) ? minIdx: n;
    
        while (lo <= hi){
            
            int mid = lo + hi >>> 1;
            int val = nums[mid];
            
            if(val == target) return mid;
            else if (val < target){
                lo = mid + 1;
            }else if (val > target){
                hi = mid - 1;
            }    
   
        }
        return -1;
    
    }
    
    
    private static int findMin(int [] nums){
        
        int lo = 0;
        int hi = nums.length - 1;
        
        if (nums.length == 1 || nums[hi] > nums[lo])
            return 0;
        
        
        while (lo < hi){
            int mid = lo + hi >>> 1;
            
            if (nums[mid] > nums[mid + 1]){
                return mid + 1;        
            }
            
            if (nums[ mid - 1] > nums [mid]){
                return mid;
            }
            
            if (nums[mid] > nums[0]){
                lo = mid + 1;
            }else{
                hi = mid - 1;
            }
        }
        
        return -1;


        /*
            public int findMinIdx(int[] nums) {
                int start = 0, end = nums.length - 1;
                while (start < end) {
                    int mid = start + (end -  start) / 2;
                    if (nums[mid] > nums[end]) start = mid + 1;
                     else end = mid;
                }
	            return start;
            }


        */
    
    }


    public static void main(String[] args){



        int[] arrA = {4,5,6,7,0,1,2};
        System.out.println("Find target in Sorted rotated Array");
        System.out.println(search(arrA, 0));


    }




    
}
