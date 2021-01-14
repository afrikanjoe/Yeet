/*

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.



*/

import java.util.*;


public class LongestSubstringNoRepeats{


    public static int lengthOfLongestSubstring(String s) {
        
        Map<Character, Integer> map = new HashMap<>();
        int begin = 0, end = 0, counter = 0, d = 0;

        while (end < s.length()) {
            char c = s.charAt(end);
            map.put(c, map.getOrDefault(c, 0) + 1);

            if(map.get(c) > 1) counter++;
            end++;
            
            while (counter > 0) {

                char charTemp = s.charAt(begin);
                
                if (map.get(charTemp) > 1) counter--;
                
                map.put(charTemp, map.get(charTemp)-1);
                
                begin++;
            }
            d = Math.max(d, end - begin);
        }
        return d;

    }
        public static void main (String[] args){

            String s = "pwwkew";
            System.out.println(lengthOfLongestSubstring(s));





        }



}