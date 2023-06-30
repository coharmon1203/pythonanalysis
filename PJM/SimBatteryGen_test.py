import unittest
import pandas as pd

class TestStringMethods(unittest.TestCase):

    def test_OnlyBidDAECannotBeMoreThanLoad(self):
        df = pd.read_excel('Scale Microgrid Solutions Operating Bowery Farms_608_20230601_20240531.xlsx', nrows=8760)
        df.fillna(0, inplace=True)

        ddd = df.loc[df['Chanel002_Generator Awarded Market Program'] == "DAE"]
        check_DAE = ddd[["Schedule Date", "HE", "Chanel002_Generator Awarded Market Program", 
                "Chanel002_Generator (DAE) Bid kW"]]

        # 200 kw is the max bid for DAE because the generator is 200 kw
        dddd = check_DAE.loc[check_DAE['Chanel002_Generator (DAE) Bid kW'] > 200]           
        self.assertEqual(len(dddd), 0)

    def test_SRnotDispatched(self):
        df = pd.read_excel('Scale Microgrid Solutions Operating Bowery Farms_608_20230601_20240531.xlsx', nrows=8760)
        df.fillna(0, inplace=True)

        ddd = df.loc[df['Chanel002_Generator Awarded Market Program'] == "SR"]
        check_SR = ddd[["Schedule Date", "HE", "Chanel002_Generator Awarded Market Program", 
                        "Chanel002_Generator Dispatched Market Program"]]

        dddd = check_SR.loc[check_SR['Chanel002_Generator Dispatched Market Program'] != 0]
        self.assertEqual(len(dddd), 0)
  
    def test_checkFRratio(self):
        df = pd.read_excel('Scale Microgrid Solutions Operating Bowery Farms_608_20230601_20240531.xlsx', nrows=8760)
        df.fillna(0, inplace=True)

        ddd = df.loc[df['Channel1002_Battery Awarded Market Program'] == "FR"]

        ddd['FR Ratio'] = ddd['Channel1002_Battery Throughput kWh'] / ddd['Channel1002_Battery (FR) Award kW'] 
        check_FR_w_ratio = ddd[["Schedule Date", "HE", "Channel1002_Battery Awarded Market Program", 
                            "Channel1002_Battery Throughput kWh", "Channel1002_Battery (FR) Award kW", "FR Ratio"]]
        dddd = check_FR_w_ratio.loc[check_FR_w_ratio['FR Ratio'] != .3]
        self.assertEqual(len(dddd), 0)

    def test_OnlyBidDAE_If_StrikePriceLessThanLMP(self):
        df = pd.read_excel('Scale Microgrid Solutions Operating Bowery Farms_608_20230601_20240531.xlsx', nrows=8760)
        df.fillna(0, inplace=True)

        ddd = df.loc[df['Chanel002_Generator Awarded Market Program'] == "DAE"]
        check_DAE = ddd[["Schedule Date", "HE", "Chanel002_Generator Awarded Market Program", 
                        "Chanel002_Generator ECON Strike ($/MW)", "DAE LMP ($/MWh)"]]

        dddd = check_DAE.loc[check_DAE['Chanel002_Generator ECON Strike ($/MW)'] > check_DAE['DAE LMP ($/MWh)']]
        self.assertEqual(len(dddd), 0)

if __name__ == '__main__':
    unittest.main()