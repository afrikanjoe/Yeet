import java.util.HashMap;

/*
https://leetcode.com/problems/valid-anagram/

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?


*/



public class ValidAnagram {



    //O(N) O(1)
    public static boolean isAnagramUnicode(String s, String t) {
        
        if (s.length() != t.length()) return false;
        
        HashMap<Character,Integer> hm = new HashMap<>();
        
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();
        
        
        for (char n: sArray){
            hm.put(n,hm.getOrDefault(n,0)+1);
        }
        
        for(char x: tArray){
            hm.put(x,hm.getOrDefault(x,0)-1);

        }
        
        for(char n: sArray){
            if (hm.get(n) !=0){
                return false;
            }
        }
        
        return true;
        
    }

    //O(N) O(1)
    public static boolean isAnagram(String s, String t){


        if (s.length() != t.length()) return false;
        
        int[] counter = new int[26];        
        
        
        for (int i = 0; i< s.length(); i++){
            counter[s.charAt(i) - 'a']++;
            counter[t.charAt(i) - 'a']--; 
        }

        
        for(int count: counter){
            if (count != 0){
                return false;
            }
        }
        
        return true;
        



    }


    

    public static void main(String[] args){


        System.out.println("Problem: Valid Anagram");
        String a = "anagram";
        String b = "nagaram";
        String c = "anagra8";
        String d = "nagara8";
        System.out.println(isAnagram(a, b));
        System.out.println(isAnagramUnicode(c,d));



    }
    
}
