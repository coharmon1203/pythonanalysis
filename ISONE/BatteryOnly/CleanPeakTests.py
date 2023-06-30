import pandas as pd
import openpyxl
# Read the excel file called groceries

df = pd.read_excel('UMass Amherst_640_20230601_20240531.xlsx', nrows=8760)

onpeakbyhour = df[["HE", "On Peak Price ($/KW)"]]
cleanpeakbyhour = df[["HE", "Clean Peak Price ($/KW)"]]
onandcleanpeakbyhour = df[["HE", "On Peak Price ($/KW)", "Clean Peak Price ($/KW)"]]

# Scale microgrid sim (FR) Award kW
dd = df["HE"] > 10
print(dd)

print(df.loc[df['On Peak Price ($/KW)'] > 0])
print(df.loc[df['Clean Peak Price ($/KW)'] > 0])

# print(onpeakbyhour.loc[onpeakbyhour['On Peak Price ($/KW)'] > 0])
print(cleanpeakbyhour.loc[cleanpeakbyhour['Clean Peak Price ($/KW)'] > 0])
# print(onandcleanpeakbyhour.loc[onandcleanpeakbyhour['On Peak Price ($/KW)'] > 0])

df = pd.read_excel('UMass Amherst_640_20230601_20240531.xlsx', nrows=8760)
cleanpeakbyhour = df[["HE", "Clean Peak Price ($/KW)"]]

print(cleanpeakbyhour.loc[cleanpeakbyhour['Clean Peak Price ($/KW)'] > 0])