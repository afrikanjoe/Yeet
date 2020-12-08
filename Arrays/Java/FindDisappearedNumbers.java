
/*

Arrays Easy
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
*/
import java.util.*;

public class FindDisappearedNumbers {

    public static void main(String[] Args) {

        System.out.println("Problem: Find disappeared numbers");
        int[] arrayA = { 4, 3, 2, 7, 8, 2, 3, 1 };

        printList(findDisappeared(arrayA));

    }

    public static List<Integer> findDisappeared(int[] nums) {

        List<Integer> missingNums = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            int index = Math.abs(nums[i]) - 1;
            System.out.print(index);

            if (nums[index] > 0) {
                nums[index] = -nums[index];
            }

        }

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                missingNums.add(i + 1);
            }

        }

        return missingNums;

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