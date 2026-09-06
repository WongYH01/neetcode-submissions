class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # biggest profit var
        # smallest buy price var
        # iterate through the price list with i stopping at len-2
            # smallest buy price = min(curr smallest and curr elem)
            # biggest profit = max(curr biggest and the minus)
        # return max(0, biggest proft)
        biggest_profit = 0
        smallest_buy_price = 101

        for i in range(0,len(prices)):
            smallest_buy_price = min(smallest_buy_price,prices[i])
            biggest_profit = max(biggest_profit,prices[i]-smallest_buy_price)
        
        return max(0,biggest_profit)

            
            
            

        