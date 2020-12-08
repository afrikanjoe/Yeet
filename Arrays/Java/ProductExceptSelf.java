
/*

Arrays: https://leetcode.com/problems/product-of-array-except-self/

from comments by user abarganier: This is an array problem where they want an O(N) runtime and constant space, 
which indicates it's probably a greedy algorithm solution. Dynamic programming involves greater than O(1) space, 
and a runtime as low as O(N) usually indicates a greedy approach is needed when dealing with arrays.

Greedy algos usually involve keeping track of some running min/max/multiplier so keeping that in mind
can help come up with a O(N) time, O(1) space solution

*/

public class ProductExceptSelf{




    public static int[] productExceptSelfBruteForce(int[] nums){


        int [] productArr = new int[nums.length];

        for(int i = 0; i < nums.length; i++){
            int mul = 1;
            for (int j = 0; j < nums.length; j++){
                if( i == j){
                    //breaks out of single iteration
                    continue;
                }
                
                mul *= nums[j];             
            }
            productArr[i] = mul;
        }

        return productArr;


    }

    public static int[] productExceptSelfDivision(int[] nums){
        int mult = 1;
        for(int i = 0; i < nums.length;i++){
            mult *= nums[i];
        }

        for(int i = 0; i < nums.length; i++){

            nums[i] = mult / nums[i];
        }
        return nums;
    }


    //greedy algorithm

    public static int[] productExceptSelfOptimal(int [] nums){

        int[] result = new int[nums.length];
        result[0] = 1;

        int mult = 1;
        for(int i = 1; i < nums.length; i++){
            result[i] = nums[i - 1] * mult;
            mult = nums[i - 1] * mult;
        }

        mult = 1;
        for(int i = nums.length - 2; i >= 0; i--){
            result[i] = nums[i + 1] * result[i] * mult;
            mult = nums[i + 1] * mult;

        }

        return result;




    }

    // Testing
    public static void main(String[] args){


        System.out.println("Problem: product except self");
        int[] arrayA = {1, 2, 3, 4};
        int[] arrB = {1, 2, 3, 4};
        print(productExceptSelfBruteForce(arrayA));
        print(productExceptSelfDivision(arrayA));
        print(productExceptSelfOptimal(arrB));


    }

    public static void print(int[] A){

        for(int a: A){
            System.out.print(a + " ");
        }
        System.out.println();


    }


}