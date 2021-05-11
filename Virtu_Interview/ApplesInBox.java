
/*

1196. How Many Apples Can You Put into the Basket

You have some apples, where arr[i] is the weight of the i-th apple.  
You also have a basket that can carry up to 5000 units of weight.
Return the maximum number of apples you can put in the basket.

Input: arr = [100,200,150,1000]
Output: 4
Explanation: All 4 apples can be carried by the basket since their sum of weights is 1450.

Input: arr = [900,950,800,1000,700,800]
Output: 5
Explanation: The sum of weights of the 6 apples exceeds 5000 so we choose any 5 of them.

1 <= arr.length <= 10^3
1 <= arr[i] <= 10^3



*/
import java.util.*;

public class ApplesInBox {

    public static int numAppleInbox(int[] nums) {

        Arrays.sort(nums);
        int sum = 0;

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (sum > 5000) {
                return i;
            }
        }
        return nums.length;

    }

    public static void main(String[] args) {

        int[] nums = { 100, 200, 150, 1000 };
        System.out.println(numAppleInbox(nums));

    }

}