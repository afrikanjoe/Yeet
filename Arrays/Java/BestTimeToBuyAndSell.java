/*

Problem should be called, best time to have bought
and sold a stock in the past lmao.


https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
*/

public class BestTimeToBuyAndSell{

    public static void main(String[] Args) {

        System.out.println("Problem: Find Max Profit");
        int[] arrayA = {7,1,5,3,6,4};

        System.out.println(maxProfit(arrayA));

    }

    public static int maxProfit(int[] prices) {
        
        
        int maxProf = 0;
        
        if (prices.length == 0) return maxProf;
        
        int buyAtPrice = prices[0];
        int profit = 0;
        
        for (int i = 1; i < prices.length; i++){
            if(buyAtPrice < prices[i]){
                profit = prices[i] - buyAtPrice;
                maxProf = Math.max(profit,maxProf);       
            }else{
                buyAtPrice = prices[i];
            }
            
        }
        
        return maxProf;
        
        
        
    }
}