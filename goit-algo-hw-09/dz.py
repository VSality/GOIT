from greed import find_coins_greedy
from dynamic import find_min_coins

coins = [50, 25, 10, 5, 2, 1]
amount = 113

print(f"greedy alg: {find_coins_greedy(coins, amount)}")
print(f"dynamic alg: {find_min_coins(coins, amount)}")