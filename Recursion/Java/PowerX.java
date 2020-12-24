/*

Implement pow(x, n), which calculates x raised to the power n (i.e. x^n).

https://leetcode.com/problems/powx-n


Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25



*/


public class PowerX {

    public static double myPow(double x, int n) {
        
        if (x == 1) return 1;
        if (n == 0) return 1;
        
         // if n = Integer.MIN_VALUE, n = -1 * n will overflow
        // Integer.MIN_VALUE = -2^31, Integer.MAX_VALUE = 2^31-1
        
        if (n < 0 && n > Integer.MIN_VALUE ){
                x = 1/x;
                n = -1 * n;
        }
        return n % 2 == 0 ? myPow(x * x, n/2) : myPow(x * x, n/2) * x;
    
        
    }


    public static void main(String[] args){


        System.out.println("Problem: Find the Power");
        System.out.println(myPow(2.00000, -2));
     
        


    }





    
}
