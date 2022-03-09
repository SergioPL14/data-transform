import numpy as np
import pandas as pd
from datetime import date, datetime
import readconfig as rc

path = rc.data['source']['path']
dataset = rc.data['source']['dataset']
format = rc.data['source']['format']

print(path)


df = pd.read_csv('repository/bookings.csv')


# Helper function for birthday_to_date that returns
# the age with a given birthdate
def calculate_age(birthdate):
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


# Given a date, it computes the age of a person and
# creates a new column with the result.
def birthdate_to_date(df_in, col):
    df_in['Age'] = df_in[col].apply(calculate_age)
    print(df_in)


# Given a categorical column with n possible values, it
# replaces it with n binary columns. For example, given the column “color”
# with 3 possible values: “blue”, “red” and “green”, we will create 3 columns:
# “is_blue”, “is_red” and “is_green”, that will be 1 or 0 depending of the
# value of the original column.
def hot_encoding(df_in, col):
    new_cols = df_in[col].unique()
    print(new_cols)
    for new_col in new_cols:
        # print(df_in[col])
        # df_in['is_' + col] = df.apply(lambda row: bin_value(row))
        df_in.loc[df_in[col] == new_col, 'is_' + new_col] = 1
        df['is_' + new_col] = df['is_' + new_col].fillna(0)
    print(df_in)


# It replaces the empty values of a column with another
# value. The value to be replaced with is passed as a parameter and it can
# be a constant or one of the following keywords: “mean”, “median” or
# “mode”. If we pass one of these keywords, we replace the empty values with the
# mean / median / mode of the rest of the elements of the column.
def fill_empty_values(df_in, col, value):
    if value == 'mean':
        value = df_in[col].mean()
    elif value == 'median':
        value = df_in[col].median()
    elif value == 'mode':
        value = df_in[col].mode()[0]
        # Note: mode returns a Series instead of a single number. Since no further criteria was given, we picked the first result.
    df_in[col] = df_in[col].replace(np.NAN, value, regex=True)
    print(df_in['user_name'])


birthdate_to_date(df, 'user_birthdate')
hot_encoding(df, 'vehicle_category')
fill_empty_values(df, 'user_name', 'Dwayne')
