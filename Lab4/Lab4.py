import pandas as pd

df1= pd.read_csv('date_climatice_2016.csv')
df1.pop("LAT")
df1.pop("LON")
df1.pop("R24")
print(df1)

df1=df1.astype({
    "DATCLIM" : "datetime64[ns]",
    "CODST" : "category"
})
df1.info()
df2= pd.read_csv('statii_meteo.csv')

df2= df2.rename(columns={"ID": "CODST", "Nume": "NUME"})
df2= df2.merge(df1,on="CODST")
print(df2)

mean_TMED = df1["TMED"].mean()
print(mean_TMED)
max_TMAX= df1["TMAX"].max()
print(max_TMAX)
min_TMIN= df1["TMIN"].min()
print(min_TMIN)
df1.query()