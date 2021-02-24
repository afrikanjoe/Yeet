/*


https://leetcode.com/problems/maximum-subarray/

Kadane's algorithm

*/


public class MaxSubArray {



    public static int maxSubArray(int[] A) {
        int best = A[0]; 
        int sum = A[0];
        
        if (A.length == 0){
            return 0;
        }
        for (int i = 1; i < A.length; i++){
            //subproblem
            sum = Math.max(A[i], sum + A[i]);

            best = Math.max(best, sum);
        }
        return best;
        
    }


    public static void main(String[] args){


        System.out.println("Problem: max Sub Array");
        int[] arrayA = {-2,1,-3,4,-1,2,1,-5,4};
        System.out.println(maxSubArray(arrayA));
        


    }
    
}
