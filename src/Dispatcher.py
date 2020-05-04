# import library for Postgres
import psycopg2
conn = psycopg2.connect(dbname='postgres', user='postgres',
                        password='123', host='localhost')
# Connecting cursor to our Postgres DataBase for interacting with database
cursor = conn.cursor()
# Closing cursor and connection with DataBase
cursor.close()
conn.close()

