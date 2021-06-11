import os
from dotenv import load_dotenv
import warnings

warnings.filterwarnings("ignore")

load_dotenv()
# get the postgres db connection parameters from environment variable
name = os.getenv("DATABASE_NAME")
user = os.getenv("DATABASE_USERNAME")
password = os.getenv("DATABASE_PASSWORD")
host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT")
