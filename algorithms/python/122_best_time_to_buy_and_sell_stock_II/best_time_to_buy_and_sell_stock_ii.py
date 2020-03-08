# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii

@Problem:
    Say you have an array for which the ith element is the price of a given stock on day i.
    Design an algorithm to find the maximum profit. 
    You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
    Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

@Example 1:
    Input: [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
                 Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
@Example 2:
    Input: [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
                 Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
                 engaging multiple transactions at the same time. You must sell before buying again.
@Example 3:
    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution(object):

    def maxProfit(self, prices):
        """
        we can also using DP
        dp_0[i]: up to date[i], if we do not rest stock, max profit we can get
        dp_1[i]: up to date[i], if we rest stock, max profit we can get
        #init:
            dp_0[-1] = 0
            dp_1[-1] = -inf  # impossible
        #state transform:
            dp_0[i+1] = max(dp_0[i], dp_1[i] + prices[i])  # if rest now, must sell it for next buying
            dp_1[i+1] = max(dp_1[i], dp_1[i] - prices[i])
        # complexity:
            time: O(n)
            space: O(1)
        """
        dp_0 = 0
        dp_1 = float('-inf')
        for i in range(len(prices)):
            tmp = dp_0
            dp_0 = max(dp_0, dp_1 + prices[i])
            dp_1 = max(dp_1, tmp - prices[i])
        return dp_0

if __name__ == "__main__":
    so = Solution()
    arr = [7,1,5,3,6,4]
    arr = [1,2,3,4,5]
    arr = [7,6,4,3,1]
    res = so.maxProfit(arr)
    print res
