import os

# Set environment variables for other
os.environ['engine'] = 'django.db.backends.postgresql_psycopg2'
os.environ['name'] = 'task'
os.environ['user'] = 'admin1'
os.environ['password'] = 'admin1'
os.environ['host'] = 'localhost'
os.environ['port'] = '5432'