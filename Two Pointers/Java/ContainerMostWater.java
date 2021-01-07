/*

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

https://leetcode.com/problems/container-with-most-water/


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above are vertical lines are represented by array 
[1,8,6,2,5,4,8,3,7]. In this case, 
the max area of water (blue section) the container can contain is 49.


Logic:

Start with pointer left=0 and pointer right=length-1
The max water is limited by the pointer with smaller height
When moving a pointer, the width of the area decrease
If we move the pointer with higher height, we will never get a
greater area, the max height will be at most the one of the pointer with smaller height.
So we need to move the pointer with smaller height to have a chance to get higher height at the next step.

*/

public class ContainerMostWater {


    //O(N) time O(1) space
    public static int maxArea(int[] height) {

        int i = 0;
        int j = height.length - 1;
        int maxArea = 0;

        while (i <= j) {

            int h = Math.min(height[i], height[j]);
            int w = j - i;

            if (height[i] < height[j]) {
                maxArea = Math.max(maxArea, h * w);
                i++;
            } else {
                maxArea = Math.max(maxArea, h * w);
                j--;
            }

        }
        return maxArea;

    }

    public static void main(String[] args) {

        int[] arrA = { 1, 8, 6, 2, 5, 4, 8, 3, 7 };

        System.out.println("Contains most water");
        System.out.println(maxArea(arrA));

    }

}
