import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Test creating a series
s = pd.Series([5, 10, 15, np.nan, 20])
print s

# Data creation
dates = pd.date_range('20170415', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print df

# Referencing rows of data
print df.head(2) # prints top 2 rows
print df.tail(2) # prints bottom 2 rows

# reference indexing, columns and values
print df.index # returns index values
print df.columns # return column values
print df.values # reutrn value of body data

# transpose and sort data frames
dft = df.T # transpose operation

print df.sort_index(axis=1, ascending=False)
print df.sort_values(by='B')
