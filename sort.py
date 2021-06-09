import pandas as pd

df = pd.read_csv('table.csv', delimiter=',')
df = df.sort_values(['region code', 'code of the territorial agency'], ascending=[True, True]) # True - сортирует в порядке возрастания, False - наоборот
df.to_csv('sorted.csv', index=False)