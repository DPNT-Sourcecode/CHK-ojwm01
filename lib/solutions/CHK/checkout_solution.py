from idlelib.iomenu import errors

import pandas as pd

help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

def get_offer_info(row, key, items):
    offer_for = []
    offer_get = None
    for offer in row:
        if 'for' in offer:
            row_split = offer.split('for')
            num = int(row_split[0].replace(key, ''))
            price = int(row_split[1].strip())
            offer_info = {'offer_num': num, 'offer_price': price}
            offer_for.append(offer_info)
        elif 'get' in offer:
            row_split = offer.split('get')
            offer_num = int(row_split[0].replace(key, ''))
            for item in items:
                if item in row_split[1]:
                   item_free = item
            for k, v in help_dict.items():
                if k in row_split[1]:
                    amount_free = help_dict[k]
            if item_free == key:
                offer_num += 1
            offer_get = {'offer_num': offer_num, 'item_free': item_free, 'amount_free': int(amount_free)}
    return offer_for, offer_get

def get_offer_price(offer_for, offer_amount):
    for offer in offer_for:
        if offer.get('offer_num') == offer_amount:
            offer_price = offer.get('offer_price')
    return offer_price

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    df_stock = pd.DataFrame({'Item': ['A', 'B', 'C', 'D', 'E', 'F'], 'Price': [50, 30, 20, 15, 40, 10], 'Special Offers': ['3A for 130, 5A for 200', '2B for 45', pd.NA, pd.NA, '2E get one B free', '2F get one F free']})
    item_options = df_stock['Item'].to_list()
    remaining = skus
    for item in item_options:
        if item in skus:
            remaining = remaining.replace(item, '')
    if isinstance(skus, str) and remaining == '':
        df_stock['Special Offers'] = df_stock['Special Offers'].apply(lambda x: x.split(', ') if pd.notnull(x) else x)
        df_stock = df_stock.explode('Special Offers')
        df_stock['Get Offer'] = df_stock['Special Offers'].apply(lambda x: 1 if pd.notnull(x) and 'get' in x else 0)
        df_stock.sort_values(by='Get Offer', ascending=False, inplace=True)
        item_counts = {}
        total_price = 0
        for sku in df_stock['Item'].unique():
            item_counts[sku] = skus.count(sku)
        for key in item_counts:
            if item_counts[key] > 0 :
                offer_for= None
                offer_get = None
                df = df_stock[df_stock['Item'] == key]
                count = item_counts.get(key)

                if len(df[~df['Special Offers'].isna()]) > 0 :
                    offer_for, offer_get = get_offer_info(df['Special Offers'], key, df_stock['Item'].to_list())

                if offer_get:
                    if count % offer_get['offer_num'] == 0:
                        item_counts[offer_get['item_free']] -= offer_get['amount_free']*(count/offer_get['offer_num'])
                    else:
                        count_free = count
                        while count_free > offer_get['offer_num']:
                            item_counts[offer_get['item_free']] -= offer_get['amount_free']
                            count_free -= offer_get['offer_num']
                    if item_counts[offer_get['item_free']] < 0:
                        item_counts[offer_get['item_free']] = 0
                    total_price += df['Price'].unique()[0] * item_counts[key]

                elif offer_for:
                    offer_amounts = []
                    for offer in offer_for:
                        offer_amounts.append(offer.get('offer_num'))
                    offer_amounts.sort(reverse=True)
                    for i in range(0, len(offer_amounts)):
                        offer_price = get_offer_price(offer_for, offer_amounts[i])
                        if count % offer_amounts[i] == 0:
                            total_price += offer_price * (count/offer_amounts[i])
                            count = 0
                        else:
                            while count >= offer_amounts[i]:
                                total_price += offer_price
                                count -= offer_amounts[i]
                    total_price += df['Price'].unique()[0] * count
                else:
                    total_price += df['Price'].unique()[0] * count
        return int(total_price)
    else:
        return -1


print(checkout("FFFF"))

