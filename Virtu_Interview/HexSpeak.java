/*

A decimal number can be converted to its Hexspeak representation by first converting it to 
an uppercase hexadecimal string, then replacing all occurrences of the digit 0 with the letter O, 
and the digit 1 with the letter I. Such a representation is valid if and only if 
it consists only of the letters in the set {"A", "B", "C", "D", "E", "F", "I", "O"}.

Given a string num representing a decimal integer N, return the Hexspeak representation 
of N if it is valid, otherwise return "ERROR".


Example 1:
Input: num = “257”
Output: “IOI”

Explanation: 257 is 101 in hexadecimal.

Example 2:
Input: num = “3”
Output: “ERROR”

Constraints:

1 <= N <= 10^12
There are no leading zeros in the given string.
All answers must be in uppercase letters.


*/

public class HexSpeak {


    public static String toHexspeak(String num){

        String validStr = "ABCDEFIO";

        int number = Integer.parseInt(num);

        String hex = Integer.toHexString(number);

        hex = hex.toUpperCase();
        hex = hex.replaceAll("0", "O");
        hex = hex.replaceAll("1","I");

        char[] hexArray = hex.toCharArray();
        for(char c: hexArray){
            if(validStr.indexOf(c)< (0)){
                return "ERROR";
            }
        }
        return hex;

    }





    public static void main(String[] args){
        String num = "3";

        System.out.println(toHexspeak(num));

        //Output: “IOI”
        //Input: num = “3”
        //Output: “ERROR”





    }
    
}
