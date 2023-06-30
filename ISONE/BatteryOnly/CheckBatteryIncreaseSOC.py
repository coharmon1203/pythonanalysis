import pandas as pd

df = pd.read_excel('UMass Amherst_640_20230601_20240531.xlsx', nrows=8760)
df.fillna(0, inplace=True)
df['Battery Increase (kW)'] = df['New BESS SOC'] - df['New BESS SOC'].shift(1)

check_charge = df[["Schedule Date", "HE", "New BESS SOC", "New BESS Charge kW", "Battery Increase (kW)"]]

ddd = check_charge.loc[check_charge['New BESS Charge kW'] < -20.0]
  
print(check_charge.loc[check_charge['New BESS Charge kW'] < -20.0])

print("No.of.unique values :", pd.unique(ddd['Battery Increase (kW)']))
print("Min value :", ddd["Battery Increase (kW)"].min())
