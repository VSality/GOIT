
def find_coins_greedy(coins, amount):
    result = {coin: 0 for coin in coins}
    
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount = amount % coin
    
    return {k: v for k, v in result.items() if v > 0}
