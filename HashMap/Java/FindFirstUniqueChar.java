import java.util.HashMap;

/*


Find Unique Character in string: https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.


 You may assume the string contains only lowercase English letters.

 https://en.m.wikipedia.org/wiki/ASCII

*/

public class FindFirstUniqueChar{




    public static int firstUniqChar(String s) {


        HashMap<Character, Integer> hm = new HashMap<>();
        char[] chArray = s.toCharArray();
        for(char c: chArray){
            hm.put(c, hm.getOrDefault(c, 0) + 1);
        }

        for(int i = 0; i < s.length(); i++){
            if(hm.get(chArray[i]) == 1){
                return i;
        }
        
        }



        return -1;
    }

    public static int firstUniqCharFast(String s) {
        int[] freq = new int[26];
        char[] chrArray = s.toCharArray();
        int n = chrArray.length;
        
        
        
        //populate an array with frequency of each letter
        //if value is a - a = index 0 of the array,
        // b- a = 1 so that would be index 1
        //essentially builds array from [a-z] for each
        //index sequencially
        for (int i = 0; i < n; i++){
            freq[chrArray[i] - 'a']++;
           
        }
              
        for (int i = 0; i<n; i++){
            if (freq[chrArray[i] - 'a'] == 1){
                return i;
            }   
        }
  
       return -1;
          
          
          
          
          
      }


    public static void main(String[] args){


        System.out.println("Problem: First Unique Char");
        String s = "leetcode";
        String y = "loveleetcode";
        System.out.println(firstUniqChar(s));
        System.out.println(firstUniqChar(y));
        System.out.println(firstUniqCharFast(s));
        System.out.println(firstUniqCharFast(y));


    }
    

}