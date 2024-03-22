import re

import pandas as pd

from sqlalchemy import create_engine
import pymysql


def datetime_to_timestamp(datetime_int):
    # print(datetime_int)
    datetime_str = str(datetime_int)
    if datetime_str == 'nan':
        return pd.NaT

    # print(datetime_str)
    match_dot = re.search(r'\.', datetime_str)
    match_plus = re.search(r'\+', datetime_str)
    if match_dot:
        datetime_str = datetime_str.split('.')[0]
        # datetime_str += ':00'
    elif match_plus:
        datetime_str = datetime_str.split('+')[0]
    return datetime_str


def str_to_bool(s):
    print(s)
    if s == 'TRUE':
        bool_s = True
        return bool_s
    elif s == 'FALSE':
        bool_s = False
        return bool_s


# print(datetime_to_timestamp('2024-02-15 23:24:49+00:00'))
# print(datetime_to_timestamp('2024-02-16 02:06:24.226765+00:00'))


"""
# Load CSV file into DataFrame
df = pd.read_csv('articles_data/articles_data.csv')

# drop id = 30
df = df[df['id'] != 30]


datetime_columns = ['published_at', 'created_at', 'update_at', 'deleted_at']
for column in datetime_columns:
    df[colum] = df[column].replace('', pd.NaT)

# # Save DataFrame back to CSV file
df.to_csv('./articles_data/articles_processed.csv', index=False)


"""


def insert_csv_to_pymysql(engine, filepath, table):
    df = pd.read_csv(filepath)
    df.to_sql(table, con=engine, if_exists='replace')
    sql_query = f'SELECT * FROM {table} data LIMIT 5'
    df2 = pd.read_sql_query(sql_query, engine)
    print(df2.head())


def connect_to_pymysql():
    host = 'localhost'
    port = 3306
    user = 'root'
    password = 'user1'
    database = 'testsite'

    engine = create_engine(
        'mysql+pymysql://root:user1@localhost:3306/testsite'
    )

    return engine


if __name__ == "__main__":
    engine = connect_to_pymysql()
    insert_csv_to_pymysql(engine, "articles.csv", "articles")


