/*

https://leetcode.com/problems/find-the-duplicate-number/solution/

Essentially the same as contains duplicate

given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

Can you solve the problem using only constant, O(1) extra space?

Floyd's Tortoise and Hare (Cycle Detection)




*/


public class FindDuplicate {
    
    
    //O(N)time & O(N)space
    public int findDuplicate(int[] nums) {
        
        HashSet<Integer> hs = new HashSet<>();
        
        for(int i: nums){
            if(hs.add(i) == false) return i;
        }
        return -1;
        
    }

    public int findDuplicateTortandHare(int []nums){




        


        return -1;
    }






    
}
