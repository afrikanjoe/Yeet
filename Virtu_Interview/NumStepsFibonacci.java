/*

Given any positive integer, determine the number of steps to Closest Fibonacci Number.

*/


public class NumStepsFibonacci {


    public static int numStepsFib(int n){

        if (n == 0) return 0;

        int firstVal = 0;
        int secondVal = 1;
        int thirdVal = firstVal + secondVal;

        while (thirdVal <= n){
            firstVal = secondVal;
            secondVal = thirdVal;
            thirdVal = firstVal + secondVal;

        }


        int steps1 = Math.abs(thirdVal - n);
        int steps2 = Math.abs(secondVal - n);
        int ans = (steps1 >= steps2) ? steps2 : steps1;

        return ans;

    }



    public static void main(String[] args){

        int n = 9;
        System.out.println(numStepsFib(n));
        //0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

    }
    
}
