/*

https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

Count Substrings with Only One Distinct Letter

Given a string S, return the number of substrings that have only one distinct letter.

Input: S = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.


Input: S = "aaaaaaaaaa"
Output: 55

1 <= S.length <= 1000
S[i] consists of only lowercase English letters.

*/


public class SubstringDistinctChar {




    public static int countSubstringWithDistinct(String s){

        int count = 0;
        int consecutive = 1;

        for (int i= 1; i < s.length(); i++){
            if(s.charAt(i) == s.charAt(i -1)){
                consecutive++;
            }else{
                count +=calculate(consecutive);
                consecutive = 1;
            }
        }

        count += calculate(consecutive);

        return count;
    }

    private static int calculate(int n){

        return n * (n + 1)/2;
    }

    public static void main(String[] args){


        String s = "aaaba";
        System.out.println(countSubstringWithDistinct(s));

    }



    
}


/*

 int count = 0;
        int length = S.length();
        int consecutive = 0;
        char prevChar = '0';
        for (int i = 0; i < length; i++) {
            char c = S.charAt(i);
            if (c == prevChar)
                consecutive++;
            else {
                count += consecutive * (consecutive + 1) / 2;
                consecutive = 1;
            }
            prevChar = c;
        }
        if (consecutive > 0)
            count += consecutive * (consecutive + 1) / 2;
        return count;
    }



*/
