import numpy as np
import pandas as pd
from datetime import date, datetime
import datatransform.read_config as rc


# Helper function to run the wanted transform depending on config file
def exec_function(input_key, *params):
    func_dict = {
        "birthdate_to_age": birthdate_to_age,
        "hot_encoding": hot_encoding,
        "fill_empty_values": fill_empty_values
    }
    func = func_dict.get(input_key)
    return func(*params)


# Helper function for birthday_to_date that returns
# the age with a given birthdate
def calculate_age(birthdate):
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


# Given a date, it computes the age of a person and
# creates a new column with the result.
def birthdate_to_age(df_in, col, new_col):
    df_in[new_col] = df_in[col].apply(calculate_age)


# Given a categorical column with n possible values, it
# replaces it with n binary columns. For example, given the column “color”
# with 3 possible values: “blue”, “red” and “green”, we will create 3 columns:
# “is_blue”, “is_red” and “is_green”, that will be 1 or 0 depending of the
# value of the original column.
def hot_encoding(df_in, col):
    new_cols = df_in[col].unique()
    for new_col in new_cols:
        df_in.loc[df_in[col] == new_col, 'is_' + new_col] = 1
        df_in['is_' + new_col] = df_in['is_' + new_col].fillna(0)


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


# main function
def main():
    df = pd.read_csv(rc.data['source']['path'] + rc.data['source']['dataset'] + '.' + rc.data['source']['format'])

    for i in range(0, len(rc.data['transforms'])):
        for j in range(0, len(rc.data['transforms'][i]['fields'])):
            function_to_run = rc.data['transforms'][i]['transform']
            if function_to_run == 'birthdate_to_age':
                exec_function(function_to_run, df, rc.data['transforms'][i]['fields'][j]['field'],
                              rc.data['transforms'][i]['fields'][j]['new_field'])
            elif function_to_run == 'hot_encoding':
                exec_function(function_to_run, df, rc.data['transforms'][i]['fields'][j])
            elif function_to_run == 'fill_empty_values':
                exec_function(function_to_run, df, rc.data['transforms'][i]['fields'][j]['field'],
                              rc.data['transforms'][i]['fields'][j]['value'])

    if rc.data['sink']['format'] == 'jsonl':
        df.to_json(rc.data['sink']['path'] + rc.data['sink']['dataset'] + '.' + rc.data['sink']['format'],
                   orient='records', lines=True)
    elif rc.data['sink']['format'] == 'parquet':
        df.to_parquet(rc.data['sink']['path'] + rc.data['sink']['dataset'] + '.' + rc.data['sink']['format'])


if __name__ == "__main__":
    main()
