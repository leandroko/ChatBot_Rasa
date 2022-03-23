import pandas as pd
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(BASE_DIR + '\\actions\\unidadesaude.csv', sep=';')
df = df.dropna()
dfpr = df[df['ESTADO'] == 'PR']
dfpr = dfpr[dfpr['CIDADE'] == 'Curitiba']

resultado = dfpr.head(5).values.tolist()

dfpr2 = dfpr.reset_index(drop=True).head(5)



cid = 'londrina'
cid.capitalize()
