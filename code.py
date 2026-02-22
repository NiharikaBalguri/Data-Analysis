import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/crime_data.csv")


df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year


print("Total Crimes:", len(df))


print("\nMost Common Crime Type:")
print(df['Crime_Type'].value_counts())


print("\nCrime by City:")
print(df['City'].value_counts())

yearly_crime = df.groupby('Year').size()

yearly_crime.plot(kind='bar')
plt.title("Crime Trend by Year")
plt.xlabel("Year")
plt.ylabel("Number of Crimes")
plt.show()
