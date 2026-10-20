class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = -1
        max_profit = 0
        for current_price in prices:
            if buy_price == -1 or current_price < buy_price:
                buy_price = current_price
            elif (current_price - buy_price) > max_profit:
                max_profit = current_price - buy_price
        return max_profit