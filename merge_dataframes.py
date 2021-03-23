# Derek Cross Python code to show sample to merge dataframes
# Source https://www.kaggle.com/datasnaek/youtube-new
# Trending analysis of YouTube Video Statistics

# importing pandas.
import pandas as pd
#Setting global print options
pd.set_option('display.max_columns',50)
pd.set_option('display.max_rows',100)
pd.set_option('display.width',1000)

#Loading Canadian and British youtube CSV data to PANDAS dataframe.
canadian_youtube = pd.read_csv("CAvideos.csv")
british_youtube = pd.read_csv("GBvideos.csv")
#Print first 5 heads of each dataframe

print(canadian_youtube.head(5))
print(british_youtube.head(5))

#Sample of left and right dataframe on "video_id" index.

merged_data = pd.merge(canadian_youtube, british_youtube, left_on=['video_id'],
             right_on= ['video_id'], how='left')

print(merged_data. head())


# Note I have studied Concat(), Joins() and Merge (with Joins) But comment out of the code.

#print(merged_data.head())

#join_data = left.join(right, lsuffix='_CAN', rsuffix='_UK')

# concat_data= pd.concat([canadian_youtube, british_youtube],axis=1) #columns
# print(concat_data.shape)

# left = canadian_youtube.set_index(['title', 'trending_date'])
# right = british_youtube.set_index(['title', 'trending_date'])
# join_data = left.join(right, lsuffix='_CAN', rsuffix='_UK')
# print(join_data.head(5))
