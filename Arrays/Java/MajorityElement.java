import java.util.HashMap;

/*

https://leetcode.com/problems/majority-element/

There is a div and conquer solution to this problem

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2


*/


public class MajorityElement{




    public static int findMajorityElement(int[] nums){

        
        int maj = nums.length/2;
        
        HashMap<Integer, Integer> hm = new HashMap<>();
        
        //if the number appears more than to maj return num
        //store each number in hashmap and return if the number of appearances is > maj
        
        
        for(int num: nums){
            hm.put(num, (hm.getOrDefault(num, 0) + 1));
        }
        
        for (int i = 0; i < nums.length; i++){
            if (hm.get(nums[i]) > maj){
                return nums[i];
            }
        }
        
        return -1;

    }


    //optimized so as to return first occurence of greater than maj while iterating through

    public static int findmajorityElementOptimize(int[] nums) {
        int maj = nums.length/2;
        int value = 0;
        
        HashMap<Integer,Integer> hm = new HashMap<>();
        
        
        for(int num: nums){
            if(!hm.containsKey(num))
                hm.put(num,1);
            else
                hm.put(num, hm.get(num)+1);
            if(hm.get(num) > maj){
                value = num;
                break;
            }
        }
        
        return value;
        
    }






    public static void main(String[] args){


        System.out.println("Problem: Find maj element");
        int[] arrayA = {2,2,1,1,1,2,2};
        System.out.println(findMajorityElement(arrayA));
        System.out.println(findmajorityElementOptimize(arrayA));
        


    }




}