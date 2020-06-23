'''
this application loads the task.csv data to the table Taskdata in
postgres DB
'''
import os
import sys
import csv
import inspect
import pandas as pd

app_path = inspect.getfile(inspect.currentframe()) # gets the current file directory
sub_dir = os.path.realpath(os.path.dirname(app_path)) # gets the file preceding directory
main_dir = os.path.dirname(sub_dir) # gets the main directory

csv_file = os.path.join(main_dir, "task/task_data.csv") # gets the directory of the task.csv file

project_home = main_dir

sys.path.append(project_home)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DataTask.settings") # get django setting properties
os.environ['DJANGO_SETTINGS_MODULE'] = 'DataTask.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() # get the django web application server.

from showdata.models import Taskdata
# from showdata.serializers import TaskSerializer
# 
# ArticleSet = Taskdata.objects.all()
#
# article_attr = []
#
# for Article in ArticleSet:
#     cont = [Article.id, Article.timestamp, Article.temperature, Article.duration]
#     article_attr.append(cont)
#
# print(pd.DataFrame(article_attr))

with open(csv_file, 'r') as csvfile:
    data_loader = csv.reader(csvfile) # reads the task.csv data
    #print(data_loader)
    next(data_loader) # skips the header names on the csv data

    # create a data object and inputs the data of each columns in the table,
    # this will store all data into the DB table.
    for ind in data_loader:
        #print(ind[1])
        Taskdata.objects.create(
            id = ind[0],
            timestamp = ind[1],
            temperature = ind[2],
            duration = ind[3])