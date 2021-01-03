/*

Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] 
horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, 
inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]



*/
public class FlipImage {


    /* 

        Two pointer explanation, if you compare i and n-i-1 in row 
        if the values are the same you should flip if they aren't
        the same they remain the same. this makes sense when you think about
        reversing and then flipping, if they aren't different, they'll remain the same in the Solution
        i.e [1,1,0] becomes [1,0,0] compare 1 with 0 different so they remain the same, the middle or 
        if the values compared are equivalent then you'll flip. if there is a middle value it always flips
        as if you reverse its still in the middle and when you invert it inverts regardless
    */

    public static int[][] flipAndInvertImageTwoPointer(int[][] A) {
      

        int n = A.length;
        for (int[] row: A){
            //use n + 1 / 2 to include the middle value floor division
            for(int i = 0; i < (n + 1)/2; i++) {
                if (row[i] == row[n - i - 1]){
                    row[i] = row[n - i - 1] ^= 1;
                }
            }
        }
    
        return A;        
       
    }


      /*
        for (int row = 0; row<A.length; row++){
            int low = 0;
            int high = A[row].length-1;
            
            while (low <= high){
                if(A[row][low] == A[row][high]){
                    A[row][low] = 1 - A[row][low];
                    A[row][high] = A[row][low];                    
                }   
            low++;
            high--; 
            }   

            
        }
        */


    public static int[][] flipAndInvertImage(int[][] A){


        for (int[] row: A){
            reverse(row);
            flipbits(row);
        }


        return A;
    }

    private static void flipbits(int[] Row){

        for(int i = 0; i < Row.length; i++){

            Row[i] ^= 1 ;
        }

    }

    private static void reverse(int[] Row){

        int n = Row.length;
        for (int i = 0; i < n/2; i++){
            int temp = Row[i];
            Row[i] = Row[n - i - 1];
            Row[n - i - 1] = temp;
        }

    }




    public static void main (String[] args){


        System.out.println("Problem: Flip Image");
        int[][] A = {{1,1,0},{1,0,1},{0,0,0}};
        int[][] B = {{1,1,0},{1,0,1},{0,0,0}};

        print (A);
        System.out.println("Reversed and Inverted");
        System.out.println("BruteForce solution");
        print(flipAndInvertImage(A));
        System.out.println("Two Pointer solution");
        print(flipAndInvertImageTwoPointer(B));




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

