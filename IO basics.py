import pandas as pd

#######-----------------------3:IO BASICS-------------------------#######
#https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

chocolate_df = pd.read_csv("chocolate-bars.csv")

chocolate_df.set_index('RowNum',inplace=True)

#Or we can directly specify the index when we read it
chocolate_df2 = pd.read_csv("chocolate-bars.csv", index_col = 0)
print(chocolate_df2)

#If we want to save data in a csv
#chocolate_df.to_csv("chocolate-bars.csv")
#Or if we want it withou headers
chocolate_df.to_csv("chocolate-bars_NOHEADERS.csv", header=False)

#And we can read the file without header and add names for them:
chocolate_df3 = pd.read_csv("chocolate-bars_NOHEADERS.csv", names = ['ID','Company','Name', 'Ref','Review.Date','Cocoa.Percent','Company.Location','Rating','Broad.Bean.Origin','Bean.Type'], index_col=0)
print(chocolate_df3)

#if we wanna rename only one/some particular columns
chocolate_df3.rename(columns = {'Review.Date':'Review_Date', 'Cocoa.Percent':'Cocoa_Percent'},inplace=True)
print(chocolate_df3.Review_Date)



