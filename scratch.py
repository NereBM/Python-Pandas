import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
#import quandl
style.use("ggplot")

#quandl.ApiConfig.api_key = 'NuLxqGMfc1sYn1-jAbro'
#house_index_df = quandl.get('NASDAQOMX/XQC')

#######-----------------------2:PANDAS BASICS-------------------------#######

#A dictionaty is created
web_stats ={'Day':[1,2,3,4,5,6],
            'Visitors':[43,53,34,45,64,34],
            'Bounce_Rate': [65,72,62,64,54,66]
            }

#Now we convert the dictionary to a data frame with pandas:
df = pd.DataFrame(web_stats)
#print the whole data frame
print(df)

#print the first 2 elements
print(df.head(2))

#print the last 2 elements
print(df.tail(2))

#You can set the index of your dataframe to be any of the columns, it depends on what you want to analyze
print(df.set_index('Day'))

#This does not modify the original df, so if we want to work with it we need t ostore it somewhere
df2 = df.set_index('Day')

#Or, to modify the original df we can use:
df.set_index('Day', inplace=True)

#To reference a column
print(df.Visitors)
print(df['Bounce_Rate'])#If the column name contains spaces we have to do it like this
print(df[['Visitors', 'Bounce_Rate']])

#Convert it to a list:
print(df.Visitors.tolist())

#We cannot convert two columns at the same time to a list with pandas, so we use numpy:
print(np.array(df[['Visitors','Bounce_Rate']]))


#and if you have a list you can convert it to a data frame also:
df2= pd.DataFrame(np.array(df[['Visitors','Bounce_Rate']]))
print(df2)

