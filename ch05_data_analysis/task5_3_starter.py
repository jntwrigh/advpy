"""
        task 5_3_starter.py - retrieve the top 100 batting averages from the provided source file:
                                <student_files>/resources/baseball/Batting.csv

                            - remove any rows where the 'atbats' was less than 502 (the official statistic).

"""
import numpy as np
np.set_printoptions(precision=3, suppress=True)

# Step 1. Read from the file.  Identify the delimiter.  We need columns 6 & 8 from the file.
#         You should also skip the first line.


# Step 2. Remove any rows with atbats that are less than 502.  Hint, use:
#                    results = results[column >= 502]

# Step 3. Remove any rows for the year earlier than 1957.  Hint, use:
#                    results = results[column >= 1957]

# Step 4. Calculate the averages.


#         Join the hits, atbats, and averages columns together.  You can use several
#         techniques.  column_stack() might be the most straight forward.


# Step 5. Use the argsort() technique shown in the slides to sort the data
#         based on the averages column.


# Step 6. Display the final values.
