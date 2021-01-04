/*

Binary: https://leetcode.com/problems/missing-number/

nums contains disting numbers in range [0,n]
return the number in the range missing from the array

*/



public class MissingNumber{



    public static int missingNumberBit(int[] nums){

        int missingNum = nums.length;

        for(int i = 0; i < nums.length; i++){

            missingNum ^= nums[i] ^ i;

        }

        return missingNum;


    }

    public static int missingNumberGaussian(int[] nums){

       
        int n = nums.length;
        int gaussianSum = n * (n + 1)/2;

        int sumOfArray = 0;
        for(int num: nums){
            sumOfArray += num;
        }

        

        return gaussianSum - sumOfArray;

    }




    public static void main(String[] args){

        System.out.println("Problem: Missing Number");
        int[] arrA = {0, 2, 3, 1, 5};
        System.out.println(missingNumberBit(arrA));
        System.out.println(missingNumberGaussian(arrA));




    }

    public static void print(int[] A){

        for(int a: A){
            System.out.print(a + " ");
        }
        System.out.println();


    }



}