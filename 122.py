"""
You are given an integer array prices where prices[i] is the price
of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can
only hold at most one share of the stock at any time. However, you
can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy
the stock to achieve the maximum profit of 0.


Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
"""


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    return max_profit(prices[1:], prices[0], 0, 0, list())


def max_profit(prices, buy, profit, ind, profits):
    if ind == len(prices):
        return sum(profits)
    sell = prices[ind]
    new_profit = sell - buy
    # print(f'{new_profit} {profit}')
    if new_profit < profit and profit > 0:
        profits.append(profit)
        buy = sell
        profit = 0
    else:
        if (ind == len(prices) - 1) and new_profit > 0:
            profits.append(new_profit)
        if new_profit > profit:
            profit = new_profit
        if sell < buy:
            buy = sell
    # print(f'{buy} {sell} {profits}')
    return max_profit(prices, buy, profit, ind + 1, profits)


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))
