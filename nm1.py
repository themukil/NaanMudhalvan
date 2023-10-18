import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Read the data from the csv file
data = pd.read_csv("statsfinal.csv")
print("Info of the data:\n")
print(data.info())
print()

#Data cleaning
#1) identifying missing values
missing_values = data.isnull().sum()
print(missing_values)
print("There is no missing values")

#2)Drop rows with missing values
data.dropna(inplace=True)

#3)Remove duplicates
data.drop_duplicates(inplace=True)
#drop the column unnamed because it resembles the column index
data = data.drop(columns=['Unnamed: 0'])

#data formatting
# Instead of formatting , Separate the date into separate columns
data['Day'] = data['Date'].apply(lambda x: x.split('-')[0])
data['Month'] = data['Date'].apply(lambda x: x.split('-')[1])
data['Year'] = data['Date'].apply(lambda x: x.split('-')[2])


#Data Reduction
#We remove 2010 and 2023 because it has insufficient data
data_reduced = data.query("Year != '2010' and Year != '2023'")

remove_date = []

for i in range(11,23):
    remove_date.append('31-9-20'+str(i))
    remove_date.append('31-11-20'+str(i))

print(remove_date)

#These are incorrect dates so we remove them
data_reduced = data_reduced[~data_reduced['Date'].isin(remove_date)]

print("\nDataset after cleaning and processing\n")
print(data_reduced)
