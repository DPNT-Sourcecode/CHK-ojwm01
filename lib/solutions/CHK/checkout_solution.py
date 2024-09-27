import pandas as pd


def get_offer_info(row):
    return row.split('for')[0].strip(), int(row.split('for')[1].strip())
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    df_stock = pd.DataFrame({'Item': ['A', 'B', 'C', 'D'], 'Price': [50, 30, 20, 15], 'Special Offers': ['3A for 130', '2B for 45', '', '']})
    # df_stock['Offer Number'] = df_stock['Special Offers'].apply(lambda x: x[:1])
    # df_stock['Offer Price'] = df_stock['Special Offers'].apply(lambda x: get_offer_price(x))


    # items = skus.split(', ')
    # items = [item.strip() for item in items]
    item_counts = {}
    total_price = 0
    for sku in df_stock['Item'].unique():
        item_counts[sku] = skus.count(sku)
    for key in item_counts:
        df = df_stock[df_stock['Item'] == key]
        count = item_counts.get(key)
        if len(df[~df['Special Offers'].isna()]) > 0 :
            offer_num, offer_price = get_offer_info(df['Special Offers'].iloc[0])
        if count == int(df['Offer Number'].iloc[0]):
            total_price += df['Offer Price'].iloc[0]
        else:
            total_price += df['Price'].iloc[0] * count




    df_stock


checkout('A, B, A, A')


