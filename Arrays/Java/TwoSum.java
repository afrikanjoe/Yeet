/*

Two Sum
https://leetcode.com/problems/two-sum/

Joseph Mugisha
*/

import java.util.HashMap;

public class TwoSum {


    public static void main ( String[] Args){

        System.out.println("Problem: Two Sum");
        int[] arrayA = {12, 28, 46, 32, 50};

        
        print(twoSumBruteForce(arrayA, 82));
        print(twoSumOnePass(arrayA, 82));
        print(twoSumTwoPass(arrayA, 82));

    }



    public static int[] twoSumTwoPass(int[] nums, int target) {
            
        HashMap <Integer, Integer> hm = new HashMap<>();
       
        for(int i = 0; i< nums.length; i++){
            hm.put(nums[i],i); 
        }
           
        for (int i = 0; i < nums.length; i++){
            int complement = target - nums[i];
            
            if (hm.containsKey(complement) && hm.get(complement) != i){
                return new int[] {i, hm.get(complement)};   
            }       
        }
           
           throw new IllegalArgumentException("no solution");
       
    }


    public static void print(int[] A){

        for(int a: A){
            System.out.print(a + " ");
        }
        System.out.println();


    }

    public static int[] twoSumOnePass(int[] nums, int target) {
        int [] indices = new int [2];
        HashMap<Integer,Integer> hm = new HashMap <>();
            
        for(int i = 0; i < nums.length; i++){
            int complement = target - nums [i];
                
            if (hm.containsKey(complement)){
                indices[0] = hm.get(complement);
                indices[1] = i; 
                return indices;
            }
            hm.put(nums[i], i);
                
        }

        return new int []{};
            
            
    }


    public static int[] twoSumBruteForce(int[] nums, int target) {
            
        int[] sum = new int[2];
            
        for (int i = 0; i < nums.length; i++){
            for (int j = i + 1; j < nums.length; j++){
                if ((nums[i] + nums[j]) == target){
                    sum[0] = i;
                    sum[1] = j;
                }               
            }
        }
            
        return sum;
            
        
    }

}
