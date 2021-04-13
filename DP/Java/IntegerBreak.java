/*

https://twchen.gitbook.io/leetcode/dynamic-programming/integer-break

https://leetcode.com/problems/integer-break


Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

Constraints:

2 <= n <= 58



*/



public class IntegerBreak{



    // (O(log(n)))
    public static int integerBreakDP(int n) {
        
        // find subproblem 
        // n = 10
        //3 * 7, 3 * dp[7]
        // max product is based on previous integer
        int[] dp = new int[n + 1]  ;
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= i; j++){
                dp[i] = Math.max(dp[i], (i - j) * j);
                //(dp[10] = max(dp[10], 7 * 3)
                dp[i] = Math.max(dp[i], dp[j] * (i - j));
                //(dp[10] = max(dp[10], dp[7] * 3)
            }  
        }
        return dp[n];
        
    }

    public static void main (String[] args){

        System.out.println (integerBreakDP(10));


    }



}


/*



// Time complexity: O(1). Space complexity: O(1)
public int integerBreak(int n) {
    if (n <= 2) return 1;
    if (n == 3) return 2;

    if (n % 3 == 0) return (int) Math.pow(3, n / 3);
    if (n % 3 == 1) return 4 * (int) Math.pow(3, (n - 4) / 3);
    if (n % 3 == 2) return 2 * (int) Math.pow(3, (n - 2) / 3);

    return -1;
}

*/

