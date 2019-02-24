import pandas as pd
#import Quandl


#Quandl.ApiConfig.api_key = 'NuLxqGMfc1sYn1-jAbro'
#df = Quandl.get('FMAC/30US')

df = pd.read_csv("datasets\\FMAC_metadata.csv", index_col=4)
print(df)

#this returns a list of data frames
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')


pd.set_option('display.max_columns', None)#To display all the columns in the output window

#so this is a list
print(type(fiddy_states))
print(len(fiddy_states))

#this is a dataframe
print(type(fiddy_states[0]))
print(len(fiddy_states[0]))
print(fiddy_states[0])
print(fiddy_states[0].columns)
states_df = fiddy_states[0]
states_df.rename(columns={'Name &postal abbreviation[1].1':'Abbr'}, inplace=True)
print(states_df.columns)
print(states_df)
print(states_df['Name &postal abbreviation[1]']['Abbr'])


