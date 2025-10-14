import pandas as pd 

answers_client = pd.read_excel('dataset/client.xlsx')

answers_sellers= pd.read_excel('dataset/vendeur.xlsx')

answers_gender = {
    'Genre_Intérogé ' : ['Femme', 'Homme', 'Femme', 'Homme', 'Homme', 'Homme', 'Femme', 'Homme', 'Homme', 'Homme', 'Homme', 'Homme']
}

df_client = pd.DataFrame(answers_client)
df_sellers = pd.DataFrame(answers_sellers)
df_gender = pd.DataFrame(answers_gender)