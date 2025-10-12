import pandas as pd 

answers_client = pd.read_excel('dataset/client.xlsx')

answers_sellers= pd.read_excel('dataset/vendeur.xlsx')

df_client = pd.DataFrame(answers_client)
df_sellers = pd.DataFrame(answers_sellers)
