# Import pandas
import pandas as pd
 
# converting to dataframe
data =  pd.read_csv("final_data.csv")

print("-----------------------------------------------------------------------")
print(data)
print("-----------------------------------------------------------------------")
print(data.columns)

print("-----------------------------------------------------------------------")
print(data.describe())
print("-----------------------------------------------------------------------")
print(data.info())
print("-----------------------------------------------------------------------")
print(data.dtypes)
print("-----------------------------------------------------------------------")

from google.colab import files
files.download("final_data.csv")