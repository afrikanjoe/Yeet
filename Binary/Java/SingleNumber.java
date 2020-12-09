import java.util.HashMap;

/*

Single Number: https://leetcode.com/problems/single-number/

Given a non empty array of integers nums, every element appears twice except for one elementfind that single one

Bit manipulation: O(N) & O(1)
HashMap

*/


public class SingleNumber {


    public static int singleNumber(int[] nums){
        int unique = 0;

        for(int num: nums){
            unique ^= num;

        }
        return unique;

    }

    public static int singleNumberHM(int[] nums){
        HashMap<Integer, Integer> hm = new HashMap<>();

        for(int num: nums){
            hm.put(num, hm.getOrDefault(num , 0) + 1);
        }

        for(int num: nums){
            if(hm.get(num) == 1){
                return num;
            }
        }

        return -1;


    }


    public static void main(String[] args){

        System.out.println("Problem: Single Number");
        int[] arrA = {4,1,2,1,2};
        System.out.println(singleNumber(arrA));
        System.out.println(singleNumberHM(arrA));




    }







    
}
