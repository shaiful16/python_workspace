import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
#print(s);

dates = pd.date_range('20130101', periods=6)
#print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
#print(df)
#print(df.head())
#print(df.index)
#print(df.describe())
#print(df.T)
#print(df.sort_index(axis=1, ascending=False))
#print(df.sort_values(by='B'))
#print(df['A'])
#print(df[0:3])
#print(df.loc[dates[0]])
#print(df.loc[:,['A','B']])
#print(df.loc['20130102':'20130104',['A','B']])
#print(df.loc['20130102',['A','B']])
#print(df.loc[dates[0],'A'])
#print(df.at[dates[0],'A'])
print(df.iloc[3])
print(df.iloc[3:5,0:2])
print(df.iloc[[1,2,4],[0,2]])
print(df.iloc[1:3,:])
print(df.iloc[:,1:3])
print(df.iloc[1,1])
print(df.iat[1,1])
print(df[df.A > 0])
print(df[df > 0])


df3 = df.copy()
df3['E'] = ['one', 'one','two','three','four','three']
print(df3)


df3[df3['E'].isin(['two','four'])]
print(df3)

df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo'})
#print(df2)
#print(df2.dtypes)

