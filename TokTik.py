import pandas as pd
df = pd.read_csv('tiktok_dataset.csv')
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

print(df.info())