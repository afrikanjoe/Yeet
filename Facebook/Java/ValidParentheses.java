/*
Problem 20: https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false


*/

import java.util.*;

public class ValidParentheses {

    public boolean isValid(String s) {

        Stack<Character> st = new Stack<Character>();
        char[] c = s.toCharArray();

        for (char i : c) {
            if (i == '(') {
                st.push(')');
            } else if (i == '{') {
                st.push('}');
            } else if (i == '[') {
                st.push(']');
            } else if (st.isEmpty() || st.pop() != i) {
                return false;
            }
        }
        return st.isEmpty();
    }

}
