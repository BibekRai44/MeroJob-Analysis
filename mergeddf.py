import pandas as pd
df1=pd.read_csv('Jobs.csv')
df2=pd.read_csv('new_data.csv')
data=pd.concat([df1,df2],axis=1)
data.to_csv('mergeddata.csv',index=False)