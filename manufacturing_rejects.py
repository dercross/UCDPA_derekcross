# Derek Cross
# Python project code to analysis High Volume medical device manufacturing rejects on Feb 2021 data.
# I have gather CSV file from Microsoft SQL database and saved to .csv file
# The goal is to analysis the top reject (Yield hitters) for the manufacturing line.


#import libary.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def csvdata_import(filename):
    data = pd.read_csv(filename)
# Take first look to understand the dataset.
# print top 5 column header.
# print shape(number of row by columns in a dataframe)
# print Names of columns, data types they contain, and if have any missing values.
    print(data.head(5), data.shape, data.info)
    return data

def missing_data():
# Call import CSV file load to dataframe  importing. display data shape, info, description.
# csvdata_import(). no need to call function as used in missing data function

    data = csvdata_import("reject_data_feb2021.csv")
# Adding.sum to show how many missing data in my data set there are none.
    missing_values = data.isnull().sum()
    print(missing_values)
(missing_data())

def clean_data():
# Clean all missing data
# descriptive data to fill with NA as not required for analysis.
# Decided to use fillna("NA") as best fit to clean the data.

# call  csvdata_import function
    data = csvdata_import("reject_data_feb2021.csv")

#Clean data fill blanks with "NA"
    cleaned_data = data.fillna("NA")
#In this dataframe I don not need to drop column or rename a column.
# See python code below on how I would drop or rename column in my Dataframe
#drop column Station to show can drop a Column in a dataframe
    #cleaned_data = data.drop(['Station'], axis=1)
#Rename Column Part_Category to Category
    #data.rename(columns={'Part_Category': 'Category'})

    return cleaned_data

def sort_data():
    data = clean_data()
#Using index Set first column to dates
    data.set_index("TIME", inplace=True)
#sort column Date of Sale  by ascending order
    data.sort_values(["TIME"], ascending=[True])
    return data

#Call clean data function.
clean_data()

#Call clean data function to clean missing data found
#data = (clean_data())
# #print(data.head(5), data.shape)
# # Call Sort data

#Called sorted_data function of the data_frame.
data = (sort_data())

# #print the top few rows.
# print(data.head(5), data.shape, data.info)


# #Analysing data and charts:
#
# Count the Category rejects and ouput charts.
# Charts using import seaborn as sns


#Chart1
#Using Mat plolib first.
#Counting the values of reject of Part_Group
data['Part_Group'].value_counts(sort=True).plot(kind='barh', figsize=(10,7))
#Turn bar chart Horizontal
#Adding labels
plt.xlabel("Count of Rejects", fontsize=14,labelpad=2)
plt.ylabel("Part", fontsize=14, labelpad=2)
#Adding legend and Title
plt.legend(['Part_Group'])
plt.title("Total count of rejects by part in the month (Feb2021)", fontsize=18, y=1.02);
# Display the plot with plt.show()
plt.show()



#Chart1
#Count the Rejects per Circuit & Cell and Graph results using Seaborn.
g= sns.catplot(y="Part_Group", data =data,kind="count", palette="Set2", height=5,aspect=1.5, legend=False)
ax = plt.gca()
ax.set_facecolor('xkcd:pale blue')
ax.legend(['Part_Group'])
# Change seaborn plot size
fig = plt.gcf()
# Change seaborn plot size
fig.set_size_inches(8, 8)
# set rotation
g.set_xticklabels(rotation=90, horizontalalignment='left')
plt.title("Total count of rejects by part in the month (Feb2021)", size=18)
#legend not needed as each bar is labeled.
#plt.legend(['Count of Rejects'])
#Adding labels
plt.xlabel("Count of Rejects", size=14)
plt.ylabel("Part", size=14)
plt.tight_layout()
#plt.savefig("Part_Group_rejects.png")
plt.show()

#Chart2
#Count the Rejects per Circuit & Cell and Graph results using Seaborn.
g= sns.catplot(y="Circuit & Cell", data =data,kind="count", palette="Set2")
ax = plt.gca()
ax.set_facecolor('xkcd:pale blue')
# Change seaborn plot size
fig = plt.gcf()
# Change seaborn plot size
fig.set_size_inches(8, 8.5)
# set rotation
g.set_xticklabels(rotation=90, horizontalalignment='left')
plt.title("Total count of rejects by Circuit & Cell in the month (Feb2021)")
#legend not needed as each bar is labeled.
#plt.legend(['Count of Rejects'])
#Adding labels
plt.xlabel("Count of Rejects", size=12)
plt.ylabel("Circuit & Cell", size=12)
#plt.legend(loc="upper left", bbox_to_anchor=(1,1))
plt.show()

#Chart3
#Count the Rejects per Station and Graph results using Seaborn.
g= sns.catplot(y="Station", data =data,kind="count", palette="Set2")
ax = plt.gca()
ax.set_facecolor('xkcd:pale blue')
# Change seaborn plot size
fig = plt.gcf()
# Change seaborn plot size
fig.set_size_inches(8, 8.5)
# set rotation
g.set_xticklabels(rotation=90, horizontalalignment='left')
plt.title("Total count of rejects by Station in the month (Feb2021)", size=16)
#legend not needed as each bar is labeled.
#plt.legend(['Count of Rejects'])
#Adding labels
plt.xlabel("Count of Rejects", size=12)
plt.ylabel("Station", size=12)
#plt.legend(loc="upper left", bbox_to_anchor=(1,1))
plt.show()

#Chart4
#Count the Rejects for Failure description and Graph results using Seaborn.
g= sns.catplot(y="Failure Description", data =data,kind="count", palette="Set2")
ax = plt.gca()
ax.set_facecolor('xkcd:pale blue')
# Change seaborn plot size
fig = plt.gcf()
# Change seaborn plot size
fig.set_size_inches(10, 10)
# set rotation
g.set_xticklabels(rotation=90, horizontalalignment='left')
# Set title for plot
plt.title("Total count of rejects by Failure Description (Feb2021)", loc='center', size=12)
#legend not needed as each bar is labeled.
#plt.legend(['Count of Rejects'])
#Adding labels
plt.xlabel("Count of Rejects", size=12)
plt.ylabel("Failure Description", size=12)
#plt.legend(loc="upper left", bbox_to_anchor=(1,1))
plt.show()


#Chart5
#Count the Rejects per Operation and Graph results using Seaborn.
g= sns.catplot(y="Operation", data =data,kind="count", palette="Set2")
ax = plt.gca()
ax.set_facecolor('xkcd:pale blue')
# Change seaborn plot size
fig = plt.gcf()
# Change seaborn plot size
fig.set_size_inches(10, 10)
# set rotation
g.set_xticklabels(rotation=90)
plt.title("Total count of rejects by Operation (Feb2021)",loc='center', size=11)
#plt.legend(['Count of Rejects'])
#Adding labels
plt.xlabel("Count of Rejects", size=12)
plt.ylabel("Operation", size=12)
#plt.legend(loc="upper left", bbox_to_anchor=(1,1))
plt.show()




sns.jointplot(x='Part_Group', y='Circuit & Cell', data=data)
ax = plt.gca()
# # Change seaborn plot size
fig = plt.gcf()
# # Change seaborn plot size
fig.set_size_inches(12, 12)
# # set rotation
g.set_xticklabels(rotation=90)
#plt.title("Total count of rejects part_group by Circuit& Cell",loc='center', size=11)
plt.legend(['Count of Rejects'])
plt.legend(loc="upper left", bbox_to_anchor=(1,1))
plt.show()

# sns.jointplot(x='Circuit & Cell', y='Part_Group', data=data)
# ax = plt.gca()
# # # Change seaborn plot size
# fig = plt.gcf()
# # Change seaborn plot size
# fig.set_size_inches(10, 10)
# # set rotation
# g.set_xticklabels(rotation=90)
# plt.title("Total count of rejects Circuit & Cell by Part_Group in the month (Feb2021)")
# plt.legend(['Count of Rejects'])
# plt.show()
#
# sns.jointplot(x='Station', y='Part_Group', data=data)
# ax = plt.gca()
# # # Change seaborn plot size
# fig = plt.gcf()
# # Change seaborn plot size
# fig.set_size_inches(10, 10)
# # set rotation
# g.set_xticklabels(rotation=90)
# plt.title("Total count of rejects Circuit & Cell by Part_Group in the month (Feb2021)")
# plt.legend(['Count of Rejects'])
# plt.legend(loc="upper left", bbox_to_anchor=(1,1))
# plt.show()


# sns.jointplot(x='Part_Group', y='Part_Category', data=data)
# ax = plt.gca()
# # # Change seaborn plot size
# fig = plt.gcf()
# # Change seaborn plot size
# fig.set_size_inches(12, 12)
# # set rotation
# g.set_xticklabels(rotation=90)
# plt.title("Total count of rejects Circuit & Cell by Part_Group in the month (Feb2021)")
# plt.legend(['Count of Rejects'])
# plt.legend(loc="upper left", bbox_to_anchor=(1,1))
# plt.show()




data.groupby(["Part_Group", "Circuit & Cell"], as_index=False)["Part_Category"].count()
print(data)

# Slicing
# Example code to show to when selecting "fetching data" pandas data using “iloc”
# Single selections using iloc and DataFrame

# Rows:
data.iloc[0] # first row of data frame
data.iloc[1] # second row of data frame
data.iloc[-1] # last row of data frame
# Columns:
data.iloc[:,0] # first column of data frame
data.iloc[:,1] # second column of data frame
data.iloc[:,-1] # last column of data frame
# Multiple row and column selections using iloc and DataFrame
data.iloc[0:5] # first five rows of dataframe
data.iloc[:, 0:2] # first two columns of data frame with all rows

print(data.iloc[0])

# Example code to show to when selecting pandas data using “Loc”
# Single selections using loc and DataFrame

# Previously set_index in the dataframe in the function sort_data():
# data.set_index("Day", inplace=True)
#data.loc ['4'] #All the purchases from 04 Jan 2010
#print(data.loc ['4'])
data.loc[data['Part_Group'] =='Introducer']
data_by_part = data.loc[data['Part_Group'] =='Introducer']
print(data_by_part)
#Slicing by dates
#data.loc["04/01/2010":"07/01/2010"]
#print (data.loc["04/01/2010":"07/01/2010"])

#Iterating DataFrames with iterrows()
#Loop over my DataFrame
#Using for loop to show iterating to get the entire row-data of an index
#i represents the index column
# for i, row in data.iterrows():
# 	print(f"Index: {i}")
# 	print(f"{row}\n")

#Sample printing out all thats in is in the Failure Description column
for i, row in data.iterrows():
    print(row['Failure Description'])

