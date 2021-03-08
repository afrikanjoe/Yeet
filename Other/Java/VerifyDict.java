import java.util.*;

/*

Problem: https://leetcode.com/problems/verifying-an-alien-dictionary/
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.






*/

public class VerifyDict {

    public static boolean isAlienSorted(String[] words, String order) {

        for (int i = 1; i < words.length; i++) {
            if (bigger(order, words[i - 1], words[i])) {
                return false;
            }
        }
        return true;

    }

    public static boolean bigger(String order, String s1, String s2) {
        int n = s1.length();
        int m = s2.length();

        for (int i = 0; i < n && i < m; i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                return (order.indexOf(s1.charAt(i))) > (order.indexOf(s2.charAt(i)));
            }
        }
        return n > m;

    }

    public static void main(String[] args) {

        String order = "ngxlkthsjuoqcpavbfdermiywz";

        int[] count = new int[26];
        for (int i = 0; i < order.length(); i++) {

            count[order.charAt(i) - 'a'] = i;
        }

        System.out.println(Arrays.toString(count));

        String[] words = { "hello", "leetcode" };
        String ordered = "hlabcdefgijkmnopqrstuvwxyz";

        System.out.println(isAlienSorted(words, ordered));

        // we need to map the xyz to abc how do we do this?

        // what would you do if the alphabet was in order, what would you do if it was
        // shifted about
        // we can simply map the number value to the index
        // s1 s2
        // ["bello","ceetcode"]
        // compare the two
        // b-a = 1 mapping[1] = 3 c-a = 2 mapping[2] = 4
        // 3 < 4 so thats good

        // mapping[s1.charAt(i) - 'a'] > mapping[s2.charAt(i) - 'a'];

        // mapping xyz to abc,
        // []
        // [2, 3, 4, 5, 6, 7, 8, 0, 9, 10, 11, 1, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        // 21, 22, 23, 24, 25]
        // String order = "hlabcdefgijkmnopqrstuvwxyz";

    }

}