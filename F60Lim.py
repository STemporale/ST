# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt

ST1 = pd.read_csv('F60Lim.csv', sep = ';', parse_dates = [1], infer_datetime_format = True, dayfirst = True)
ST1.index = pd.to_datetime(ST1['FyH'])
ST1['Eq'] = pd.to_numeric(ST1['Equity'])
del ST1['FyH']
del ST1['Equity']
ST1['Incr'] = ST1['Eq'].pct_change()
ST1 = ST1.drop(ST1['Incr' == 0])
ST1['Incr2'] = ST1['Incr'].shift(-1)
ST1['Peak'] = (ST1['Incr'] * ST1['Incr2']) < 0
ST1.plot(subplots = True, figsize = (12, 10), title = 'Equity')
ST2 = ST1[(ST1.Peak == True)]
ST2['EqAnt'] = ST2['Eq'].shift(1)
ST2['FyH'] = ST2.index
ST2['FyHAnt'] = ST2['FyH'].shift(1)
ST2['Lapso'] = ST2['FyH'] - ST2['FyHAnt']
ST2['GyP'] = ST2['Eq'] - ST2['EqAnt']
ST2
ST2.to_csv('F60Lim2.csv', sep = ";")
