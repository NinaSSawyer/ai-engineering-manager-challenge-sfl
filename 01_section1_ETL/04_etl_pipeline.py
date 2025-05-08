import pandas as pd
df = pd.read_excel('E:\HDD Docs\Career Stuff\Deloitte\DEM_Challenge_Section1_DATASET.xlsx')
print("\n📋 First 5 rows:")
print(df.head())

print("\n🔍 Column Info:")
print(df.info())

print("\n🧼 Any Nulls?")
print(df.isnull().sum())