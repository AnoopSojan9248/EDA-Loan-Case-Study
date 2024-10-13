#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Import the required Libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ## Data Cleaning 

# ### Data Reading & Data Types 

# In[4]:


#Read the data in pandas
inp0= pd.read_csv("Dress+Sales.csv")
inp1= pd.read_csv("Attribute+DataSet.csv")


# In[5]:


inp1.info()


# You have “Attribute DataSet” which contains a column named “Price”. Choose the correct statement from the following about its data type and variable type.
# - Integer type and numerical variable
# - Object type and categorical ordinal variable
# - Object type and categorical nominal variable
# - Float type and categorical variable.
# 

# There is another column in “Attribute DataSet” named as “Recommendation”, choose the correct statement about its data type and variable type.
# - Integer type and categorical
# - Object type and categorical
# - Integer type and continuous numerical
# - Object type only.
# 

# Which of the following column do you think are of no use in “Attribute DataSet”.
# - Dress_ID
# - Price
# - Size and material
# - NeckLine
# - None of the above
# 

# In[6]:


# Print the information
inp1.info()


# ### Fixing the Rows and Columns 

# As you can see, there is a column in “Attribute Dataset” named as ‘Size’. This column contains the values in abbreviation format. Write a code in Python to convert the followings:
# 
# - M into  “Medium”
# - L into  “Large”
# - XL into “Extra large”
# - free into “Free”
# - S, s & small into “Small”.
# 
# Now once you are done with changes in the dataset, what is the value of the lowest percentage, the highest percentage and the percentage of Small size categories in the column named “Size”?
# 

# In[7]:


inp0.Size= inp1.Size.replace(['S', 'small', 's'], "Small")

inp0.Size= inp1.Size.replace('free', "Free")

inp0.Size= inp1.Size.replace('M', "Medium")

inp0.Size= inp1.Size.replace('L', "Large") 

inp0.Size= inp1.Size.replace('XL', "Extra large")
inp0.Size.value_counts(normalize=True)


# In[8]:


# Print the value counts of each category in "Size" column.


# ### Impute/Remove Missing values

# In[9]:


# Print the null count of each variables of inp0 and inp1.
inp0.isnull().sum()
inp1.isnull().sum()


# You are given another dataset named “Dress Sales”. Now if you observe the datatypes of the columns using ‘inp1.info()’ command, you can identify that there are certain columns defined as object data type though they primarily consist of numeric data.
# 
# Now if you try and convert these object data type columns into numeric data type(float), you will come across an error message. Try to correct this error.
# 
# 
# 
# 
# 
# 

# In[10]:


# Print the data types information of inp1 i.e. "Dress Sales" data.
inp0["14-09-2013"].unique()


# In[11]:


# Try to convert the object type into float type of data. YOU GET ERROR MESSAGE.
inp0.loc[inp0['09-12-2013']== 'Removed',"09-12-2013"] = np.NaN

inp0.loc[inp0['14-09-2013']== 'removed',"14-09-2013"] = np.NaN

inp0.loc[inp0['16-09-2013']== 'removed',"16-09-2013"] = np.NaN

inp0.loc[inp0['18-09-2013']== 'removed',"18-09-2013"] = np.NaN

inp0.loc[inp0['20-09-2013']== 'removed',"20-09-2013"] = np.NaN

inp0.loc[inp0['22-09-2013']== 'Orders',"22-09-2013"] = np.NaN


# In[12]:


# Do the required changes in the "Dress Sales" data set to get null values on string values.


# In[13]:


# Convert the object type columns in "Dress Sales" into float type of data type.


# When you see the null counts in “Dress Sales” dataset after performing all the operations that have been mentioned in jupyter notebook, you will find that there are some columns in “Dress Sales” data where there are more than 40% of missing values. Based on your understanding of dealing with missing values do the following steps.

# In[14]:


# Print the null percetange of each column of inp1.


# In[15]:


# Drop the columns in "Dress Sales" which have more than 40% of missing values.
inp1.head(10)


# You should categorise the dates into seasons in “Dress Sales” data to simplify the analysis according to the following criteria:
# - June, July and August: Summer.
# - September, October and November: Autumn.
# - December, January and February: WInter.
# - March, April and May: Spring.
# 
# 
# 

# In[16]:


# Convert columns to numeric (float)
date_columns = ['09-04-2013', '29-08-2013', '31-08-2013', '09-02-2013', '09-12-2013', '10-12-2013', '09-06-2013', '09-08-2013', '10-06-2013', '09-10-2013', '14-09-2013', '16-09-2013', '18-09-2013', '20-09-2013', '22-09-2013', '24-09-2013', '28-09-2013']

for column in date_columns:
    inp0[column] = inp0[column].astype(float)

# Create the seasons columns
inp0['Spring'] = inp0['09-04-2013']
inp0['Summer'] = inp0['29-08-2013'] + inp0['31-08-2013'] + inp0['09-06-2013'] + inp0['09-08-2013'] + inp0['10-06-2013']
inp0['Winter'] = inp0['09-02-2013'] + inp0['09-12-2013'] + inp0['10-12-2013']
inp0['Autumn'] = inp0['09-10-2013'] + inp0['14-09-2013'] + inp0['16-09-2013'] + inp0['18-09-2013'] + inp0['20-09-2013'] + inp0['22-09-2013'] + inp0['24-09-2013'] + inp0['28-09-2013']


# In[17]:


# calculate the sum of sales in each seasons in inp1 i.e. "Dress Sales".
inp0['Spring'].sum()
inp0['Spring'].sum()


# Now let's merge inp1 with inp0 with left join manner, so that the information of inp0 should remain intact.

# In[18]:


# Merge inp0 with inp1 into inp0. this is also called left merge.
inp0 = pd.merge(left=inp0,right=inp1, how='left', left_on='Dress_ID', right_on='Dress_ID')
inp.head()


# In[ ]:


# Now Drop the Date columns from inp0 as it is already combined into four seasons.
inp0.drop(inp0.loc[:,'29-08-2013':'10-12-2013'].columns, axis= 1, inplace= True)
inp0.isnull().sum()


# Print the null count of inp0 to get the idea about the missing values in data set.

# In[ ]:


# Print the null count of each columns in inp0 dataframe i.e. combined data frame of inp0 and inp1 without date columns.


# You can see that there are two types of variables one with a large number of missing values and another is very less number of missing values. These two columns can be categorized as:
# 
# Type-1: Missing values are very less (around 2 or 3 missing values): Price, Season, NeckLine, SleeveLength, Winter and Autumn. 
# 
# Type-2: Missing values are large in numbers (more than 15%): Material, FabricType, Decoration and Pattern Type.
# 
# 

# In[ ]:


# Deal with the missing values of Type-1 columns: Price, Season, NeckLine, SleeveLength, Winter and Autumn.
inp0 = inp0[~inp0.Price.isnull()]

inp0 = inp0[~inp0.Season.isnull()]

inp0 = inp0[~inp0.NeckLine.isnull()]

inp0 = inp0[~inp0.SleeveLength.isnull()]

inp1 = inp1[~inp1.Winter.isnull()]

inp1 = inp1[~inp1.Autumn.isnull()]


# In[ ]:


# Deal with the missing values for Type-2 columns: Material, FabricType, Decoration and Pattern Type.
inp0


# ### Standardise value 

# In the given dataset, there are certain discrepancies with the categorical names such as irregular spellings. Choose the correct option of columns with irregular categories and update them.
#  
# - Season, NeckLine
# - Price, Material
# - fabricType, Decoration
# - Season, SleeveLength
# 

# In[ ]:


#correcting the spellings.
inp1["Style"].value_counts()


# In[ ]:


#correcting the Spellings.


# ## Univariate Analysis 

# ### Categorical Unordered Univariate Analysis
#  

# There is a column named ‘Style’ in ‘Attribute Dataset’ which consists of the different style categories of the women apparels. Certain categories whose total sale is less than 50000 across all the seasons is considered under one single category as ‘Others’.
# 

# Which of the following categories in ‘Style’ column can be grouped into ‘Others’ category? and perform the grouping operation in the notebook for further analysis.
# - Flare, fashion
# - Novelty, bohemian
# - OL, fashion, work
# - Novelty, fashion, Flare
# 

# In[ ]:


#data = inp0.merge(inp1[['Dress_ID', 'Style']], on='Dress_ID', how='left')
#data['Sum_1_to_13'] = data.iloc[:, 1:13].sum(axis=1)
style = data.iloc[:, 40:43]


# In[ ]:


style


# In[ ]:


style_sums = style.groupby('Style_y')['Sum_1_to_13'].sum().reset_index()
style_sums


# In[ ]:


count_less_than_50000 = style_sums[style_sums['Sum_1_to_13'] < 50000]
count_less_than_50000


# # Group "Style" categories into "Others" which have less than 50000 sales across all the seasons.
# 

# What is the percentage of “cute” and “Others” category in “Style” column in “Attribute DataSet” respectively?
# - 46%, 5%
# - 9%, 2.1%
# - 2.1%, 5%
# - 13.8%, 9%
# 

# In[ ]:


# Calculate the percentage of each categories in the "Style" variable.


# Similarly Club Neckline, SLeeve length categories into "Others" which have less than 50000 sales across all the seasons.

# In[ ]:


# Group "Neckline" categories into "Others" which have less than 50000 sales across all the seasons.


# In[ ]:


# Group "Sleeve length" categories into "Others" which have less than 50000 sales across all the seasons.


# Club material, fabrictype, patterntype and decoration categories into "Others" which have less than 25000 sales across all the seasons

# In[ ]:


# Group "material" categories into "Others" which have less than 25000 sales across all the seasons.


# In[ ]:


# Group "fabric type" categories into "Others" which have less than 25000 sales across all the seasons.


# In[ ]:


# Group "patern type" categories into "Others" which have less than 25000 sales across all the seasons.


# In[ ]:


# Group "decoration" categories into "Others" which have less than 25000 sales across all the seasons.


# ### Caregorical Ordered Univariate Analysis

# Which of the following is an unordered variable in “Attribute DataSet”.
# - Style
# - Price
# - Season
# - Size
# 

# ### Numerical variable Univariate analysis:

# What is the approximate difference between the maximum value and 75th percentile in “Autumn” column.
# - Approx 54000
# - Approx 55000
# - Approx 52000
# - Approx 50000
# 
# 

# In[ ]:


# Describe the numerical variale: "Autumn".


# In[ ]:


# plot the boxplot of "Autumn" column.


# Which of the following season has the highest difference between the maximum value and 99th quantile of sales?
# - Winter
# - Summer
# - Spring
# - Autumn
# 

# In[ ]:


# Find the maximum and 99th percentile of Winter season.


# In[ ]:


# Find the maximum and 99th percentile of Summer season.


# In[ ]:


# Find the maximum and 99th percentile of Spring season.


# In[ ]:


# Find the maximum and 99th percentile of Autumn season.


# ## Bivariate Analysis 

# ### Numerical- Categorical analysis

# Which of the following “Price” category has the lowest average value of rating?
# - very-high
# - Medium
# - Low
# - High (Answer)
# 

# In[ ]:


# Find the Mean of Ratings for each Price category.
avg=inp1.groupby("Price")["Rating"].mean()
avg


# What is the median of the rating of “vintage” category in Style column?
# - 4.6(Answer)
# - 4.7
# - 4.55
# - 0.00
# 

# In[ ]:


# Find the median of Ratings for each Style category.
inp1.groupby("Style")["Rating"].median()


# Which of the following season has the highest average value of sale for “Recommendation” value equals to 1.
# - Summer
# - Spring
# - Autumn
# - Winter
# 

# In[ ]:


inp0['Spring'] = inp0.apply(lambda x: x['09-04-2013'], axis=1,)

inp0['Summer'] = inp0.apply(lambda x: x['29-08-2013'] + x['31-08-2013']+ x['09-06-2013']+ x['09-08-2013']+ x['10-06-2013'], axis=1)

inp0['Winter'] = inp0.apply(lambda x: x['09-02-2013'] + x['09-12-2013']+ x['10-12-2013'], axis=1)

inp0['Autumn'] = inp0.apply(lambda x: x['09-10-2013'] + x['14-09-2013']+ x['16-09-2013']+ x['18-09-2013']+ x['20-09-2013']+ x['22-09-2013']+ x['24-09-2013']+ x['28-09-2013'], axis=1)


# In[ ]:


inp1


# In[ ]:


# Summer sale vs Recommendation.


# In[ ]:


# Spring sale vs Recommendation.


# In[ ]:


# Autumn sale vs Recommendation.


# In[ ]:


# Winter sale vs Recommendation.


# ### Categorical categorical bivariate analysis
# 

# Which of the following size categories has the highest positive recommendations?
# - Medium and extra large
# - Extra large and small
# - Free and small
# - Free and medium(Answer)
# 

# In[ ]:


# Size vs Recommendation.
res=inp1[inp1.Recommendation==1]
merged = inp1.merge(res, on='Size', how='inner')

merged.groupby("Size")["Recommendation_y"].sum()


# ### Multivariate analysis 

# Which of the following pair of “Style” and “Price” category has the highest average of positive recommendations?
# - Price: medium and style: vintage
# - Price: medium and style: cute(Answer)
# - Price: very high and style: party
# - Price: low and style: sexy
# 

# In[ ]:


# plot the heat map of Style, price and Recommendation.
piv=pd.pivot_table(data=inp1,index="Style",columns="Price",values="Recommendation")
sns.heatmap(piv,annot=True)


# Which of the following material type has no recommendation in summer and winter seasons?
# - Mix and Milksilk
# - Nylon and Rayon
# - Microfiber and Silk (Anser)
# - Milksilk and Microfiber
# 

# In[ ]:


# plot the heat map of Season, material and Recommendation.
piv1=pd.pivot_table(data=inp1,index="Season",columns="Material",values="Recommendation")
sns.heatmap(piv1,annot=True)


# In[ ]:


inp1.head(2)


# In[ ]:





# In[22]:


print(inp0.groupby('Recommendation')['Autumn'].mean())


# In[ ]:





# In[ ]:




