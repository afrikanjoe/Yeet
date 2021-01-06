/*


Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.


Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 
 */

public class SquaresOfSortedArray {

    // O(N) time, O(N) space
    public static int[] sortedSquares(int[] A) {

        int N = A.length;
        int[] result = new int[N];

        int i = 0;
        int j = N - 1;

        for (int idx = N - 1; idx >= 0; idx--) {

            if (Math.abs(A[i]) > Math.abs(A[j])) {
                result[idx] = A[i] * A[i];
                i++;
            } else {

                result[idx] = A[j] * A[j];
                j--;
            }

        }
        return result;

    }

    public static void main(String[] args) {

        System.out.println("Problem: Squares of sorted Array");
        int[] arrayA = { -4, -1, 0, 3, 10 };

        print(sortedSquares(arrayA));

    }

    public static void print(int[] A) {

        for (int a : A) {
            System.out.print(a + " ");
        }
        System.out.println();

    }

}
