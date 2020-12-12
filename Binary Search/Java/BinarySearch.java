
/*

https://leetcode.com/problems/binary-search/

Given a sorted (in ascending order) integer array nums of n elements and a target value, 
write a function to search target in nums. If target exists, then return its index, otherwise return -1.

//interesting article: https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
explains the use of lo + (hi - lo) / 2 in order to avoid overflow.

it fails if the sum of low and high is greater than the maximum positive int value (2^31 - 1). 
The sum overflows to a negative value, and the value stays negative when divided by two. 
This would happen if the array size happened to be massive.

In C this causes an array index out of bounds with unpredictable results. In Java, 
it throws ArrayIndexOutOfBoundsException.

Bit shifting concepts:
https://www.interviewcake.com/concept/java/bit-shift

*/



public class BinarySearch{




    public static int search(int[] nums, int target){

        int hi = nums.length - 1;
        int lo = 0;

        while (lo <= hi){

            //shifting bits to the right by 1 divides by 2
            int mid = (hi + lo) >>> 1;
            // Alternatively int mid = lo + (hi - lo)/ 2;
            int val = nums[mid];

            if (val == target) return mid;
            else if (val < target){
                lo = mid + 1;
            }else if (val > target){
                hi = mid - 1;
            }

        }

        return -1;


    }



    public static void main(String[] args){


        System.out.println("Problem: Binary Search");
        int[] arrA = {-1,0,3,5,9,12,679856099};
        System.out.println(search(arrA, 9));


        System.out.println("-----------------------------");
        System.out.println("Overflow testing");
        System.out.println("-----------------------------");


        // Testing with overflow.

        int a = 1798560999;
        int b = 989856099;

        int d = 1798560999 + 989856099;
        System.out.println("d = 1798560999 + 989856099 = " + d);
        System.out.println("-----------------------------");
        System.out.println("Clear overflow, as the value is negative d = " + d);

        System.out.println("-----------------------------");

        int e = d >>> 1;
        System.out.println("-1506550198 >>> 1 = " + e);
        System.out.println("No more overflow, logical right shift, returns value of (1798560999 + 989856099) / 2");


        int f = -1506550198 >>> 1;
        //10100110001100111101111001001010 >>> 1 = 
        //01010011000110011110111100100101
        //this pushes the overflow back 1 which sets it to the actuall value of
        //1394208549
        
        System.out.println (f);

        int h = b + (a - b) / 2;
        System.out.println(h);

        //1394208549


        
        
        




    }


}