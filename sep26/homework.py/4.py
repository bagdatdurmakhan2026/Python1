import pandas as pd
bitcoin_prices = [92000, 95500, 89000, 101000, 98000, 105000, 93000]
def cnt(pr):
    c=[]
    for s in bitcoin_prices:
        if s>95000:
            c.append(s)
    return c
print(cnt(bitcoin_prices))

bitcoin_prices = [92000, 95500, 89000, 101000, 98000, 105000, 93000]
print((lambda pr: [s for s in bitcoin_prices if s > 95000])(bitcoin_prices))