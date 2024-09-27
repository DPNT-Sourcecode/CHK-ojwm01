import pandas as pd

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    df_stock = pd.DataFrame({'Item': ['A', 'B', 'C', 'D'], 'Price': [50, 30, 20, 15], 'Special Offers': ['3A for 130', '2B for 45', '', '']})
    df_stock['Offer Number'] = df_stock['Special Offers'].apply(lambda x: x[:1])
    df_stock['Offer Price'] = df_stock['Special Offers'].apply(lambda x: x.split('for')[1] if x.split('for') != '')
    df_stock


checkout('A, B')


