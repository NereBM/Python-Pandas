import pandas as pd

########--------------------5:Concatenating and Appending dataframes------------

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])
#simple concatenation, as df1 and df2 have same columns and different indexes
concat = pd.concat([df1,df2])
print(concat)

#here we have missing values
concat = pd.concat([df1,df2,df3])
print(concat)

#we use append to add at the end
df4 = df1.append(df2)
print(df4)

#BUT THIS HAPPENS IF WE APPEND DATA WITH THE SAME INDEX
df4 = df1.append(df3)
print(df4)

#It is important here to introduce the concept of "Series".A series is basically a single-columned dataframe.
#A series does have an index, but, if you convert it to a list, it will be just those values.
#Whenever we say something like df['column'], the return is a series.
s = pd.Series([80,2,50], index=['HPI','Int_rate','US_GDP_Thousands'])
df4 = df1.append(s, ignore_index=True)
print(df1)
print(df4)

#We have to ignore the index when appending a series, because that is the law, unless the series has a name.

#############--------------6:Joining and Merging Dataframes--------------------------

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])
#Here we merge by HPI
print(pd.merge(df1,df3, on='HPI'))

#We can also merge by several columns
print(pd.merge(df1,df2, on=['HPI','Int_rate']))

#Pandas is a great module to marry to a database like mysql? here's why
df4 = pd.merge(df1,df3, on='HPI')
df4.set_index('HPI', inplace=True)
print(df4)
#Now, what if HPI was already the index?
# Or, in our case, We'll probably be joining on the dates,
# but the dates might be the index. In this case, we'd probably use join.
df1.set_index('HPI', inplace=True)
df3.set_index('HPI', inplace=True)
print(df1)
print(df3)

joined = df1.join(df3)
print(joined)


#What happens if we have slightly different indexes?
df1 = pd.DataFrame({
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                    'Year':[2001, 2002, 2003, 2004]
                    })

df3 = pd.DataFrame({
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53],
                    'Year':[2001, 2003, 2004, 2005]})

merged = pd.merge(df1,df3, on='Year')
print(merged)

merged = pd.merge(df1,df3, on='Year')
merged.set_index('Year', inplace=True)
print(merged)

#The parameters that ar not common are missing, how do we solve this? With the "how" parameter of merge:
#Left - equal to left outer join SQL - use keys from left frame only
#Right - right outer join from SQL- use keys from right frame only.
#Outer - full outer join - use union of keys
#Inner - use only intersection of keys.

merged = pd.merge(df1,df3, on='Year', how='left')
merged.set_index('Year', inplace=True)
print(merged)

#Merging on the left is literally on the left dataframe. We had df1, df3,
#  the one on the left is the first one, df1. So, we wound up with an index
# that was identical to the left dataframe (df1).

merged = pd.merge(df1,df3, on='Year', how='outer')
merged.set_index('Year', inplace=True)
print(merged)

#With the "outer" all the indexes are shown
#Finally, "inner" is the intersection of keys, basically just what is shared between all the sets.(It is the defautl option)

#we an do the same with join:
df1.set_index('Year', inplace=True)
df3.set_index('Year', inplace=True)
joined = df1.join(df3, how="outer")
print(joined)