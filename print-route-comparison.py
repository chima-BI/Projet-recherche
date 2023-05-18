import pandas as pd
from tabulate import tabulate
data_Medium=pd.read_json("comparison_Medium.json")
print(tabulate(data_Medium, headers='keys', tablefmt='psql'))

data_High=pd.read_json("comparison_High.json")
print(tabulate(data_High, headers='keys', tablefmt='psql'))

data_Low=pd.read_json("comparison_Low.json")
print(tabulate(data_Low, headers='keys', tablefmt='psql'))


