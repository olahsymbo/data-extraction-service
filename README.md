## DataTask application 

This django web application is developed for uploading data in ".csv" format to a postgresql database and serving (rendering) the data from the DB in an html.

### Getting Started

To enable this app function properly, install the dependencies in the requirements.txt. Simply run:

`pip3 install -r requirements.txt`

Once all the dependencies have been installed, proceed as follows:

- Create a postgres DB   
- Run upload_data app
- Launch DataTask server

The details of the steps are provided as follows:

### Create a Postgres DB

-  First install postgresql 12.2 (incase it's not installed already).

    One way of doing this is to download the postgresql app from https://postgresapp.com/downloads.html 
    or use homebrew by running:

    `brew install postgresql`

    After installing postgresql, start all postgresql services from terminal by either running (postgres must be running at all times):

    `pg_ctl -D /usr/local/var/postgres start`
    or 
    `brew services start postgresql`

- Second, create a new postgres database named `task` using:

    `CREATEDB task;` 
    
    Afterward, launch the `task` db shell by running:

    `psql task`

    create username and password for the database using:
    
    `CREATE USER admin1 with encrypted password 'admin1';`

    grant all privileges of the db to USER `admin1` using:
    
    `GRANT ALL PRIVILEGES ON DATABASE task TO admin1;`
    
    grant the USER the role to create new db using:
    
    `ALTER USER admin1 CREATEDB;`
    

### Run upload_data app

By completing the first step, we have created a db `task`. The next step is uploading csv data to postgres db. The app for achieving this is `upload_data`.

In order to upload the data, we need to create a db table which will be accessed by our django project model, we need to:

- Create db table

    Go to the project directory 

    `cd DataTask`

    in the project directory, activate the virtual environment:

    `source datataskenv/bin/activate`

    create db table `Taskdata` in the db `task` by running the following: 

    `python3 upload_data/create_db_table.py`

- Upload csv data to db table

    start the web server using:

    `python3 manage.py runserver`

    open another terminal and goto project directory

    `cd DataTask` 

    to upload the `task.csv` data into table `Taskdata`, run:

    `python3 upload_data/stack_data.py`
    
    we can now turn off the web application server (Ctrl + C)

### Launch DataTask server

The main app in DataTask is `showdata`. It contains the data model, views, and url routes

- Again launch the server using:

    `python3 manage.py runserver`

- to view the uploaded data in html, go to:

    `http://127.0.0.1:8000/index.html/`

- to access the admin page, go to:

    `http://127.0.0.1:8000/admin/`

    The admin page login details is:

    username: admin

    password: user1234



