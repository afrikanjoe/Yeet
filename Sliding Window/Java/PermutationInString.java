/*

Given two strings s1 and s2, 
write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

https://leetcode.com/problems/permutation-in-string/

*/


import java.util.*;




public class PermutationInString{


    public static boolean checkInclusion(String s1, String s2) {
    
        if(s1 == null || s2 == null) {
            return false;
        }
        
        int windowlen = s1.length();
        Map<Character, Integer> map = new HashMap<>();
        for(char c: s1.toCharArray()){
            map.put(c, map.getOrDefault(c,0) + 1);
        }
        
        int count = map.size();
        int beginWindow = 0;
        int endWindow = 0;
        
        //start at end of window
        
        while(endWindow < s2.length()){
            char ch = s2.charAt(endWindow);
            
            if(map.containsKey(ch)){
                map.put(ch, map.get(ch) - 1);
                //decrement map size if there is no longer
                //a number associated with the character
                if(map.get(ch) == 0){
                    count--;
                }
            }
            while(count == 0){
                if(endWindow - beginWindow + 1 == windowlen){
                    return true;
                }
                
                char temp = s2.charAt(beginWindow);
                if(map.containsKey(temp)){
                    map.put(temp, map.get(temp) + 1);
                    if(map.get(temp) > 0){
                        count++;
                    }    
                }
                
                beginWindow++;
            }
            endWindow++;
        }
        return false;
    }

    public static void main (String[] args){


        String s1 = "ab";
        String s2 = "eidbaooo";
        System.out.println(checkInclusion(s1, s2));

    }
            
            
}




