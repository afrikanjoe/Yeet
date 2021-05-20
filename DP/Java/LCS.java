/*

https://leetcode.com/problems/longest-common-subsequence/submissions/

https://leetcode.com/problems/longest-common-subsequence/discuss/351689/JavaPython-3-Two-DP-codes-of-O(mn)-and-O(min(m-n))-spaces-w-picture-and-analysis

https://en.m.wikipedia.org/wiki/Longest_common_subsequence_problem

https://www.youtube.com/watch?v=57cfxtP9acI

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.


*/

public class LCS{

    public static int longestCommonSubsequence(String s1, String s2){

        int [][]dp = new int[s1.length() + 1][s2.length() + 1];
        for (int i = 0; i < s1.length(); i++){
            for(int j = 0; j <s2.length(); j++){
                if(s1.charAt(i) == s2.charAt(j)) dp[i+1][j+1] = 1 + dp[i][j];
                else dp[i + 1][j + 1] = Math.max(dp[i][j+1], dp[i+1][j]);     
            }
        }
        return dp[s1.length()][s2.length()];


    }




    public static void main(String[] args){

        String s1 = "abcde";
        String s2 = "ace";

        System.out.print("LCS = " + longestCommonSubsequence(s1, s2) + " ");


    }
}