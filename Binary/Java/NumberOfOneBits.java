/*

Binary: https://leetcode.com/problems/number-of-1-bits/

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

n & n-1 will remove the right most 1 from n.
(n-1) flips right-most 1 and everything right of that


tip: you can use n & n-1 == 0 to check whether a given number n is a power of 2 because 
all powers of 2 only have a single 1. i.e 

n = 32 = 100000
 &
n-1=31 = 011111
----------------
n&(n-1)= 000000

As you can see n & n-1 removed the right most 1 from n. so you can easily check
if something is a power of 2 by checking if n& n-1 == 0 given a number n.

it follows that you could easily count the number of bits in a number
if you remove the rightmost 1 using n& n-1 and increment a counter everytime you
do so to figure out the number of bits.


*/

public class NumberOfOneBits {


    public static int hammingWeight(int n) {
        
        int count = 0;
        while(n != 0){
            
            n = n & (n-1);
            count++;
        }
        
        return count;
              
        
    }


    public static void main(String[] args){


        System.out.println("Problem: NumberOfOneBits");
        int num = 5;
        int numB = 00000111111001;
        System.out.println(hammingWeight(num));
        System.out.println(hammingWeight(numB));

    }





    
}
