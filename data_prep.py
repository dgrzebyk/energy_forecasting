import os
import pandas as pd

cwd = os.path.abspath('C:\\Users\\danie\\PycharmProjects\\internalProject\\data\\SolarForecast')
files = os.listdir(cwd)

files_ls = []
for file in files:
    if file.endswith('.xls'):
        df_from_excel = pd.read_excel(cwd + f'\\{file}', header=3)
        files_ls.append(df_from_excel)
df = pd.concat(files_ls)

df.to_csv(cwd + '\\solar_forecast_2021.csv', index=False)
