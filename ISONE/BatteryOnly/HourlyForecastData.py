import pandas as pd
import numpy as np
import openpyxl
# Read the excel file called groceries

df = pd.read_excel('UMass Amherst_640_20230601_20240531.xlsx', nrows=8760)

onpeakbyhour = df[["HE", "On Peak Price ($/KW)"]]
cleanpeakbyhour = df[["HE", "Clean Peak Price ($/KW)"]]
onandcleanpeakbyhour = df[["HE", "On Peak Price ($/KW)", "Clean Peak Price ($/KW)"]]
he_byhour = df[["HE", "Load Forecast (kW)"]]
dcmlimit_byday = df[["Schedule Date", "Site Level DCM Limit (KW)"]]
# print(df)


# Scale microgrid sim (FR) Award kW
dd = df["HE"] > 10
print(dd)

aa = np.array(df.loc[df['On Peak Price ($/KW)'] > 0])
print(aa)

print(df.loc[df['On Peak Price ($/KW)'] > 0])
print(df.loc[df['Clean Peak Price ($/KW)'] > 0])

print(onpeakbyhour.loc[onpeakbyhour['On Peak Price ($/KW)'] > 0])
print(cleanpeakbyhour.loc[cleanpeakbyhour['Clean Peak Price ($/KW)'] > 0])
print(onandcleanpeakbyhour.loc[onandcleanpeakbyhour['On Peak Price ($/KW)'] > 0])
print(he_byhour.loc[he_byhour['HE'] == 1])
print(dcmlimit_byday.loc[dcmlimit_byday['Schedule Date'] == '2023-11-11'])