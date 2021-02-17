
/*

https://leetcode.com/problems/longest-repeating-character-replacement/

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


*/

import java.util.*;

public class LongestRepeatingCharRepl {

    public static int characterReplacement(String s, int k) {

        int end = 0;
        int begin = 0;
        int dominantChar = 0;
        int maxWindow = 0;

        HashMap<Character, Integer> hm = new HashMap<>();

        while (end < s.length()) {

            char ch = s.charAt(end++);
            hm.put(ch, hm.getOrDefault(ch, 0) + 1);

            // What causes you to stop the window growth.
            // well if k = 1 currwindow = AABAB 4-0 - 3 (dominantChar A in this window) > 1
            dominantChar = Math.max(dominantChar, hm.get(ch));
            if (end - begin - dominantChar > k) {
                char remove = s.charAt(begin);
                hm.put(remove, hm.get(remove) - 1);
                begin++;
            }

            maxWindow = Math.max(maxWindow, end - begin);

        }

        return maxWindow;

    }

    public static void main(String[] args) {

        String s = "AABABBA";
        int k = 1;

        System.out.println(s);
        System.out.println(k);
        System.out.println(characterReplacement(s, k));

    }

}
