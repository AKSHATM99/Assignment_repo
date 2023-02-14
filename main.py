# Spatic Assignment
# By - Akshat Mishra
# Mail - mails.akshat@gmail.com


# First of all we are importing necessary modules
# Here 'geopy' library is used for calculating 'geodesic distance or the great-circle distance' between two points
# 'enchant' library is used for calculating 'Levenshtein_distance' between two names(strings)
# 'pandas' library is used for importing dataset and used in further 'dataframe' manipulation

import geopy 
import enchant
import pandas as pd
pd.set_option('mode.chained_assignment', None) # This statement is used for avoiding 'chained_assignment' warning


# In this step we are importing dataset file in our program as a 'dataframe' by using "pd.read_csv" function of pandas library
df = pd.read_csv(r"assignment_data.csv")


# Function for calculating 'geodesic distance or the great-circle distance'
# We are using 'distance' method of geopy library
# Function accepts a 'tuple' type of data having 2 separate values like- (lat, log) = (12.2255, 77.12165)
# This (lan, lon) tuple is passed as an arguments to the function 
# Here function is returning 'int' type of values those are in 'meters'
def dist(name1, name2):
    d = int(geopy.distance.distance(name1, name2).meters)
    return d


# Function for calculating 'Levenshtein_distance' between two names(strings)
# 'utils.levenshtein' method is used from the 'enchant' library
# Function accepts 'string' type of data as arguments
# names are passed as an arguments to the function
# Function is returning 'int' type value which is reffered as 'edit_distance'
def similarity(name1, name2):
    return enchant.utils.levenshtein(name1, name2)


# Adding a new column in the dataframe
# Initially column have no values
df['is_similar'] = ''


# Creating an empty array for storing "0 or 1" values 
arr = []


# A 'while' loop is used for traversing the whole dataset(range of loop = length of dataframe)

# Main Logic :
#     1 - First of all here we are checking if we are at the last index of the df or not
#     2 - If 'yes' then we append '0' in our above defined arr
#     3 - '0' is appended because now we don't have any other datapoint left for matching with this current datapoint
#     4 - If 'no' then we perform our calculation by calling our 'distance' and 'similarity' functions
#     5 - Now we check our condition if distance is less than '200 meters' and 'edit_distance' is less than '5'
#     6 - If 'yes' then we append '1' two times because now our current value(i) is matching with the value (i+1) i.e the next value
#     7 - and we increment 'i' two because now we don't want to check for the next value 
#     8 - If our main condition (distance is less than '200 meters' and 'edit_distance' is less than '5') is not 'true'
#     9 - then append '0' and increment 'i' to '+1'

i = 0
while i<len(df):
    if i==len(df)-1:
        arr.append(0)
        break
    name1 = (df.iloc[i][1], df.iloc[i][2])
    name2 = (df.iloc[i+1][1], df.iloc[i+1][2])
    name1_str = df.iloc[i][0]
    name2_str = df.iloc[i+1][0]
    d = dist(name1, name2)
    sim = similarity(name1_str, name2_str)
    if d<200 and sim<5:
        arr.append(1)
        arr.append(1)
        i += 2
    else:
        arr.append(0)
        i += 1

# Time Complexity for loop:

# Assume that we have a dataframe of lenght 'n' and have 'k' number of consecutive pairs(set of 2) of similar strings which satisfy our condtion then :
#      Time Complexity = O(n - k)

# Here 'arr.append' is taking constant time i.e. O(1)
# Our program is using pandas which is already optimized for performance and memory


# Populating 'is_similar' column by 'arr'
df['is_similar'] = arr


# Preview of output
df.head()


# Exporting output in 'csv' format
df.to_csv('result.csv')