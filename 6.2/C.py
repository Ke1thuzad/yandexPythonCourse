import pandas as pd


def cheque(prices: pd.Series, **products):
    res = {'product': [], 'price': [], 'number': [], 'cost': []}
    for label, amount in sorted(products.items(), key=lambda x: x[0]):
        res['product'].append(label)
        res['price'].append(prices[label])
        res['number'].append(amount)
        res['cost'].append(amount * prices[label])
    price_list = pd.DataFrame(res)

    return price_list
