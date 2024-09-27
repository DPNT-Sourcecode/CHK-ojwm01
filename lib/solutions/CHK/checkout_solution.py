import pandas as pd


def get_offer_price(row):
    price = row.split('for')
    if price != ['']:
        return int(price[1].strip())
    else:
        return ''
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    df_stock = pd.DataFrame({'Item': ['A', 'B', 'C', 'D'], 'Price': [50, 30, 20, 15], 'Special Offers': ['3A for 130', '2B for 45', '', '']})
    df_stock['Offer Number'] = df_stock['Special Offers'].apply(lambda x: x[:1])
    df_stock['Offer Price'] = df_stock['Special Offers'].apply(lambda x: get_offer_price(x))

    total_price = 0
    items = skus.split(',')
    for item in skus:
        df = df_stock[df_stock['Item'] == item]


    df_stock


checkout('A, B')




