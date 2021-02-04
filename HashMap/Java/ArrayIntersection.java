/*
https://leetcode.com/problems/intersection-of-two-arrays/


Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.



*/

import java.util.*;

public class ArrayIntersection {

    public static int[] intersection(int[] nums1, int[] nums2) {

        HashSet<Integer> nums1set = new HashSet<>();
        HashSet<Integer> intersectionSet = new HashSet<>();

        for (int num : nums1)
            nums1set.add(num);

        for (int num : nums2) {

            if (nums1set.contains(num))
                intersectionSet.add(num);
        }

        int[] result = new int[intersectionSet.size()];

        int i = 0;
        for (int num : intersectionSet) {
            result[i++] = num;
        }

        return result;

    }

    public static void main(String[] args) {

        int[] nums1 = { 4, 9, 5 };
        int[] nums2 = { 9, 4, 9, 8, 4 };

        int[] intersect = intersection(nums1, nums2);

        System.out.println(Arrays.toString(intersect));

    }
}
