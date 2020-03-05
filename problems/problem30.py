'''
Blind Curated 75 - Problem 30
=============================

Best Time to Buy and Sell Stock
-------------------------------

Say you have an array for which the _i_<sup>th</sup> element is the price of
some stock on day _i_.

If you were only permitted to complete at most one transaction (i.e., buy and
sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a share of stock before you buy it.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

def solution(prices):
	'''
	Find the highest high which follows the lowest low. Return their difference.
	'''
	max_price = max_profit = float('-inf')
	for price in prices[::-1]:
		if price > max_price:
			max_price = price
		else:
			max_profit = max(max_profit, max_price - price)
	return max(max_profit, 0)
