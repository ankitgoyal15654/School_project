from flask_sqlalchemy import SQLAlchemy
import configparser

print("db imported")

db = SQLAlchemy()

cp = configparser.ConfigParser()
cp.read('db_conn.ini')

database = cp.get('sql_conn', 'database')
host = cp.get('sql_conn', 'host')
username = cp.get('sql_conn', 'username')
password = cp.get('sql_conn', 'password')
