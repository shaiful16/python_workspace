
from pandas import DataFrame, read_csv
import pandas as pd
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

# The inital set of baby names and bith rates
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 76, 578, 973]

BabyDataSet = list(zip(names,births))
print(BabyDataSet)
df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
print(df)
df.to_csv('E:/WorkSpace/python_workspace/datascience/pandasExamples/baby.csv',index=False,header=False)


#read from csv to data frame
df2 = pd.read_csv('E:/WorkSpace/python_workspace/datascience/pandasExamples/baby.csv')
print('my df')
print(df2)






