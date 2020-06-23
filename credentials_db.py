import os
'''
this is create to store the paramters of connecting postgres in
enviroment variable. 
the point of this is to conceal such connection parameters from
client side. 
this credentials_db.py will normally not be committed to a repository, 
but scp to the server.
'''
# Set environment variables for other
os.environ['engine'] = 'django.db.backends.postgresql_psycopg2'
os.environ['name'] = 'task'
os.environ['user'] = 'admin1'
os.environ['password'] = 'admin1'
os.environ['host'] = 'localhost'
os.environ['port'] = '5432'