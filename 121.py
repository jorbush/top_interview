"""
You are given an array prices where prices[i] is the price
of a given stock on the ith day.

You want to maximize your profit by choosing a single day to
buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If
you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed
because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # return max_profit(prices, 0, float('inf'), 0, False)
    return max_profit_recursive(prices[1:], prices[0], 0, 0)


def max_profit_recursive(prices, buy, profit, ind):
    if ind == len(prices):
        return profit
    sell = prices[ind]
    new_profit = sell - buy
    if new_profit > profit:
        profit = new_profit
    if sell < buy:
        buy = sell
    # print(f'{sell} {buy} {profit}')
    return max_profit_recursive(prices, buy, profit, ind + 1)


def max_profit_x(prices):
    if len(prices) < 2:
        return 0
    min_buy = min(prices[:-1])
    min_buy_index = prices.index(min_buy)
    max_sell = max(prices[1:])
    max_buy_index = prices.index(min_buy)
    valid = max_buy_index > min_buy_index
    if valid:
        profit = max_sell - min_buy
    else:
        new_min_buy = min(prices[:max_buy_index])
        min_ind_profit = max_sell - new_min_buy
        new_max_sell = max(prices[min_buy_index:])
        max_ind_profit = new_max_sell - min_buy
        profit = max(min_ind_profit, max_ind_profit)
        valid = prices.index(new_max_sell) > prices.index(min_buy) if profit == max_ind_profit else prices.index(
            max_sell) > prices.index(new_min_buy)
        profit = profit if valid else 0
    return profit if profit > 0 else 0


def max_profit(prices, ind, min_buy, max_sell, bought):
    if ind == len(prices):
        return max_sell - min_buy if min_buy != float('inf') and max_sell != 0 else 0
    current_price = prices[ind]
    if not bought:
        if current_price < min_buy and max_sell == 0:
            min_buy = current_price
        else:
            max_sell = current_price
            bought = True
    else:
        if current_price > max_sell and bought:
            max_sell = current_price
    return max_profit(prices, ind + 1, min_buy, max_sell, bought)


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    prices_f = [2, 1, 2, 1, 0, 1, 2]
    prices_f_2 = [3, 2, 6, 5, 0, 3]
    prices_0 = [7, 6, 4, 3, 1]
    print(maxProfit(prices))
