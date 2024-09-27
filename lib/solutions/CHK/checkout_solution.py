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


    items = skus.split(', ')
    items = [item.strip() for item in items]
    item_counts = {}
    total_price = 0
    for sku in df_stock['Item'].unique():
        item_counts[sku] = items.count(sku)
    for item in items:
        df = df_stock[df_stock['Item'] == item]
        count = item_counts.get(item)
        if count == df['Offer Number'].iloc[0]:
            total_price += df['Offer Number'].iloc[0]
        else:
            total_price += df['Price'].iloc[0] * count




    df_stock


checkout('A, B')







