/*
Given a positive integer, return the closest number of the Fibonacci sequence, under these rules:

The closest Fibonacci number is defined as the Fibonacci number with the smallest absolute difference with the given integer. 
For example, 34 is the closest Fibonacci number to 30, because |34 - 30| = 4, 
which is smaller than the second closest one, 21, for which |21 - 30| = 9.

If the given integer belongs to the Fibonacci sequence, 
the closest Fibonacci number is exactly itself. For example, the closest Fibonacci number to 13 is exactly 13.

In case of a tie, you may choose to output either one of the Fibonacci numbers that are both closest to the input
 or just output them both. For instance, if the input is 17, 
 all of the following are valid: 21, 13 or 21, 13. In case you return them both, please mention the format.


*/

public class ClosestFibonacci {

    public static int findClosest(int n) {

        if (n == 0)
            return 0;

        int firstVal = 0;
        int secondVal = 1;
        int thirdVal = firstVal + secondVal;

        while (thirdVal <= n) {
            firstVal = secondVal;
            secondVal = thirdVal;
            thirdVal = firstVal + secondVal;

        }

        int ans = (Math.abs(thirdVal - n) >= Math.abs(secondVal - n)) ? secondVal : thirdVal;

        return ans;

    }

    public static void main(String[] args) {

        int n = 55;
        System.out.println(findClosest(n));
        // 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

    }

}
