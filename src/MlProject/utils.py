import os
import sys
import pandas as pd
import pymysql
from dotenv import load_dotenv
from src.MlProject.exception import CustomException
from src.MlProject.logger import logging

load_dotenv()
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')


def read_mysql_data():
    try:
        logging.info("Connection is Establishing")
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=database
        )
        logging.info("Connection Established", connection)
        df = pd.read_sql_query("SELECT * FROM cancer;", connection)
        print(df.head())
        return df
    except Exception as ex:
        raise CustomException(ex, sys)




read_mysql_data()

