/*

Arrays Easy
https://leetcode.com/problems/contains-duplicate

*/

import java.util.*;

public class ContainsDuplicate{


    public static boolean containsDup(int[] nums){
        
        HashSet<Integer> hs = new HashSet<>();
        for(int i: nums){
        
            // if (hs.contains(i)) return true;
            // hs.add(i);
            
            if(hs.add(i) == false) return true;
            
            
        }
        return false;

    }

    //another way would be to sort and return true if the number next to previous is true

    public static boolean containsDupSorted(int[] nums){
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 1; i++){
            if(nums[i] == nums[i+1]) return true;
        }
        return false;


    }


    public static void main(String[] args){

        int[] arrayA = { 1,3,4,5,7,8 };
        System.out.println(containsDup(arrayA));
        System.out.println(containsDupSorted(arrayA));
        


    }
}