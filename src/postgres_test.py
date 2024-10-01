import psycopg2
import os

connection = psycopg2.connect(
  database=os.environ["DB_DB"], \
  user=os.environ["DB_USER"], \
  password=os.environ["DB_PASS"], \
  host=os.environ["DB_HOST"], \
  port=5432)

cursor = connection.cursor()
cursor.execute("SELECT first_name, last_name from public.actor")
# Fetch all rows from database
record = cursor.fetchall()
print("Data from Database:- ")
print(record)
