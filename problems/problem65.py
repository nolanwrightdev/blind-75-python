'''
Blind Curated 75 - Problem 65
=============================

Coin Change
-----------

Given different denominations of coins which are available and a total amount of
change needed, find the smallest number of coins that is required to make up the
change. If there is no combination of coins which can make up the change, return
`-1`.

[→ LeetCode][1]

[1]: https://leetcode.com/problems/coin-change/
'''

import math

def solution(coins, amount):
	'''
	This is a bottom-up dynamic programming solution. From `0` to `amount`, in
	increments of the largest viable coin denomination, calculate the smallest
	number of coins required to make change for that number. The number of coins
	for subsequent numbers can be derived from those already calculated.
	'''
	coins.sort()
	while coins and coins[-1] > amount:
		coins.pop()

	if not coins:
		return -1 if amount else 0

	mc = coins[-1]
	if amount % mc == 0:
		return amount // mc

	previous = [float('inf')] * mc
	current = [0] + [float('inf')] * (mc - 1)
	for _ in range(math.ceil(amount / mc)):
		for i in range(mc):
			for coin in coins:
				ind = i - coin
				val = current[ind] if ind >= 0 else previous[ind]
				current[i] = min(current[i], val + 1)
		previous, current = current, [float('inf')] * mc
	num_coins = previous[amount % mc]
	return -1 if num_coins == float('inf') else num_coins
