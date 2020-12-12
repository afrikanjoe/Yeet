/*

Peak Element: https://leetcode.com/problems/find-peak-element/

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, 
return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

relevant video: https://www.youtube.com/watch?v=HtSuA80QTyo&feature=youtu.be&t=1660


*/

public class PeakElement {



    //O(log 2(n))

    public static int findPeakElementBS(int[] nums){

        int lo = 0;
        int hi = nums.length - 1;

        while(lo < hi){

            int mid = hi + lo >>> 1;
            int val = nums[mid];

            if (val > nums[mid + 1]){
                hi = mid;     
            }else{
                lo = mid + 1;
            }

        }

        return lo;








    }



    // O(N) Time O(1) space
    public static int findPeakElementBF(int[] nums) {

        for(int i = 0; i < nums.length - 1; i++){

            if(nums[i] > nums[i+1]){
                return i;
            }
        }


        return nums.length - 1;

    }

    public static void main(String[] args){


        System.out.println("Problem: Peak Element");
        int[] arrA = {1,2,3,1};
        System.out.println(findPeakElementBF(arrA));
        System.out.println(findPeakElementBS(arrA));







    }
    
}
