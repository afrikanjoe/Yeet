/*

https://leetcode.com/problems/find-smallest-letter-greater-than-target/solution/

Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, 
find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.
Which i interpret as if the target is bigger than the last element, return the first element.

Examples:

Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:

letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.


*/


public class FindSmallestLetterGreater {

    // time: O(N) space: O(1)
    public static char nextGreatestLetterBF(char[] letters, char target) {

        for (char c: letters){

            //Since the order is already ascending you can just find the
            // first instance greater than the target.
            if (c > target) return c;
        }


        return letters[0];
        
    }


    //O(logN), where N is the length of letters, O(N) space
    /*
       we want to find something larger than target in a sorted array. 
       This is ideal for a binary search: Let's find the rightmost position to insert target into letters so that it remains sorted.
       At each round, let's maintain the loop invariant that the answer must be in the interval 
       [lo, hi]. If letters[mi] <= target, 
       then we must insert it in the interval [mi + 1, hi]. Otherwise, we must insert it in the interval [lo, mi].
       At the end, if our insertion position says to insert target into the last position letters.length, 
       we return letters[0] instead. This is what the modulo operation does.
     */
    public static char nextGreatestLetterBS(char[] letters, char target) {

        int lo = 0, hi = letters.length - 1;

        while (lo <= hi) {

           int mid = hi + lo >>> 1;
           if (letters[mid] <= target) lo = mid + 1;
           else hi = mid - 1 ;

        }

        return (lo == letters.length) ? letters[0] : letters[lo];
        //return letters[lo % letters.length];
        // b/c all numbers are smaller unless its letters.length % letters.length would we get letters [0] otherwise
        //letters[lo]
        

        
    }

    public static void main(String[] args){



        System.out.println("Problem: Find Smallest Letter Greater than target");
        char[] arrA = {'c', 'f', 'j'};
        System.out.println(nextGreatestLetterBF(arrA, 'f'));
        assert nextGreatestLetterBF(arrA, 'f') == 'j';
        System.out.println(nextGreatestLetterBS(arrA,'j'));
        assert nextGreatestLetterBS(arrA,'j') == 'c';




    }


    



}
