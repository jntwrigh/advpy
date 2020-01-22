"""
    task7_2_starter.py  -   Groupby and Pandas

        Using our Batting.csv file, your task was to answer two questions:
            1. Which team has hit the most home runs (cumulative)?
            2. Which team hit the most home runs in 2015?

Then, plot the total home runs hit per decade to see which decade had the most.


"""
import pandas as pd

filename = '../resources/baseball/Batting.csv'

# Step 1: Use Pandas to read ALL DATA from Batting.csv file into a DataFrame.  Use the
#         first line from the file as the column names.


# Step 2: Check the shape and inspect the info() on the DataFrame



# Step 3: Answer question 1: Which team has hit the most home runs (cumulative)?
#         Hint: Groupby teamID, perform a sum() on the groups, sort by largest HR.



# Step 4: Answer question 2: Which team hit the most home runs in 2015?
#         Hint: Filter out all records that are not from the yearID 2015, then
#         groupby teamID, perform a sum() on the groups, sort by largest HR.



# Step 5: Define your decade (bins) starting from 1870 going up to 2020.
#         Hint: it's just a list.  : )



# Step 6: Use Pandas cut() to break the yearID column into decades.  You can create
#         a new column called 'hr_decade' or something similar.


# Step 7: Plot the HRs for each decade as a 'barh' plot.
#         Hint: first groupby 'hr_decade', sum() the groups, then plot only the HR column.
