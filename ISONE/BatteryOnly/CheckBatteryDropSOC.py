import pandas as pd

df = pd.read_excel('UMass Amherst_640_20230601_20240531.xlsx', nrows=8760)
df.fillna(0, inplace=True)
df['Battery Drop (kW)'] = df['New BESS SOC'].shift(1) - df['New BESS SOC'] 

check_charge = df[["Schedule Date", "HE", "New BESS SOC", "New BESS Throughput kWh", "Battery Drop (kW)"]]

ddd = check_charge.loc[check_charge['New BESS Throughput kWh'] != 0.0]
  
print("No.of.unique values :", pd.unique(ddd['Battery Drop (kW)']))
print("Min value :", ddd["Battery Drop (kW)"].min())
