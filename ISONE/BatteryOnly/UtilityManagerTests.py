import pandas as pd
import openpyxl
# Read the excel file called groceries


df = pd.read_excel('UMass Amherst_640_20230601_20240531.xlsx', nrows=8760)
df.fillna(0, inplace=True)
df['Battery Drop (kW)'] = df['New BESS SOC'].shift(1) - df['New BESS SOC'] 



onpeakbyhour = df[["HE", "On Peak Price ($/KW)"]]
cleanpeakbyhour = df[["HE", "Clean Peak Price ($/KW)"]]
onandcleanpeakbyhour = df[["HE", "On Peak Price ($/KW)", "Clean Peak Price ($/KW)"]]
he_byhour = df[["HE", "Load Forecast (kW)"]]
dcmlimit_byday = df[["Schedule Date", "Site Level DCM Limit (KW)"]]
check_charge = df[["Schedule Date", "HE", "New BESS SOC", "New BESS Throughput kWh", "Battery Drop (kW)"]]
# print(df)

# Scale microgrid sim (FR) Award kW
dd = df["HE"] > 10
print(dd)

print(df.loc[df['On Peak Price ($/KW)'] > 0])
print(df.loc[df['Clean Peak Price ($/KW)'] > 0])

# print(onpeakbyhour.loc[onpeakbyhour['On Peak Price ($/KW)'] > 0])
# print(cleanpeakbyhour.loc[cleanpeakbyhour['Clean Peak Price ($/KW)'] > 0])
# print(onandcleanpeakbyhour.loc[onandcleanpeakbyhour['On Peak Price ($/KW)'] > 0])
# print(he_byhour.loc[he_byhour['HE'] == 1])
# print(dcmlimit_byday.loc[dcmlimit_byday['Schedule Date'] == '2023-11-11'])

print(check_charge.loc[check_charge['New BESS Throughput kWh'] != 0.0])

ddd = check_charge.loc[check_charge['New BESS Throughput kWh'] != 0.0]

f = ddd["Battery Drop (kW)"].min()
n = pd.unique(ddd['Battery Drop (kW)'])

  
print("No.of.unique values :", n)
print("Min value :", f)

# Is the first date of the simulation the same as the first date of the excel file?




# Logistical - SOC 

# Calculating perceived revenue correctly
# Optimization financials