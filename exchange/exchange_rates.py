# BTC => base
# USD => quote
# Bid => price base defined in quote (1 BTC = 990 USD)
# Ask => price quote in 1/ask (ie 1 USD = 1/1000)

# Input currency: USD in example
# Target currency: EUR in example
# I have USD, exchange for EUR
# 5000 USD => 5000 /1000 (ask) = x => BTC => x * bid (1150) => EUR
# 5000 USD => 5000/200 (ask) = x  => ETH => x * bid (210) => EUR
# 1 USD => 0.001 * 1150 => 1.15
# 1 USD => 0.005 * 210 => 1.05

# [(USD, BTC), (ETH, BTC), (USD, ETH), (ETH,EUR), ()]
# [BTC-USD, bid, ask],
# [BTC-EUR, bid, ask]
# ETH-USD
# ETH-EUR
# {
# 	BTC-USD: {bid: 1150, ask: 200},
# }
# {
#   'USD': [{'currency': 'BTC', 'price': 1/1000}, {'currency': 'ETH', 'price': 1/180}],
#   'BTC': [{'currency': 'EUR', 'price': 1200}, {'currency': 'USD', 'price': 220}],
# }
# if quote => 1/ask
# if base => bid
# source = USD
# target = EUR

from collections import defaultdict

currencies = [('BTC-USD', 1000, 990), ('BTC-EUR', 1200, 1150), ('ETH-USD', 200, 180), ('ETH-EUR', 220, 210)]

currency_mapping = defaultdict(list)
for currency_pair in currencies:
    base, quote = currency_pair[0].split('-')
    ask = currency_pair[1]
    bid = currency_pair[2]

    currency_mapping[base].append({'currency': quote, 'price': bid})
    currency_mapping[quote].append({'currency': base, 'price': 1/ask})



def get_best_conversion_rate(source, target, value):
    visited = set() # set of visited currencies
    results = []

    def dfs(currency, target, value, price, path):
        source_currency = currency
        path = path[:]
        value = value * price

        if currency == target:
            results.append((path, value))
            return

        for currency in currency_mapping[source_currency]:
            if currency['currency'] in visited:
                continue
            path.append(currency['currency'])
            visited.add(currency['currency'])

            dfs(currency['currency'], target, value, currency['price'], path)
            visited.remove(currency['currency'])
            path.pop()

    visited.add(source)
    dfs(source, target, value, 1, [source])

    return max(results, key=lambda x: x[1])

if __name__ == '__main__':
    print(get_best_conversion_rate('USD', 'EUR', 1))
    # assert(get_best_conversion_rate('USD', 'EUR', 1) == (['USD', 'BTC', 'EUR'], 1.15))
