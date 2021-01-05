/*


https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]





*/
import java.util.*;


public class FindAllDuplicates {




    //O(N) solution, very similar to find disappeared numbers solution

    public static List<Integer> findDuplicates(int[] nums) {
        
        
        List<Integer> res = new ArrayList<>();
        
        for (int i = 0; i < nums.length; i++){
            int idx = Math.abs(nums[i]) - 1;
            
            if (nums[idx] < 0){
                res.add(Math.abs(nums[i]));
            }
            nums[idx] = -nums[idx];
        }
        
        
        return res;
    }






    

    public static void main(String[] Args) {

        System.out.println("Problem: Find All Duplicates");
        int[] arrayA = { 4, 3, 2, 7, 8, 2, 3, 1 };

        printList(findDuplicates(arrayA));

    }
    public static void print(int[] A) {

        for (int a : A) {
            System.out.print(a + " ");
        }
        System.out.println();

    }

    public static void printList(List<Integer> value) {

        System.out.println(Arrays.toString(value.toArray()));

    }
    
}
