/*

Find the index in the Fibonacci sequence if I gave you the Fibonacci number.

*/


public class FindIndexFib {
    


    public static int findFibIndex(int n){

        int count = 0;
        if (n == 0) return count;

        int first = 0;
        int second = 1;
        int third = first + second;


        while(third <= n){
            first = second;
            second = third;
            third = first + second;
            count++;
        }


        return count + 1;
    }



    public static void main(String[] args){

        //0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
        int n = 2;
        System.out.println(findFibIndex(n));

    }




}
