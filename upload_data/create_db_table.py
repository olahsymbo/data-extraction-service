import psycopg2
from credentials_db import *
import warnings
warnings.filterwarnings("ignore")

# get the postgres db connection parameters from environment variable
name = os.environ.get('name')
user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')
port = os.environ.get('port')

# connect an instance of postgres DB
con = psycopg2.connect(database= name, user= user, password= password, host= host, port= port)
print("Database opened successfully")

cur = con.cursor()

# create a table "Taskdata" in db "task" in our postgres
cur.execute('''CREATE TABLE Taskdata
      (id VARCHAR(250) PRIMARY KEY, 
      timestamp TIMESTAMP,
      temperature VARCHAR(250) NOT NULL,
      duration VARCHAR(250) NOT NULL);''')
print("Table created successfully")
con.commit()
con.close() # commit and close connection