"""
        task 7_1_starter.py
            - Use Pandas to complete the Batting average exercise:
                          - Display the top 100 batting averages
                          - Find the 50% average
                          - Plot the averages vs. atbats

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
np.set_printoptions(suppress=True, precision=3)

# Step 1. read from the file using read_csv().  Read the year, atbats, and hits columns.


# Step 2. Filter records using Boolean indexing.  Use .loc[] and Boolean
#          indexing.  Keep records with 502 or more atbats and year >= 1957


# Step 3. Calculate the averages.  You can easily create a new column in Pandas
#         by referencing a new column name:
#                   data['new_col'] = data['colA'] / data['colB']
#
#         No need to column_stack()


# Step 4. Sort the array values.  Obtain the 50% value using the describe() function.


# Step 5. Plot the values as we did before.  Use df.plot(kind='scatter', x='col', y='col')
#         Don't forget to show() it!

