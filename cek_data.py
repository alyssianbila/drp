import pandas as pd

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

print ("\n JUMLAH DATA DAN KOLOM")
print(df.shape)

print("\n 5 DATA TERATAS")
print(df.head()) 
  
# cek kesehatan data
print("\n INFO DATA")
df.info() 

print("\n JUMLAH DATA YANG KOSOSNG")
print(df.isna().sum())

# cek duplikat
print("\n CEK DATA DUPLIKAT")
print("jumlah data duplicated",df.duplicated().sum())

# penulisan
print("\n CEK PENULISAN DATA KATEGORI")
for col in ["Gender", "Occupation", "BMI Category", "Sleep Disorder"]:
    print(f"\n-- {col} --")
    print(df[col].value_counts(dropna=False))

# cek semua kolom int atau float
print("\n CEK KOLOM INT ATAU FLOAT")
print(df.describe())
