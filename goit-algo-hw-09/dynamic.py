
def find_min_coins(coins, amount):
    
    # Ініціалізація таблиці dp, де dp[i] буде містити мінімальну кількість монет для суми i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    # Ініціалізація таблиці для відстеження вибраних монет
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    result = {coin: 0 for coin in coins}
    while amount > 0:
        coin = coin_used[amount]
        result[coin] += 1
        amount -= coin
    
    result = {k: v for k, v in result.items() if v > 0}

    return result
