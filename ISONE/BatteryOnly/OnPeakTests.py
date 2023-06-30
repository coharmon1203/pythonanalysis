import pandas as pd
import openpyxl
# Read the excel file called groceries

df = pd.read_excel('UMass Amherst_640_20230601_20240531.xlsx', nrows=8760)

onpeakbyhour = df[["HE", "On Peak Price ($/KW)"]]
cleanpeakbyhour = df[["HE", "Clean Peak Price ($/KW)"]]
onandcleanpeakbyhour = df[["HE", "On Peak Price ($/KW)", "Clean Peak Price ($/KW)"]]

onpeakhours = onpeakbyhour.loc[onpeakbyhour['On Peak Price ($/KW)'] > 0]
print(df.loc[df['On Peak Price ($/KW)'] > 0])
print(df.loc[df['Clean Peak Price ($/KW)'] > 0])

pd.unique(df['On Peak Price ($/KW)'])
print(onpeakbyhour.loc[onpeakbyhour['On Peak Price ($/KW)'] > 0])
print("No.of.unique values :", pd.unique(onpeakhours['HE']))

cleanpeakbyhour = df[["HE", "Clean Peak Price ($/KW)"]]
cleanpeakhours = cleanpeakbyhour.loc[cleanpeakbyhour['Clean Peak Price ($/KW)'] > 0]
pd.unique(df['Clean Peak Price ($/KW)'])
print(cleanpeakbyhour.loc[cleanpeakbyhour['Clean Peak Price ($/KW)'] > 0])
print("No.of.unique values :", pd.unique(cleanpeakhours['HE']))