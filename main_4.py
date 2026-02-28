# Mastering Pandas: 100 Exercises with solutions for Python data analysis

import pandas as pd

# Exercise 1:
# Create a DataFrame from a dictionary of lists.
# data = {"x":[1,2,3,4],
#         "y":[5,6,7,8]
#         }
# df = pd.DataFrame(data)
# print(df)

# Exercise 2:
# Select the first 3 rows of a DataFrame.
# data = {"x":[1,2,3,4],
#         "y":[5,6,7,8]
#          }
# df = pd.DataFrame(data)
# print(df.head(3))

# Exercise 3:
# Select the 'X' column from a DataFrame.
# data = {"x":[1,2,3,4],
#         "y":[5,6,7,8]
#          }
#
# df = pd.DataFrame(data)
# print(df["x"])

# Exercise 4:
# Filter rows based on a column condition.
# data = {"x":[1,2,3,4],
#         "y":[5,6,7,8]
#          }
# df = pd.DataFrame(data)
# filter_rows = df[df["x"]>2]
# print(filter_rows)

# Exercise 5:
# Add a new column to an existing DataFrame.
# data = {"x":[1,2,3,4],
#         "y":[5,6,7,8]
#          }
#
# df = pd.DataFrame(data)
# df["z"] = df["x"] * df["y"]
# print(df)