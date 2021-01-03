/*You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
Example 3:

Input: matrix = [[1]]
Output: [[1]]
Example 4:

Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]
 

Constraints:

matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
*/


public class RotateImage {


    /*
    Time complexity is O(N^2)
    Space complexity is O(1) as its done in place

    solution is to transpose the matrix and then reverse each row

    */
    public static void rotate(int[][] matrix) {

        transpose(matrix);
        for (int[] row: matrix){
            reverse(row);
        }

        
    }
    /*
        
        The transpose of a matrix is simply a flipped version of the original matrix. 
        We can transpose a matrix by switching its rows with its columns. 
        We denote the transpose of matrix A by A^T 

        [1 2 3]           [1 4]
        [4 5 4]  becomes  [2 5]
                          [3 6]

        [1 2]           [1 4]
        [4 5]  becomes  [2 5]
                          

        since the constrains in this show its an n * n matrix we know we can do it in place
        simply swap 
    */
    private static void transpose(int[][] matrix) {

        int n = matrix.length;

        for (int r = 0; r < n; r++){
            for (int c = r ; c < n; c++){
                int temp = matrix[r][c];
                matrix[r][c] = matrix[c][r];
                matrix[c][r] = temp;
            }
        }

    }

    private static void reverse(int[] matrix) {

        int n = matrix.length;
        for(int i = 0; i < n/2; i++){
            int temp = matrix[i];
            matrix[i] = matrix[n - 1 - i];
            matrix[n - 1 - i] = temp;

        }
    }





    

    public static void main(String[] args){


        System.out.println("Problem: Rotate Image");
        int[][] A = {{1,2,3},{4,5,6},{7,8,9}};
        int[][] B = {{1,1,0},{1,0,1},{0,0,0}};

        print (A);
        System.out.println("solution");

        rotate(A);
        print(A);




    }


    public static void print(int[][] A){

        System.out.println("-----------------------------");


        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j <A[i].length; j++) {
                System.out.print(A[i][j] + " ");
            }
            System.out.println("");
        }
        System.out.println("-----------------------------");

    }
    
}
