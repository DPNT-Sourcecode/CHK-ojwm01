import pandas as pd


def get_offer_info(row, key):
    split = row.split('for')
    num = int(split[0].replace(key, ''))
    price = int(split[1].strip())
    return num, price

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    df_stock = pd.DataFrame({'Item': ['A', 'B', 'C', 'D'], 'Price': [50, 30, 20, 15], 'Special Offers': ['3A for 130', '2B for 45', pd.NA, pd.NA]})
    item_options = df_stock['Item'].to_list()
    remaining = skus
    for item in item_options:
        if item in skus:
            remaining = remaining.replace(item, '')
    if isinstance(skus, str) and remaining == '':
        item_counts = {}
        total_price = 0
        for sku in df_stock['Item'].unique():
            item_counts[sku] = skus.count(sku)
        for key in item_counts:
            df = df_stock[df_stock['Item'] == key]
            count = item_counts.get(key)
            if len(df[~df['Special Offers'].isna()]) > 0 :
                offer_num, offer_price = get_offer_info(df['Special Offers'].iloc[0], key)
            if offer_num:
                if count % offer_num == 0:
                    total_price += offer_price * (count/offer_num)
                else:
                    while count > offer_num:
                        total_price += offer_price
                        count -= offer_num
                    total_price += df['Price'].iloc[0] * count
            else:
                total_price += df['Price'].iloc[0] * count
        return int(total_price)
    else:
        return -1


print(checkout('A,B,C,D'))